import re

def sanitize_input(input_string):
    p = re.compile("[;'\"\\\\]")
    return p.sub('', input_string)

def is_email(input_string):
    p = re.compile("[\\w_\\-\\.]+@[\\w_\\-]+\\.[\w]+")
    return p.match(input_string) is not None
