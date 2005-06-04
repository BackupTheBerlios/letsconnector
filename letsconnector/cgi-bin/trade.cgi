#!/usr/bin/python

import cgi
import lets_html
import cgitb
import LetsForms

cgitb.enable()

form = cgi.FieldStorage()
c = LetsForms.Trade("trades")

def form_for_input():
    """Prints the HTML form for creating a new trade"""
    h = lets_html.helpers()
    body = c.input_form() # Form object supplies the body of the form html
    return h.page(body)

def process_input(form):
    """Do the database stuff to create a new trade"""
    c.receive_input(form)
    c.db_action()
    return form_print_test(form)

def form_print_test(form):  
    out = "Content-Type: text/plain\n\n"
    for key in form.keys():
        out += form.getfirst(key) + "\n"
    return out

if not form:
    print form_for_input()
else: # should have something to validate the form here really
    print process_input(form)
