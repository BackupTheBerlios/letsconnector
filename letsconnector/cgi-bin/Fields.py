# Module file, not run as script.
# contains base class and subclasses for form fields.

class Field:
    def __init__(self):
        pass
    def input_html(self):
        pass

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
    screen_size = 0
    max_size = 0
    default = None
    def input_html(self):
        format = """<b>%s</b> <input name="%s" size="%d" maxlength="%d"><br>\n"""
        return format % ( self.description, self.name, self.screen_size, self.max_size )

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
