# QA‑портфолио: проекты по тестированию (веб, мобайл, API)

Это портфолио с проектами по ручному тестированию и автотестированию. 

## О навыках и подходе

В проектах я применяю системный подход QA: декомпозирую требования, выявляю «серые зоны»,
покрываю сценарии техниками тест‑дизайна (классы эквивалентности, граничные значения, таблицы принятия решений) и фиксирую дефекты с воспроизводимыми шагами.

**Стек и инструменты:**
- **Ручное тестирование:** чек‑листы, тест‑кейсы, баг‑репорты, исследовательское тестирование.
- **API:** Postman, Swagger, валидация JSON, SQL‑запросы.
- **Веб:** DevTools, кроссбраузерность, проверка адаптивности, Allure (для автотестов).
- **Мобайл:** Android Studio (эмуляторы), Charles (анализ трафика), нативные сценарии (push, офлайн, миграция).
- **Автотесты:** pytest, параметризация, фикстуры, Page Object (BasePage), Selenium, WebDriverWait.

## Проекты в репозитории

### Яндекс Маршруты (веб)
**Что тестировала:** функциональное и кроссбраузерное тестирование (Яндекс Браузер, Firefox). Ключевые сценарии: валидация полей, расчёт стоимости, 
логика окон оплаты, кнопка «Забронировать».  
**Особенности:** сверка с макетами в Figma, применение техник тест‑дизайна, подготовка документации.  
**Польза:** снижение рисков некорректной работы критически важных сценариев.

### Яндекс Метро (мобильное приложение)
**Что тестировала:** функциональное и регрессионное тестирование после рефакторинга. Сценарии: маршрутизация, интерактивная схема, выбор станций, 
нативные функции (push‑уведомления, офлайн‑режим, ориентация экрана, миграция данных при обновлении).  
**Особенности:** тестирование на эмуляторе Android Studio, выявление серых зон в требованиях.  
**Польза:** подтверждена стабильность приложения после рефакторинга; подготовлена отчётность для релиза в стор.

### Яндекс.Прилавок (API)
**Что тестировала:** API‑методы (GET, POST, PUT, DELETE), валидные/невалидные сценарии, граничные значения, коды ответов, структура JSON.  
**Особенности:** кросс‑проверка данных через SQL‑запросы (соответствие БД и ответов API), изучение Swagger‑документации.  
**Польза:** выявлена рассинхронизация данных и ошибки валидации; подтверждена целостность информации.

### Яндекс Самокат (веб, мобайл, API — сквозные сценарии)
**Что тестировала:** UI веб‑версии (бронирование, экран «Статус заказа», адаптивность), действия курьера в мобильном приложении, API‑создание заказов.  
**Особенности:** end‑to‑end сценарии при ограниченной тестовой среде: заказ создаётся через API, действия курьера — через мобайл‑приложение, 
финальная валидация — в веб‑UI. Использован Charles для анализа трафика и DevTools для отладки.  
**Польза:** выявлены расхождения статусов и задержки обновления UI; сценарии спроектированы атомарно для дальнейшей автоматизации.

## Структура репозитория
jelisejenkova88-jpg/Practicum_projects}/
├── README.md
├── manual-testing-yandex-marshruty/
│   ├── README.md
│   ├── manual-testing-yandex-marshruty(1).xlsx
│   └── manual-testing-yandex-marshruty.xlsx
├── manual_testing_yandex_metro/
│   ├── README.md
│   ├── Screenshots.xlsx
│   └── manual_testing_yandex_metro.xlsx
├── manual_testing_yandex_prilavok_API/
│   ├── README.md
│   └── manual_testing_yandex_prilavok_API.xlsx
├── manual_testing_yandex_scooter/
│   ├── README.md
│   └── manual_testing_yandex_scooter.xlsx
├── stellar_burgers_API/
│   ├── api_methods/
│   │   ├── __init__.py
│   │   └── methods.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_order_create.py
│   │   ├── test_user_create.py
│   │   └── test_user_login.py
│   ├── README.md
│   ├── conftest.py
│   ├── data.py
│   ├── generators.py
│   ├── requirements.txt
│   └── url.py
├── stellar_burgers_UI/
│   ├── locators/
│   │   ├── __init__.py
│   │   ├── constructor_locators.py
│   │   ├── login_locators.py
│   │   └── order_list_locators.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── constructor_page.py
│   │   └── order_list_page.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_constructor_page.py
│   │   └── test_order_list.py
│   ├── README.md
│   ├── conftest.py
│   ├── requirements.txt
│   └── url.py
├── stellar_burgers_unit/
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_burger.py
│   ├── README.md
│   ├── conftest.py
│   └── requirements.txt
├── yandex_scooter_API/
│   ├── api_methods/
│   │   ├── __init__.py
│   │   ├── courier_methods.py
│   │   └── order_methods.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_accept_order.py
│   │   ├── test_courier_creation.py
│   │   ├── test_courier_delete.py
│   │   ├── test_courier_login.py
│   │   ├── test_list_of_orders.py
│   │   ├── test_order_by_track.py
│   │   └── test_order_creation.py
│   ├── README.md
│   ├── conftest.py
│   ├── data.py
│   ├── generators.py
│   ├── requirements.txt
│   └── url.py
├── yandex_scooter_UI/
│   ├── locators/
│   │   ├── __init__.py
│   │   ├── faq_locators.py
│   │   ├── main_locators.py
│   │   └── order_locators.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── faq_page.py
│   │   └── order_page.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_faq_page.py
│   │   └── test_order_page.py
│   ├── README.md
│   ├── conftest.py
│   ├── requirements.txt
│   └── url.py
