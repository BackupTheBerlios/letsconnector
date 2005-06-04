import Fields
import pprint # for debug

class Form:
    """A base class defining a form. Forms includes the ability to:
    - print the HTML for form input
    - parse the POST information which returns
    - act on this information in some way
    Some of this will be implemented in subclasses"""
    
    def __init__(self, table):
        self.table = table
    fields = []
    title = ""
    action = ""
    submit_text = ""
    table = ""
    
    # public interface
    def input_form(self):
        """Prints the HTML for input on this form"""
        html_for_input = self._form_title()
        html_for_input += self._form_begin()
        for field in self.fields:
            html_for_input += field.HtmlForForm()
        html_for_input += self._submit()
        html_for_input += self._form_end()
        return html_for_input

    def receive_input(self, form):
        for field in self.fields:
            form_value = form.getfirst(field.name)
            if form_value != None:
                field.SetValue(form_value)

    def mysql_insert(self):
        """Returns a MySQL command to insert the data held in this form into
        a MySQL database.
        If this action is not appropriate to a particular form, it should
        be overridden with a stub which raises an exception."""
        name_list = ""
        value_list = ""
        for field in self.fields:
            name_list += field.ColumnForMySqlInsert() + ", "
            value_list += field.ValueForMySqlInsert() + ", "
        # tidy excess commas and spaces
        name_list = name_list[ 0 : len(name_list) - 2 ]
        value_list = value_list[ 0 : len(value_list) - 2 ]
        return "".join(["INSERT INTO ", self.table, " ( ", name_list, " ) ",
            " VALUES ( ", value_list, " );"])
    
    # Helpers ##########################################
    def _form_title(self):
        return "<h3>" + self.title + "</h3><p>\n";
    def _form_begin(self):
        format = """<form action="%s" method=post>\n"""
        return format % ( self.action )
    def _form_end(self):
        return "</form>"
    def _submit(self):
        format = """<input type=submit value="%s">\n"""
        return format % ( self.submit_text )
