
class lets_html:
    """A helper class for generating HTML"""
    # plain HTML helpers
    def begin(self):
        return "<html>"
    def head(self):
        return "<head><title>LETS Connector</title></head>"
    def begin_body(self):
        return "<body>"
    def end_body(self):
        return "</body>"
    def end(self):
        return "</html>"
    # CGI helpers
    def text_input(self, description, name, size, maxlength):
        format = """<b>%s</b> <input name="%s" size="%d" maxlength="%d%><br>"""
        return format % ( description, name, size, maxlength )
    def date_input(self, description, name):
        format = """<b>%s</b> Date input not implemented :(<br>"""
        return format % ( description )
