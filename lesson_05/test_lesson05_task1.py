from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Откройте страницу https://httpbin.qa-territory.online.
    driver.get("https://httpbin.qa-territory.online/")

    # Сохраняю исходный URL для сравнения
    start_url = driver.current_url

    # Найдите и кликните на ссылку HTML Form.
    link_html = driver.find_element(By.LINK_TEXT, "HTML Form")
    link_html.click()

    # Проверьте, что URL изменился на /forms/post.
    assert "/forms/post" in driver.current_url

    # Вернитесь назад на главную страницу.
    driver.back()

    # Проверьте, что вернулись на исходный URL.
    assert driver.current_url == start_url

    driver.quit()
