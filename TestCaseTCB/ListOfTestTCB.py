import time
import pytest

from selenium import webdriver


def first_test():
    # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
    driver = webdriver.Chrome()

    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
    time.sleep(5)

    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    driver.get("https://vk.com/")
    time.sleep(5)


if __name__ == "__main__":
    first_test()
