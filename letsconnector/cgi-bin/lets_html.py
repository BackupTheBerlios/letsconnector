
class helpers:
    """A helper class for generating HTML"""
    # plain HTML helpers
    def begin(self):
        return "Content-Type: text/html\n\n<html>\n"
    def head(self):
        return "<head><title>LETS Connector</title></head>\n"
    def begin_body(self):
        return "<body>\n"
    def end_body(self):
        return "</body>\n"
    def end(self):
        return "</html>\n"
    # Form helpers
    # (this should make it easier to add tables)
    def form_begin(self, action):
        format = """<form action="%s" method=post>\n"""
        return format % ( action )
    def form_end(self):
        return "</form>"
    def submit(self, description):
        format = """<input type=submit value="%s">\n"""
        return format % ( description )
    # make a page with standard headers, footers etc.
    def page(self, body_text):
        page_out = self.begin()
        page_out += self.head()
        page_out += self.begin_body()
        page_out += body_text
        page_out += self.end_body()
        page_out += self.end()
        return page_out