# """
# This module contains page classes for CGAA pages,
# which provide locators for interactions.
# """

from selenium.webdriver.common.by import By
import time


class LoginPage:
    URL = 'http://127.0.0.1:8080'
    time.sleep(5)
    BUTTON_LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')

    INPUT_EMAIL = (By.XPATH, '//input[@placeholder="Email"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@placeholder="Password"]')
    BUTTON_MASUK = (By.XPATH, '//button[normalize-space()="Masuk"]')

class AddMultipleChoicePage:
    MULTIPLE_CHOICE_MENU = (By.XPATH, '//p[normalize-space()="Tambah Pilihan Ganda"]')
    time.sleep(5)

    INPUT_PERTANYAAN = (By.XPATH, '//span[@id="cke_1_bottom"]' )
    # TINGKAT_SOAL = (By.XPATH, )
    # INPUT_A = (By.XPATH, )
    # INPUT_B = (By.XPATH, )
    # INPUT_C = (By.XPATH, )
    # INPUT_D = (By.XPATH, )
    # KUNCI_JAWABAN = (By.XPATH, )
    # INPUT_PENJELASAN = (By.XPATH, )
