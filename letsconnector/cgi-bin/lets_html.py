
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
    # make a page with standard headers, footers etc.
    def page(self, body_text):
        page_out = self.begin()
        page_out += self.head()
        page_out += self.begin_body()
        page_out += body_text
        page_out += self.end_body()
        page_out += self.end()
        return page_out