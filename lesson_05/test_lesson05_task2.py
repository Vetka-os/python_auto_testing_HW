from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Найдите поле ввода с названием custname.
    user_name = driver.find_element(By.NAME, "custname")

    # Введите в него ваше имя.
    user_name.send_keys("Ольга")

    # Найдите кнопку Submit и нажмите на нее.
    button_submit = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button_submit.click()

    # Проверьте, что после нажатия URL изменился.
    assert "/post" in driver.current_url

    driver.quit()
