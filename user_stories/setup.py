"""
Place the use cases to start testing in this file.
When using persistent users, It won't be necessary to add them again.
"""

stories = (
    'register user', [
        ('register', {}),
        ('confirm_registered', {})
        ('logout', {}),
    ],
)

def format_(stories):
    """(str, [str, dict], str, [str, dic], ...) -> [(str, [str, dict]), ...]
    Takes item 1 and 2 and adds them in a tuple.
    """
    if len(stories) % 2 != 0:
        raise Exception('stories variable had syntax/format errors')
    return [(stories[i], stories[i+1]) for i in range(0, len(stories)-1, 2)]

stories = format_(stories)