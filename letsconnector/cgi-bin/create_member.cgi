#!/usr/bin/python

import lets_html.py
import cgitb

cgitb.enable()

def create_member_ui():
    """Prints the HTML form for creating a new member"""
    print "Content-Type: text/html\n\n"

    print lets_html.begin()
    print lets_html.begin_body()

    print "<h3>Add New Member</h3><p>"
    print "<form action=create_member.cgi method=post>"
    print lets_html.text_input("Name:", "name", 40, 128)
    print lets_html.text_input("Address:", "address", 40, 255)
    print lets_html.text_input("Phone:", "phone_number_1", 20, 20)
    print lets_html.text_input("Alt. Phone:", "phone_number_2", 20, 20)
    print lets_html.text_input("Email:", "email_1", 40, 128)
    print lets_html.text_input("Alt. Email:", "email_2", 40, 128)
    print lets_html.date_input("Date Joined:", "date_joined")
    print lets_html.text_input("Notes:", "notes", 40, 255)
    print "</form>"

    print lets_html.end_body()
    print lets_html.end()