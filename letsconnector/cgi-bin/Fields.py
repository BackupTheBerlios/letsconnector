# Module file, not run as script.
# contains base class and subclasses for form fields.

import datetime

class TextField:
    def __init__(self, description, name, characters, max_string_length, **args):
        self.description = description
        self.name = name
        self.size_in_characters = characters
        self.max_string_length = max_string_length
    def HtmlForForm(self):
        format = """<b>%s</b> <input name="%s" size="%d" maxlength="%d"><br>\n"""
        return format % (
            self.description, self.name, self.size_in_characters, self.max_string_length
        )
    def SetValue(self, value):
        self.value = value
    def ValueForMySqlInsert(self):
        if(self.value == None):
            raise AttributeError, []
        return '"'+self.value+'"'  # quoted for MySQL
    def ColumnForMySqlInsert(self):
        return self.name

class IntField:
    def __init__(self, description, name, characters, **args):
        self.description = description
        self.name = name
        self.size_in_characters = characters
        self.failure_reason = None
        self.suppress_input = (
            args.has_key('suppress_input') and (args['suppress_input'] == True)
        )

    def HtmlForForm(self):
        if self.suppress_input:
            return ''
        format = """<b>%s</b> <input name="%s" size="%d" maxlength="%d"><br>\n"""
        return format % (
            self.description, self.name, self.size_in_characters, self.size_in_characters
        )
    def SetValue(self, value):
        try:
            self.value = int(value)
        except ValueError:
            self.failure_reason = "This should be an integer"
    def ValueForMySqlInsert(self):
        if(self.value == None):
            raise AttributeError, []
        return str(self.value)
    def ColumnForMySqlInsert(self):
        return self.name

class DateField:
    def __init__(self, description, name, **args):
        self.description = description
        self.name = name
        self.failure_reason = None
        self.suppress_input = (
            args.has_key('suppress_input') and (args['suppress_input'] == True)
        )
        self.value = None
    def HtmlForForm(self):
        if self.suppress_input:
            return ''
        else:
            raise NotImplementedError()
    def SetValue(self, date):
        self.value = date
    def ValueForMySqlInsert(self):
        if(self.value == None):
            raise AttributeError, []
        return '"'+self.value.isoformat()+'"'
    def ColumnForMySqlInsert(self):
        return self.name


class DateTimeField:
    def __init__(self, description, name, **args):
        self.description = description
        self.name = name
        self.failure_reason = None
        self.suppress_input = (
            args.has_key('suppress_input') and (args['suppress_input'] == True)
        )
        self.value = None
    def HtmlForForm(self):
        if self.suppress_input:
            return ''
        else:
            raise NotImplementedError()
    def SetValue(self, date):
        self.value = date
    def ValueForMySqlInsert(self):
        if(self.value == None):
            raise AttributeError, []
        return '"'+self.value.isoformat()+'"'
    def ColumnForMySqlInsert(self):
        return self.name
