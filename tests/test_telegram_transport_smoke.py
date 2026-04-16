from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _load_root_conftest_module() -> ModuleType:
    """Load repo-root conftest.py explicitly to avoid xdist import collisions."""
    repo_root = Path(__file__).resolve().parents[1]
    conftest_path = repo_root / "conftest.py"

    repo_root_str = str(repo_root)
    if repo_root_str not in sys.path:
        sys.path.insert(0, repo_root_str)

    spec = importlib.util.spec_from_file_location("lendings_root_conftest", conftest_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load root conftest from {conftest_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


alerts_module = _load_root_conftest_module()


class _DummyBot:
    def __init__(self):
        self.calls = []

    def send_message(self, chat_id, text):
        self.calls.append((chat_id, text))


class _DummyResponse:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text


def test_proxy_off_uses_direct_transport(monkeypatch):
    bot = _DummyBot()
    monkeypatch.setattr(alerts_module, "ALERTS_ENABLED", True)
    monkeypatch.setattr(alerts_module, "USE_TELEGRAM_PROXY", False)
    monkeypatch.setattr(alerts_module, "bot", bot)
    monkeypatch.setattr(alerts_module, "chat_id", 123456)

    alerts_module._send_telegram_message("runtime alert body")

    assert bot.calls == [(123456, "runtime alert body")]


def test_proxy_on_uses_proxy_transport(monkeypatch):
    sent = {}

    def _fake_post(url, headers, json, timeout):
        sent["url"] = url
        sent["headers"] = headers
        sent["json"] = json
        sent["timeout"] = timeout
        return _DummyResponse(status_code=200, text='{"ok":true}')

    monkeypatch.setattr(alerts_module, "ALERTS_ENABLED", True)
    monkeypatch.setattr(alerts_module, "USE_TELEGRAM_PROXY", True)
    monkeypatch.setenv("TELEGRAM_PROXY_URL", "https://proxy.example/send")
    monkeypatch.setenv("TELEGRAM_PROXY_AUTH_SECRET", "secret")
    monkeypatch.setenv("TELEGRAM_PROXY_CREDS", "creds")
    monkeypatch.setattr(alerts_module.requests, "post", _fake_post)

    alerts_module._send_telegram_message("runtime alert body")

    assert sent["url"] == "https://proxy.example/send"
    assert sent["headers"]["X-Authentication"] == "secret"
    assert sent["json"]["text"] == "runtime alert body"
    assert sent["json"]["creds"] == "creds"
    assert sent["timeout"] == alerts_module.TELEGRAM_PROXY_TIMEOUT_SEC


def test_proxy_on_missing_env_fails_fast(monkeypatch, capsys):
    def _should_not_call(*args, **kwargs):
        raise AssertionError("proxy request must not be executed when env is missing")

    monkeypatch.setattr(alerts_module, "ALERTS_ENABLED", True)
    monkeypatch.setattr(alerts_module, "USE_TELEGRAM_PROXY", True)
    monkeypatch.setattr(alerts_module, "_PROXY_MISSING_ENV_LOGGED", False)
    monkeypatch.delenv("TELEGRAM_PROXY_URL", raising=False)
    monkeypatch.delenv("TELEGRAM_PROXY_AUTH_SECRET", raising=False)
    monkeypatch.delenv("TELEGRAM_PROXY_CREDS", raising=False)
    monkeypatch.setattr(alerts_module.requests, "post", _should_not_call)

    alerts_module._send_telegram_message("runtime alert body")

    out = capsys.readouterr().out
    assert "Missing required env vars" in out
