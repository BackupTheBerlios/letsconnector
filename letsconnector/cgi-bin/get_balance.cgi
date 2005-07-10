#!/usr/bin/python

import cgi
import lets_html
import cgitb
import LetsForms

cgitb.enable()

form = cgi.FieldStorage()
c = LetsForms.GetBalance("trades")
h = lets_html.helpers()

def form_for_input():
    """Prints the HTML form for creating a new member"""
    h = lets_html.helpers()
    body = c.input_form() # Form object supplies the body of the form html
    return h.page(body)

def process_input(form):
    """Do the database stuff to create a new member"""
    c.receive_input(form)
    c.db_action()
    return form_print(c)
  
def form_print(c):
    body_text = "<h3><strong>Current Balance</strong></h3><p>\n"
    body_text += "Balance for member ID <strong>%d</strong> is: <strong>%d</strong> Reekies" % (c.id, c.balance)
    return h.page(body_text)

if not form:
    print form_for_input()
else: # should have something to validate the form here really
    print process_input(form)
