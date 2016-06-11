import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import StaleElementReferenceException


def _assert(result, msg=''):
    """Gets a boolean if false,
    Throws a exception that will be handled by the runner.
    """
    if not result:
        raise AssertFail(msg)


def assert_with_picture(result, msg=''):
    """Gets a boolean if false,
    Throws a exception that will be handled by the runner.
    makes a picture of the browser screen.
    """
    if not result:
        # saving images and logs in a central place is better.
        driver.save_screenshot(time.ctime())
        raise AssertFail(msg)

def assert_title(driver, excpected):
    _assert(driver.title == expected)

def backwards(driver):
    """Goes back one page.
    Selenium sometimes fails to go backwards.
    As a hack we use javascript to go back one page.
    Selenium source code has lot of code calling js.
    """
    driver.execute_script("window.history.go(-1)")
    
    
def accept_alert_message(driver):
    Alert(driver).accept()
    
def dismiss_alert_message(driver):
    Alert(driver).dismiss()


def username_input(driver, id_, user):
    # could add if isintance to check if user is a str or user_class
    username_field = driver.find_element_by_id(id_)
    email_field.send_keys(user.username)


def email_input(driver, id_, user):
    # could add if isintance to check if user is a str or user_class
    email_field = driver.find_element_by_id(id_)
    email_field.send_keys(user.email)


def password_input(driver, id_, user):
    # could add if isintance to check if user is a str or user_class
    password_field = driver.find_element_by_id(id_)
    password_field.send_keys(user.password)


def clear_field(driver, id_):
    """Clear the field."""
    elem = driver.find_element_by_id(id_)
    elem.clear()


def join_url(*args):
    return '/'.join(s.strip('/') for s in args)

def browser_go_to(driver, kwargs, url):
    driver.get(join_url(kwargs['root'], url))


def wait_until_id(driver, id_, sec=10):
    """waits until a id is present."""
    # When there are 
    nav-access

def wait_until_url(driver, id_sec=10):
    """waits until browser is on an url"""
    pass
    

def click_on_id(driver, id_):
    element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, id_)))
    element.click()


def click_on_id_and_wait_on_id(driver, click_id, wait_id):
    pass


def click_on_id_try(driver, id_, tries=3):
    """Tries to click on a element"""
    # There are times when a element isn't clicked.
    pass


def input_text_to_id(driver, id_, text):
    elem = driver.find_element_by_id(id_)
    elem.send_keys(text)


def js_click_on_id(driver, id_):
    """Forces a click with js"""
    js_click = "document.getElementById('{}').click();".format(id_)
    driver.execute_script(js_click)


def scroll_to_bottom(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def html_of_elem(driver, id_):
    return driver.find_element_by_id(id_).get_attribute('innerHTML')


class AssertFail(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )
    
def click_on_id_wait_on_new_page(driver, id_):
    link = driver.find_element_by_id(id_)
    link.click()

    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            link.find_elements_by_id('doesnt-matter') 
            return False
        except StaleElementReferenceException:
            return True

    wait_for(link_has_gone_stale)
    
    
def click_on_a_href_wait_on_new_page(driver, text):
    link = driver.find_element_by_link_text(text)
    link.click()

    def link_has_gone_stale():
        try:
            # poll the link with an arbitrary call
            link.find_elements_by_id('doesnt-matter') 
            return False
        except StaleElementReferenceException:
            return True

    wait_for(link_has_gone_stale)
    
