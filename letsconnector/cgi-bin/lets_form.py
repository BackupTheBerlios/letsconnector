#!/usr/bin/python

# very simple exception type when there is an error in a form
class FormException(Exception):
    def __init__(self, f):
        Exception.__init__(self)
        self.field = f

class FormFieldNotPresent(FormException):
    def __init__(self, f):
        FormException.__init__(self, f)

class FormFieldWrongType(FormException):
    def __init__(self, f):
        FormException.__init__(self, f)

# raise this when an operation (eg. insert, query) is attempted on an
# inappropriate form
class FormBadOperation(Exception):
    def __init__(self):
        Exception.__init__(self)

# raise this when a query is submitted with no fields entered
class FormEmptyQuery(Exception):
    def __init__(self):
        Exception.__init__(self)

def text(form, field):
    """get a text field from the form, check present, check textyness"""
    val = form.getfirst(field)
    if(val == None):
        raise FormFieldNotPresent(field)
    elif(type(val) != type("")):
        raise FormFieldWrongType(field)
    else:
        return val

def numeric(form, field):
    """get a numeric field from the form
    todo: check numericness"""
    return gettext(form, field)

def email(form, field):
    """get an email field from the form
    todo: check emailness"""
    return gettext(form, field)

def date(form, field):
    """alas, I am yet a nop"""
    pass
    
