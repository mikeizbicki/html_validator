#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags
    # without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags
    new_tags_list = _extract_tags(html)
    stack = []
    for tag in new_tags_list:
        if tag.startswith("<") and not tag.startswith("</"):
            stack.append(tag[1:-1])
        elif tag.startswith("</"):
            if not stack:
                return False
            if tag[2:-1] != stack[-1]:
                return False
            stack.pop()
    return not stack


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used
    directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input
    string,stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    in_tags_list = []
    working_tag = ''
    in_tag = False
    for t in html:
        if t == '<':
            in_tag = True
        elif t == '>':
            in_tag = False
            working_tag += t
            in_tags_list.append(working_tag)
            working_tag = ''
        elif in_tag:
            working_tag += t

    return in_tags_list


output1 = validate_html('<strong>example</strong>')
print("output1=", output1)
output2 = validate_html('<strong>example')
print("output2=", output2)
output3 = _extract_tags('Python <strong>rocks</strong>!')
print("output3=", output3)
