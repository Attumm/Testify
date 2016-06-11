import time, importlib

from selenium import webdriver

from settings import user_count, dry_run, user_stories
from settings import username, password, controllers

from users import User
from utils import AssertFail


def start_webdriver(user):
    #TODO should use the browser of the user to init webdriver
    return webdriver.Firefox()


def run_test(controller, stories, user_config, root_url, dry_run=False):
    kwargs = {'root': root_url}
    user = User(**user_config)
    for name_story, story in stories:

        driver = start_webdriver(user)
        user_story_fails = 0
        # log name of story
        print "story {}".format(name_story)
        for i, args in enumerate(story, 1):
            # args == (step, argumensts)
            step = args[0]
            kwargs.update(args[1])

            # log step in the story
            print " {0}. step {1}".format(i, step)

            if not dry_run:
                try:
                    getattr(controller, step)(driver, user, kwargs)

                except AssertFail as e:
                    user_story_fails += 1
                    print('assert failed')
                    print(e)

                except KeyboardInterrupt:
                    print "interactive mode\nto stop ctrl+c"
                    while True:
                        try:
                            print eval(raw_input('>>> '))
                        except (NameError, SyntaxError) as e:
                            print e
                        except KeyboardInterrupt:
                            break

                except Exception as e:
                    # log error with name of the step.
                    err_msg = "with user {0} in {1} of {2} failed with\
                            error message:\n{3}"
                    err_msg = err_msg.format(user.username, step, name_story ,e)
                    print(err_msg)
        # done with test. Close the browser.
        driver.close()


users_config = [{
    'username': username.format(i),
    'email': username.format(i) + '@gmail.com',
    'password': password.format(i),
    'browser': None}
            for i in range(1, user_count+1)]


if __name__ == '__main__':

    for name_controller, root_url in controllers:
        controller = importlib.import_module('controllers.' + name_controller)

        for name_file in user_stories:
            user_storie = importlib.import_module('user_stories.' + name_file)

            for user_config in users_config:
                run_test(controller, user_storie.stories, user_config, root_url, dry_run)

