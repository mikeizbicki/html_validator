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
    # use the _extract_tags function below to generate a
    # list of html tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class
    # will be that you will have to keep track of not
    # just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    ls = []
    # created empty stack/list
    balanced = True
    # Defining Boolean Logic for Problem

    for i in _extract_tags(html):
        if '/' not in i:
            ls.append(i)
        else:
            if ls == []:
                balanced = False
    # This for loop creates use helper function to look for
    # tags with no / to improve functionality
            else:
                a = ls.pop()
                if a[2:] not in i[1:]:
                    balanced = False
    if balanced and ls == []:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not
    meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    for i in range(len(html)):
        tag = ''
        ls = html[i]
        if ls == '<':
            if '>' not in html:
                return html
            else:
                while ls != '>':
                    tag += ls
                    i += 1
                    ls = html[i]
                tag += '>'
                tags.append(tag)
    return tags
