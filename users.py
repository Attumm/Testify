class User(object):
    def __init__(self, username, password, browser='firefox'):
        self.username = username
        self.password = password
        self.browser = browser
        self.email = '{}@gmail.com'.format(username)
