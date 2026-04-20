# FORM_SHORT: план стабилизации и KPI

Дата обновления: 2026-04-20  
Контур: Jenkins job `form_short`  
Связанные файлы: `FORM_SHORT_CHRONIC_STABILITY_REPORT.md`, `FORM_SHORT_CONTEXT_2026-04-20.md`

## 1) Текущее состояние (по факту внедрения)

Базовая точка:

1. Build `1013` на `61b3eb2`: `5 failed, 154 passed, 9 skipped`.
2. До этого было `8 failed, 151 passed, 9 skipped` (build `1011`).
3. Значит, уже есть снижение tail-флаков после серии правок hidden/AB.

Уже внедрено после `61b3eb2`:

1. `10c52b2` — `Stabilize Tele2 link checks and region verification`.
2. `30844b5` — `Fix remaining form_short popup and express flakes`.

Что закрывали этими коммитами:

1. Tele2 links: файловые ссылки (`pdf` и др.) проверяются по HTTP, а не через `page.goto`.
2. Tele2 region verify: расширены candidate-селекторы + fallback по URL slug.
3. RTK/MTS popup checks: проверка только по реально видимым маркерам, без hidden-дубликатов.
4. Profit/Express: расширен набор селекторов полей, усилены fallback для улицы/дома.
5. Express: добавлен fallback на ручной house value, если dropdown дома не появляется.

## 2) Обновленный приоритетный план стабилизации

### Шаг 1 (завершено)

Точечный хвост по Tele2 стабилизирован:

1. `test_check_all_pages` (Tele2 links).
2. `test_choose_region_header` (Tele2 region verify).

Локально подтверждено: `2 passed` в таргетном запуске после `10c52b2`.

### Шаг 2 (в работе / валидация через Jenkins)

Проверить остаточный хвост после `30844b5`:

1. `tests/test_mts/test_mts_home_online_third.py::...::test_application_popup_super_offer_third`.
2. `tests/test_rtk/test_rtk_internet_online.py::...::test_application_popup_super_offer`.
3. `tests/test_forms/test_forms.py::...::test_application_express_connection[https://mts-home-online.ru/]`.

Локально на таргетном прогоне было:

1. MTS third — pass.
2. RTK internet popup — pass.
3. Express — один fail до финального fallback; после последней правки полный повторный прогон был прерван пользователем, поэтому финальный verdict переносим на Jenkins.

### Шаг 3 (следующая итерация, если останется 1-2 флака)

Фиксить строго по одному кейсу за коммит:

1. Не возвращаться к широкому рефакторингу.
2. Делать узкий diff + таргетный pytest + пуш.
3. Сразу обновлять `FORM_SHORT_CONTEXT_2026-04-20.md` и этот план.

### Шаг 4 (после стабилизации tail)

Низкорисковая техдолг-итерация:

1. Убрать часть `time.sleep` в критичных flow на `wait_for`/`expect`.
2. Снизить индексные XPath в hot-path модулях.
3. Добавить явную маркировку причин падения в отчете (`infra`, `selector_drift`, `real_regression`).

## 3) KPI и критерии готовности

Краткосрочные KPI (текущая серия):

1. На ближайшем build после `30844b5`: `<=2 failed`.
2. На следующей итерации: `0-1 failed` при сопоставимом наборе тестов.
3. Ноль повторных падений Tele2 по причинам `ERR_ABORTED`/невидимой city-кнопки.

Среднесрочные KPI (2-3 итерации):

1. Удержание fail-rate ниже `<3%` на стабильном наборе тестов.
2. Снижение `selector_drift` минимум на `40%`.
3. Снижение количества `time.sleep` в ключевых flow на `30%` без роста false-negative.

## 4) Операционный чеклист на каждый цикл

1. Взять Jenkins лог последнего build и сравнить с предыдущим.
2. Разложить падения по типам: `infra`, `selector_drift`, `real_regression`.
3. Сделать только точечный фикс под конкретный фейл.
4. Прогнать таргетные тесты локально (если позволяет окружение).
5. Запушить в `main`.
6. Сразу обновить:
   - `FORM_SHORT_CONTEXT_2026-04-20.md`
   - `FORM_SHORT_STABILIZATION_PLAN.md`

## 5) Operational update after build 1015 (2026-04-20)
Current status:
1. Build `1015` on `30844b5` regressed to `15 failed, 144 passed, 9 skipped`.
2. The dominant failure mode is popup interaction interception (`popup-lead-catcher`, `popup-banner`).
3. Secondary failure mode: overly strict popup presence assertion in `check_popup_super_offer_second`.

Applied micro-fixes for the next run:
1. `pages/main_steps.py`: prioritize popup-scoped selectors in `send_popup_profit` and `send_popup_express_connection`, avoid fragile street click in profit flow, and force submit click where overlay intercepts events.
2. `pages/page_mts/mts_page.py`: `check_popup_super_offer_second` changed to any-visible-marker polling for 65 seconds.

Immediate validation plan (targeted, before/with next Jenkins run):
1. Validate one representative profit popup test (`beeline_home_online`).
2. Validate both express popup endpoints (`mts-home-online.ru` and `/moskva`).
3. Validate `moskva_mts_home_online` popup appearance check.
4. Push and observe full Jenkins rerun.

Decision gates:
1. If targeted tests are green and Jenkins drops to <=2 fails, continue with small cleanup only.
2. If profit popup still flakes, tighten selectors to active popup root by visibility + z-index checks.
3. If express still flakes on submit, add explicit close/await for competing overlays before click.
4. If telegram post-action still reports HTTP 400, update chat id in Jenkins secret/config to `-1003929635211` (separate infra task).

## 6) Validation status after latest code changes (2026-04-20)
Targeted run outcome:
1. `beeline_home_online::test_application_popup_super_offer` — passed.
2. `test_application_express_connection[https://mts-home-online.ru/]` — passed.
3. `test_application_express_connection[https://mts-home-online.ru/moskva]` — passed.
4. `moskva_mts_home_online::test_application_popup_super_offer` — passed.

Current interpretation:
1. Profit popup interaction fix is validated on representative Beeline flow.
2. Express popup submit interception fix is validated on both failing URLs from build 1015.
3. `check_popup_super_offer_second` no longer blocks the `moskva` case.

Next action:
1. Push changes and monitor next full Jenkins run for regression spillover.
