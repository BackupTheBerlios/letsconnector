# Module file, not run as script.
# contains base class and subclasses for form fields.

class TextField:
    def __init__(self, description, name, characters, max_string_length):
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
        return "\""+self.value+"\""  # quoted for MySQL
    def ColumnForMySqlInsert(self):
        return self.name

class IntField:
    def __init__(self, description, name, characters):
        self.description = description
        self.name = name
        self.size_in_characters = characters
	self.failure_reason = None
    def HtmlForForm(self):
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
        return self.value
    def ColumnForMySqlInsert(self):
        return self.name

        
# class DateField(Field):
#     def __init__(self, description, name):
#         Field.__init__(self)
#         self.description = description
#         self.name = name
#     description = ""
#     name = ""
#     def input_html(self):
#         format = """<b>%s</b> Date input not implemented :(<br>\n"""
#         return format % ( self.description )
#     def set_value(self, value):
#         """alas, I am but a poor humble stub"""
#         pass
#     def value_for_mysql_insert(self):
#         return ""
#     def name_for_mysql_insert(self):
#         return ""

