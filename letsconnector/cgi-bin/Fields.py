# Module file, not run as script.
# contains base class and subclasses for form fields.

class Field:
    def __init__(self):
        pass
    def input_html(self):
        pass
    def set_value(self, value):
        pass
    def text_for_mysql_insert(self):
        pass
    description = ""
    name = ""
        
class TextField(Field):
    def __init__(self, description, name, screen_size, max_size, default):
        Field.__init__(self)
        self.description = description
        self.name = name
        self.screen_size = screen_size
        self.max_size = max_size
        self.default = default
    description = ""
    name = ""
    value = ""
    screen_size = 0
    max_size = 0
    default = None
    def input_html(self):
        format = """<b>%s</b> <input name="%s" size="%d" maxlength="%d"><br>\n"""
        return format % ( self.description, self.name, self.screen_size, self.max_size )
    def set_value(self, value):
        self.value = value;
    def value_for_mysql_insert(self):
        if(self.value == None):
            raise AttributeError, []
        return "\""+self.value+"\""  # quoted for MySQL
    def name_for_mysql_insert(self):
        return self.name

class DateField(Field):
    def __init__(self, description, name):
        Field.__init__(self)
        self.description = description
        self.name = name
    description = ""
    name = ""
    def input_html(self):
        format = """<b>%s</b> Date input not implemented :(<br>\n"""
        return format % ( self.description )
    def set_value(self, value):
        """alas, I am but a poor humble stub"""
        pass
    def value_for_mysql_insert(self):
        return ""
    def name_for_mysql_insert(self):
        return ""