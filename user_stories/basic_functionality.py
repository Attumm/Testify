"""
Explain why and who this works. What is stories.
"""

stories = (
    'Login and confirm detail page', [
        ('go_to', {'page': 'index'}),
        ('login', {}),
        ('confirm_title', {'title': 'ID Vault'}),
    ],
)

# set the parser/formatter in the config and runner.
def format_(stories):
    """(str, [str, dict], str, [str, dic], ...) -> [(str, [str, dict]), ...]
    Takes item 1 and 2 and adds them in a tuple.
    """
    if len(stories) % 2 != 0:
        raise Exception('stories variable had syntax/format errors')
    return [(stories[i], stories[i+1]) for i in range(0, len(stories)-1, 2)]

stories = format_(stories)


