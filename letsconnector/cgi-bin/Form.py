import Fields

class Form:
    """A base class defining a form. Forms includes the ability to:
    - print the HTML for form input
    - parse the POST information which returns
    - act on this information in some way
    Some of this will be implemented in subclasses"""
    def __init__(self):
        pass
    fields = []
    title = ""
    def input_form(self):
        """Prints the HTML for input on this form"""
        html_for_input = "<h3>" + self.title + "</h3><p>\n"
        for field in self.fields:
            html_for_input += field.input_html()
        return html_for_input
    
