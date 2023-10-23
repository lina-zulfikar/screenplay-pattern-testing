# """
# This module contains web UI interactions for DuckDuckGo.
# """

from screenplay.pattern import Actor, Task, Question
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from testlib.pages import LoginPage, AddMultipleChoicePage

# Questions
class IsElementVisible(Question[str]):
    def __init__(self, element):
        self.element = element

    def of(element):
        return IsElementVisible(element)

    def answered_by(self, actor):
        try:
            return self.element.is_displayed()
        except:
            return False 
        

# Tasks

class Load(Task):
    def __init__(self, url: str) -> None:
        self.url = url

    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.get(self.url) 

class LogInCgaa(Task):
    # def __init__(self, phrase: str) -> None:
    #     self.phrase = phrase
    
    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.find_element(*LoginPage.BUTTON_LOGIN).click()
        browser.find_element(*LoginPage.INPUT_EMAIL).send_keys('linazulfikar99@mail.ugm.ac.id')
        browser.find_element(*LoginPage.INPUT_PASSWORD).send_keys('testingAutomation')
        browser.find_element(*LoginPage.BUTTON_MASUK).click()

        
class AddMultipleChoice(Task):
    def perform_as(self, actor: Actor) -> None:
        browser: WebDriver = actor.using('browser')
        browser.find_element(*AddMultipleChoicePage.MULTIPLE_CHOICE_MENU).click()    
        browser.find_element(*AddMultipleChoicePage.INPUT_PERTANYAAN).send_keys('Ini testing screenplay')
