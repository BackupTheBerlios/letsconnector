#!/usr/bin/python

import cgi
import lets_html
import cgitb
import LetsForms

cgitb.enable()

form = cgi.FieldStorage()
c = LetsForms.CreateMember()

def form_for_input():
    """Prints the HTML form for creating a new member"""
    h = lets_html.helpers()
    body = "<h3>Add New Member</h3><p>\n"
    body += c.input_html() # Form object supplies the body of the form html
    body += h.submit("Add New Member")
    body += h.form_begin("create_member.cgi")
    body += h.form_end()
    return h.page(body)

def process_input(form):
    out = "Content-Type: text/plain\n\n"
    for key in form.keys():
        out += form.getfirst(key) + "\n"
    return out

if not form:
    print form_for_input()
else: # should have something to validate the form here really
    print process_input(form)