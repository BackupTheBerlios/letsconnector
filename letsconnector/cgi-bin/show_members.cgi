#!/usr/bin/python

import ShowTable, lets_html

import cgitb

cgitb.enable()

h = lets_html.helpers()

print h.begin()
print '<pre>'
ShowTable.ShowTableMembers()
print '</pre>'
print h.end()