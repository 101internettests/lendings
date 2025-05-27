import os
from datetime import datetime
from typing import Optional
import allure
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
load_dotenv()

# Преобразуем значение HEADLESS в bool
HEADLESS_ENV = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page


@pytest.fixture(scope="session")
def launch_options():
    return {
        "headless": HEADLESS_ENV
    }


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()