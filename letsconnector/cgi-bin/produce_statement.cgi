#!/usr/bin/python

import cgi
import lets_db
import lets_form
import lets_html
import cgitb
import string
import LetsForms

cgitb.enable()

form = cgi.FieldStorage()
c = LetsForms.ProduceStatement("members")

width = 80 # XXX: where should this be set, ideally?  User prefs?

def form_for_input():
    """Prints the HTML form to get a membership number"""
    h = lets_html.helpers()
    body = c.input_form() # Form object supplies the body of the form html
    return h.page(body)

def process_input(form):
    """Get the membership number and produce a statement"""
    c.receive_input(form)
    return form_print_statement(form)
  
def form_print_statement(form):  
    member_id = None
    for field in c.fields:
        if field.ColumnForMySqlInsert() == "member_id":
            member_id = field.ValueForMySqlInsert()
            break
    if not member_id:
        raise lets_form.FormEmptyQuery
    # XXX: security risk, user-supplied member_id could contain SQL
    id_string = "'%s'" % str(member_id)
    db = lets_db.connection()
    cursor = db.cursor()
    cursor.execute("""SELECT date_of_trade AS date,"""
                   """       member_id_from AS from_id,"""
                   """       member_id_to AS to_id,"""
                   """       description,"""
                   """       amount"""
                   """ FROM trades"""
                   """ WHERE member_id_from = %s"""
                   """ OR member_id_to = %s"""
                   """ ORDER BY date"""
                   % (id_string, id_string))
    rows = cursor.fetchall()
    cursor.close()
    
    ## produce text for statement
    text = ""

    text += string.center("EdinburghLETS statement of account",
                          width) + "\n"
    text += "\n"
    text += "Account #%s\n" % str(member_id)
    # name, address, from & to dates will go here

    date_width = len("dd/mm/yyyy")
    other_width = 3
    out_width = 8
    in_width = 8
    balance_width = 9
    description_width = (width - date_width - other_width
                         - out_width - in_width
                         - balance_width - 5)
    text += ("%s %s %s %s %s %s\n" %
             (string.ljust("Date", date_width),
              string.ljust("Acc", other_width),
              string.ljust("Description", description_width),
              string.rjust("Out", out_width),
              string.rjust("In", in_width),
              string.rjust("Balance", balance_width)))

    def row_text(date, other, description, out, in_, balance):
        if date <> "":
            date_text = date.strftime("%d/%m/%Y")
        else:
            date_text = ""
        if len(other) > other_width:
            other_text = other[:other_width]
        else:
            other_text = other
        if out == 0:
            out = ""
        else:
            out = "%.2f" % out
        if in_ == 0:
            in_ = ""
        else:
            in_ = "%.2f" % in_
        balance_field = "%.2f" % balance
        if len(description) > description_width:
            description = description[:description_width]
        return ("%s %s %s %s %s %s\n" %
                (string.ljust(date_text, date_width),
                 string.ljust(other_text, other_width),
                 string.ljust(description, description_width),
                 string.rjust(out, out_width),
                 string.rjust(in_, in_width),
                 string.rjust(balance_field, balance_width)))

    running_balance = 0.0
    text += "-" * width + "\n"
    ## holdovers from my old class-based code.  Might be handy if we
    ## want to let users specify dates from and to.
#     if self.brought_forward:
#         if self.date_from:
#             date = self.date_from
#         else:
#             date = ""
#         text += row_text(date, "", "Brought forward", 0.0, 0.0,
#                          self.brought_forward)
#         running_balance = self.brought_forward
    for row in rows:
        date, from_, to, description, amount = row
        out = in_ = 0.0
        if str(from_) == str(member_id):
            out = amount
            other = str(to)
        if str(to) == str(member_id):
            # not 'else if'; that would go wrong if someone traded
            # with themselves
            in_ = amount
            other = str(from_)
        running_balance = running_balance + in_ - out
        text += row_text(date, other, description, out, in_, running_balance)
    text += "-" * width + "\n"
    text += row_text("", "", "Statement closing balance", 0.0, 0.0,
                     running_balance)

    out = "Content-Type: text/plain\n\n"
    out += text
    return out

if not form:
    print form_for_input()
else: # should have something to validate the form here really
    print process_input(form)
