class DataCourier:

    CREATE_ERROR_MESSAGE_DUPLICATE_LOGIN = "Этот логин уже используется"
    CREATE_ERROR_MESSAGE_MISSING_FIELDS = "Недостаточно данных для создания учетной записи"
    LOGIN_ERROR_MESSAGE_ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    LOGIN_ERROR_MESSAGE_MISSING_DATA = "Недостаточно данных для входа"
    DELETE_ERROR_MESSAGE_MISSING_ID = "Недостаточно данных для удаления курьера"
    DELETE_ERROR_MESSAGE_INVALID_ID = "Курьера с таким id нет"

    WRONG_PASSWORD_VALUE = "wrong_password_999"
    WRONG_LOGIN_VALUE = "wrong_courier_100"
    INVALID_LOGIN = "fake_courier_100999"
    INVALID_PASSWORD = "fake_password55"
    INVALID_ID = 9999999


class DataOrder:
    ACCEPT_ERROR_MESSAGE_COURIER_NOT_FOUND = "Курьера с таким id не существует"
    ACCEPT_ERROR_MESSAGE_ORDER_NOT_FOUND = "Заказа с таким id не существует"
    ACCEPT_ERROR_MESSAGE_NO_ID = "Недостаточно данных для поиска"
    ORDER_BY_NUMBER_ERROR_MESSAGE_NO_TRACK = "Недостаточно данных для поиска"
    ORDER_BY_NUMBER_ERROR_MESSAGE_INVALID_TRACK = "Заказ не найден"
    ORDER_BY_NUMBER_INVALID_TRACK = 00000
    INVALID_CID = 999999
    INVALID_ORDER_ID = 999999
    