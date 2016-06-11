from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
# explicit import is better.
from utils import *


# start controller functions

def go_to(driver, user, kwargs):
    browser_go_to(driver, kwargs, '/login')

def confirm_title(driver, user, kwargs):
     assert_title(driver, kwargs['title'])

def login(driver, user, kwargs):
    browser_go_to(driver, kwargs, '/login')
    #username_input(driver, 'id_username', user)
    #password_input(driver, 'id_password', user)
    # done with filling out form
    #click_on_id_and_wait_on(driver, 'btn-login', 'id_next_page')
    # have to stay on the page to complete login


def logout(driver, user, kwargs):
    # logout does not yet have a id added it.
    driver.get(join_url(kwargs['root'], 'mailbox'))
    browser_go_to(driver, kwargs, '/logout')
    click_on_id(driver, 'id_logout')


def confirm_welcome_mail(driver, user, kwargs):
    driver.get(join_url(kwargs['root'], 'mailbox'))
    elem = driver.find_element_by_id('list')
    print(elem.get_attribute('innerHTML'))
    # should assert a email
    # a general function to view email subject in mailbox


def register(driver, user, kwargs):
    driver.get(kwargs['root'])
    # button to register on frontpage doesn't contain a id
    # temp workaround with get.
    driver.get(join_url(kwargs['root'], 'order', 'account'))

    # A page with the question if want to purchase or already have a code.
    click_on_id(driver, 'btn-purchase')

    username_input(driver, 'field-email', user)

    click_on_id(driver, 'process-btn')
    # Now we have to pay.
    click_on_id(driver, 'field-country-confirm')
    click_on_id(driver, 'field-terms-agree')
    click_on_id(driver, 'process-btn')
    # payment is mocked. going back
    backwards(driver)
    time.sleep(5)

    # create account
    click_on_id(driver, 'btn-create-new')

    clear_field(driver, 'field-email')
    email_input(driver, 'field-email', user)
    password_input(driver, 'field-password', user)
    password_input(driver, 'field-confirm-password', user)
    time.sleep(5)
    click_on_id(driver, 'btn-register')


def send_email_to_myself(driver, user, kwargs):
    driver.get(join_url(kwargs['root'], 'mailbox'))
    click_on_id(driver, 'btn-compose')

    email_address = user.username
    input_text_to_id(driver,
                    'field-send-to',
                     email_address)

    input_text_to_id(driver,
                    'field-subject',
                    'hai this is email')

    click_on_id(driver, 'btn-compose-send')


def register_trial(driver, user, kwargs):
    driver.get(join_url(kwargs['root'], 'signup', 'trial'))
    username_input(driver, 'field-email', user)
    password_input(driver, 'field-password', user)
    password_input(driver, 'field-confirm-password', user)
    click_on_id(driver, 'field-terms-agree')
    click_on_id(driver, 'btn-register')
    time.sleep(20)
    trial_email_address = html_of_elem(driver, 'link_to_mailbox')
    time.sleep(5)
    user.trial_email = trial_email_address
    time.sleep(5)
    click_on_id(driver, 'upgrade-complete-btn')
    time.sleep(5)


def login_trial(driver, user, kwargs):
    driver.get(join_url(kwargs['root'], 'login'))
    email_input(driver, 'field-login_username', user, trial=True)
    password_input(driver, 'field-login_password', user)
    # done with filling out form
    click_on_id(driver, 'btn-login')
    # have to stay on the page to complete login
    time.sleep(10)

def change_username_to_uppercase(driver, user, kwargs):
    username = user.username[:user.username.find('@')].upper()
    domain = user.username[user.username.find('@')+1:]

    user.username = username + domain


def assert_false(driver, user, kwargs):
    assert_(1 == 2, 'one is not two')

