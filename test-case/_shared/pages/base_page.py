from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.support.expected_conditions import (
    invisibility_of_element_located,
    presence_of_all_elements_located,
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.current_timeout = 10
        self.wait = WebDriverWait(self.driver, self.current_timeout)

    def update_wait_timeout(self, timeout):
        self.current_timeout = timeout
        self.wait = WebDriverWait(self.driver, self.current_timeout)

    def wait_for_element(self, element_locator, timeout=30):
        return self.wait_for_elements(element_locator, timeout)[0]

    def wait_for_elements(self, element_locator, timeout=30):
        old_timeout = self.current_timeout
        self.update_wait_timeout(timeout)
        elements = self.wait.until(presence_of_all_elements_located(element_locator))
        self.update_wait_timeout(old_timeout)
        return elements

    def wait_for_element_to_disappear(self, element_locator, timeout=30):
        old_timeout = self.current_timeout
        self.update_wait_timeout(timeout)
        try:
            self.wait.until(invisibility_of_element_located(element_locator))
        except TimeoutException as e:
            raise TimeoutException(
                "The element is still displayed after {} s".format(self.current_timeout)
            ) from e
        self.update_wait_timeout(old_timeout)

    def wait_for_page_to_load_with_element(self, element_locator=None):
        if element_locator:
            self.wait_for_elements(element_locator)
        page_state = self.driver.execute_script("return document.readyState;")
        return page_state == "complete"
