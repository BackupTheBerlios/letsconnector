#!/usr/bin/python

import cgi
import lets_html
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

def form_for_input():
    """Prints the HTML form for creating a new member"""
    h = lets_html.helpers()
    body = "<h3>Add New Member</h3><p>\n"
    body += h.form_begin("create_member.cgi")
    body += h.text_input("Name:", "name", 40, 128)
    body += h.text_input("Address:", "address", 40, 255)
    body += h.text_input("Phone:", "phone_number_1", 20, 20)
    body += h.text_input("Alt. Phone:", "phone_number_2", 20, 20)
    body += h.text_input("Email:", "email_1", 40, 128)
    body += h.text_input("Alt. Email:", "email_2", 40, 128)
    body += h.date_input("Date Joined:", "date_joined")
    body += h.text_input("Notes:", "notes", 40, 255)
    body += h.submit("Add New Member")
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