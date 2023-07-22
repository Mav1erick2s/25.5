import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class', autouse=True)
def driver(request):
    # Используем в качестве драйвера GooglChrome
    driver = webdriver.Chrome(r'c:\\chromedriver.exe')
    driver.implicitly_wait(10)
    # Определяем размер окна для работы
    driver.set_window_size(1000, 800)
    # Присваиваем к переменной класса переменную фикстуры
    request.cls.driver = driver

    yield

    driver.quit() #Закрываем весь драйвер

class TestUI:
    def test_tab_phone_positive_001(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Проверяем, что мы оказались на странице авторизации по мобильному телефону
        assert self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]').text == "Мобильный телефон"

    def test_tab_emile_positive_003(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Почта"
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        # Проверяем, что мы оказались на странице авторизации по электронной почте
        assert self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]').text == "Электронная почта"

    def test_tab_login_positive_005(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Логин"
        self.driver.find_element(By.ID, 't-btn-tab-login').click()
        # Проверяем, что мы оказались на странице авторизации по логину
        assert self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]').text == "Логин"

    def test_tab_personal_account_positive_008(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Лицевой счет"
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        # Проверяем, что мы оказались на странице авторизации по лицевому счету
        assert self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]').text == "Лицевой счёт"

    def test_registration_link_positive_011(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим по ссылке "Зарегистрироваться"
        self.driver.find_element(By.ID, 'kc-register').click()
        # Проверяем, что мы оказались на странице регистрации пользователя
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"

    def test_input_field_email_positive_004(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Почта"
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        # Вводим email
        self.driver.find_element(By.ID, 'username').send_keys('komoltsevaa1703@gmail.com')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.ID, 'kc-login').click()
        # Проверяем, что авторизация прошла успешно
        assert self.driver.find_element(By.CSS_SELECTOR, 'h3[class="card-title"]').text == "Учетные данные"
        # Выходим из личного кабинета
        self.driver.find_element(By.ID, 'logout-btn').click()

    def test_input_filed_password_positive_009(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку "Мобильный телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Вводим мобильный телефон
        self.driver.find_element(By.ID, 'username').send_keys('89507958198')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Проверяем, что авторизация прошла успешно
        assert self.driver.find_element(By.CSS_SELECTOR, 'h3[class="card-title"]').text == "Учетные данные"
        # Выходим из личного кабинета
        self.driver.find_element(By.ID, 'logout-btn').click()

    def test_password_restoration_positive_012(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Нажимаем на ссылку "Забыл пароль"
        self.driver.find_element(By.ID, 'forgot_password').click()
        # Проверяем, что оказались на странице восстановления пароля
        assert self.driver.find_element(By.CSS_SELECTOR, 'h1[class="card-container__title"]').text == "Восстановление пароля"

    def test_back_button_positive_014(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Нажимаем на ссылку "Забыл пароль"
        self.driver.find_element(By.ID, 'forgot_password').click()
        # Нажимаем на ссылку "Вернуться назад"
        self.driver.find_element(By.ID, 'reset-back').click()
        # Проверяем, что оказались на странице авторизации
        assert self.driver.find_element(By.CSS_SELECTOR, 'h1[class="card-container__title"]').text == "Авторизация"

    def test_link_user_agreement_positive_015(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Нажимаем на ссылку "пользовательское соглашение"
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="rt-link rt-link--orange"]').click()
        # Открываем новое окно по из ссылки
        tab_from_link = self.driver.window_handles[1]
        self.driver.switch_to_window(tab_from_link)
        # Проверяем, что оказались на странице с информацией для пользователя
        assert self.driver.find_element(By.XPATH, '//*[@id="title"]/h1[1]').text == \
               "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"

    def test_registration_positive_010(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим на страницу "Зарегистрироваться"
        self.driver.find_element(By.ID, 'kc-register').click()
        # Проверяем, что мы оказались на странице регистрации
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
        # Вводим данные в поле "Имя"
        self.driver.find_element(By.NAME, 'firstName').send_keys('Анастасия')
        # Вводим данные в поле "Фамилия"
        self.driver.find_element(By.NAME, 'lastName').send_keys('Бунькова')
        # Вводим данные в поле "E-mail или мобильный телефон"
        self.driver.find_element(By.ID, 'address').send_keys('bunkovana@gmail.com')
        # Вводим данные в поле "Пароль"
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('karamelkinnapriemE1')
        # Вводим данные в поле "Подтвержение пароля"
        self.driver.find_element(By.ID, 'password-confirm').send_keys('karamelkinnapriemE1')
        # Нажимаем на кнопку "Зарегистрироваться"
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn"]').click()
        # Проверяем, что все данные успешно заполнены и пользователь перешел к подтвержению E-mail или телефона
        assert self.driver.find_element(By.CSS_SELECTOR, 'h1[class="card-container__title"]').text == "Подтверждение email"

    def test_link_VK_016(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим по ссылке "ВКонтакте"
        self.driver.find_element(By.ID, 'oidc_vk').click()
        # Проверяем, что оказались на странице авторизации через "ВК"
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        'h1[class="vkc__VKDisplayTitle__title vkc__VKDisplayTitle__demiboldWeight vkc__VKDisplayTitle__titleLevel2"]')

    def test_link_OK_017(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим по ссылке "ОК"
        self.driver.find_element(By.ID, 'oidc_ok').click()
        # Проверяем, что оказались на странице авторизации через "Одноклассники"
        assert self.driver.find_element(By.CSS_SELECTOR, 'div[class="ext-widget_h_tx"]').text == "Одноклассники"


                                                  ### Negative tests ###
    def test_input_filed_personal_account_negative_012(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Лицевой счет"
        self.driver.find_element(By.ID, 't-btn-tab-ls').click()
        # Вводим данные в поле "Лицевой счет"
        self.driver.find_element(By.ID, 'username').send_keys('111111111111')
        # Вводим данные в поле "Пароль"
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Войти"
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке
        assert self.driver.find_element(By.ID, 'form-error-message')

    def test_input_filed_login_negative_005(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Логин"
        self.driver.find_element(By.ID, 't-btn-tab-login').click()
        # Вводим данные в поле "Логин"
        self.driver.find_element(By.ID, 'username').send_keys('1?р$68aghdjv')
        # Вводим данные в поле "Пароль"
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Войти"
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке
        assert self.driver.find_element(By.ID, 'form-error-message')

    def test_input_field_mobile_phone_negative_013(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку "Мобильный телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Вводим спецсимволы в поле "Телефон"
        self.driver.find_element(By.ID, 'username').send_keys('Aa!@#$%^&*()-_+=`~/\,.?><|b / PaSSword!@#$%^&*()-_+=`~/\,.?><|')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке, мы находимся на странице авторизации по номеру телефона
        assert self.driver.find_element(By.ID, 'form-error-message') and \
               self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input__placeholder"]').text == "Мобильный телефон"
        # ---Баг-репорт NN-002---

    def test_input_field_mobile_phone_negative_014(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку "Телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Вводим кириллицу в поле "Телефон"
        self.driver.find_element(By.ID, 'username').send_keys('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке, мы находимся на странице авторизации по номеру телефона
        assert self.driver.find_element(By.ID, 'form-error-message') and \
               self.driver.find_element(By.CSS_SELECTOR,
                                        'span[class="rt-input__placeholder"]').text == "Мобильный телефон"
        # ---Баг-репорт NN-003---

    def test_input_field_email_negative_009(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку "Почта"
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        # Вводим кириллицу в поле "Электронная почта"
        self.driver.find_element(By.ID, 'username').send_keys('Aa!@#$%^&*()-_+=`~/\,.?><|b / PaSSword!@#$%^&*()-_+=`~/\,.?><|')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке, мы находимся на странице авторизации по номеру телефона
        assert self.driver.find_element(By.ID, 'form-error-message') and \
               self.driver.find_element(By.CSS_SELECTOR,
                                        'div[class="rt-tab rt-tab--small rt-tab--active"]').text == "Почта"
        # ---Баг-репорт NN-004---

    def test_input_field_mobile_phone_negative_001(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку "Телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Вводим кириллицу в поле "Телефон"
        self.driver.find_element(By.ID, 'username')\
            .send_keys('umtalosftgmvxbdgtpmgxkvrcjmvjooqudvhclfsocgugutaisloxzrmnkgdkzllqufpssjcayjlglsgdbgcwewpvedaivdgxrcgcmqwripxnabuvskudqtcbizaixbjbmjxuijxnmkaxzvmfbpbrslovmrxonsjwxaqupaebnchxplltszoebnzlvncfhuzhbngwbcqkftfygiygxooiozfdedbsotrhlpmwcvdhtgftnzngfziiszxmxlwijou')
        # Вводим пароль
        self.driver.find_element(By.ID, 'password').send_keys('karamelkinnapriemE2')
        # Нажимаем на кнопку "Вход"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке, мы находимся на странице авторизации по номеру телефона
        assert self.driver.find_element(By.ID, 'form-error-message') and \
               self.driver.find_element(By.CSS_SELECTOR,
                                        'span[class="rt-input__placeholder"]').text == "Мобильный телефон"
        # ---Баг-репорт NN-001---

    def test_input_filed_password_negative_003(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Телефон"
        self.driver.find_element(By.ID, 't-btn-tab-phone').click()
        # Вводим данные в поле "Мобильный телефон"
        self.driver.find_element(By.ID, 'username').send_keys('89507958198')
        # Вводим данные в поле "Пароль"
        self.driver.find_element(By.ID, 'password').send_keys('hauisb@4389')
        # Нажимаем на кнопку "Войти"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке
        assert self.driver.find_element(By.ID, 'form-error-message')

    def test_input_filed_email_negative_004(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Переходим во вкладку по табу "Почта"
        self.driver.find_element(By.ID, 't-btn-tab-mail').click()
        # Вводим данные в поле "Электронная почта"
        self.driver.find_element(By.ID, 'username').send_keys('')
        # Вводим данные в поле "Пароль"
        self.driver.find_element(By.ID, 'password').send_keys('')
        # Нажимаем на кнопку "Войти"
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded login-form__login-btn"]').click()
        # Ожидаем, что авторизация не удалась и получено сообщение об ошибке
        assert self.driver.find_element(By.ID, 'form-error-message') and \
               self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input-container__meta rt-input-container__meta--error"]')
        # ---Баг-репорт NN-005---

    def test_input_name_negative_015(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Нажимаем на ссылку "Зарегистрироваться"
        self.driver.find_element(By.ID, 'kc-register').click()
        # Вводим данные в поле "Имя"
        self.driver.find_element(By.NAME, 'firstName') \
            .send_keys('92842957653842938573')
        # Переходим к заполнению поля "Фамилия"
        self.driver.find_element(By.NAME, 'lastName').send_keys('Бунькова')
        # Ожидаем, что страница отображает сообщение об ошибке(некорректном заполнении поля "Имя")
        assert self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

    def test_input_name_negative_011(self):
        # Переходим на страницу авторизации
        self.driver.get("https://b2c.passport.rt.ru")
        # Нажимаем на ссылку "Зарегистрироваться"
        self.driver.find_element(By.ID, 'kc-register').click()
        # Вводим данные в поле "Имя"
        self.driver.find_element(By.NAME, 'firstName')\
            .send_keys('т')
        # Переходим к заполнению поля "Фамилия"
        self.driver.find_element(By.NAME, 'lastName').send_keys('Бунькова')
        # Ожидаем, что страница отображает сообщение об ошибке(некорректном заполнении поля "Имя")
        assert self.driver.find_element(By.CSS_SELECTOR, 'span[class="rt-input-container__meta rt-input-container__meta--error"]')\
                   .text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."




