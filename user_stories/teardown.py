"""
Place the use cases to end the test in this file.
When using persistent users, It won't be necessary to remove them after each test.
"""

stories = (
    'delete user', [
        ('delete user', {}),
        ('confirm deleted', {}),
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