"""
Explain the settings
"""

import uuid

# tuple with name of controller and url to run the use cases on.
controllers = [
        #('production', 'https://example.com'),
        #('dev_old_frontend', 'https://dev.example.com'),
        #('dev_old_frontend', 'https://accept.example.com'),
        ]

user_stories = (
        'setup',
        'basic_functionality',
        'teardown',
)

pre_run_scripts = (
        #'setup_db',
)

post_run_scripts = (
        #'remove_data_db',
)

dry_run = True

temp_user = True

user_count = 3
random_str = str(uuid.uuid4())[:5]

username = 'selenium_test{0}@gmail.com'.format(random_str)
password = '!@123SEkret{0}'

