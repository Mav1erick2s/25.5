import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope='class', autouse=True)
def driver(request):
    driver = webdriver.Chrome(r'c:\\chromedriver.exe')
    driver.implicitly_wait(10)
    driver.set_window_size(2000, 2000)
    request.cls.driver = driver

    yield

    #driver.quit()

class TestUI:
    def test_show_all_pets(self):
        # Переходим на страницу авторизации
        self.driver.get('https://petfriends.skillfactory.ru/login')
        # Вводим email
        self.driver.find_element(By.ID, 'email').send_keys('komoltsevaa1703@gmail.com')
        # Вводим пароль
        self.driver.find_element(By.ID, 'pass').send_keys('karamelkinnaprieme')
        # Нажимаем на кнопку входа в аккаунт
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.driver.find_element(By.CSS_SELECTOR, 'span[id="form-error-message",data-error="Неверный логин или пароль"]').click()
        # Проверяем, что мы оказались на главной странице пользователя
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    def test_number_of_pets(self):
        # Переходим во вкладку "Мои питомцы"
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))
        allStat = self.driver.find_element(By.XPATH, '//div[@class =".col-sm-4 left"]').text.split('\n')
        statPets = allStat[1].split(':')
        cards = self.driver.find_element(By.CSS_SELECTOR, 'tbody').text.split('\n')
        assert int(len(cards)/2) == int(statPets[1].strip())
        # Выходим в главное меню
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]').click()

    def test_check_photo(self):
        # Переходим во вкладку "Мои питомцы"
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "all_my_pets")))
        # переменные:
        images = self.driver.find_elements(By.CSS_SELECTOR, 'tbody > tr > th > img')
        pets = self.driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')

        assert int(len(images)) >= int(len(pets))/2
        # Выходим в главное меню
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]').click()

    def test_my_pets(self):
        # Переходим во вкладку "Мои питомцы"
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]').click()

        names = self.driver.find_elements(By.XPATH, '// *[ @ id = "all_my_pets"] / table / tbody / tr / td[1]')
        breed = self.driver.find_elements(By.XPATH, '// *[ @ id = "all_my_pets"] / table / tbody / tr / td[2]')
        age = self.driver.find_elements(By.XPATH, '// *[ @ id = "all_my_pets"] / table / tbody / tr / td[3]')
        uniqueNames = []
        duplicates = []

        for i in range(len(names)):
            namesI = names[i].text
            assert names[i].text != ''
            assert breed[i].text != ''
            assert age[i].text != ''

            if namesI not in uniqueNames:
                uniqueNames.append(namesI)
            else:
                duplicates.append(namesI)

        assert duplicates == []
        print(duplicates)

        # Выходим в главное меню
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]').click()
