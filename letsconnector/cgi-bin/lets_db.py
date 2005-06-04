#!/usr/bin/python

import MySQLdb

def connection():
    """Connection for running on local machine -- assumes no restrictions
    on the database"""
    return MySQLdb.connect(
#        db="alisdair", host="localhost", user="alisdair", passwd=""
        db="lets_test", host="localhost", user="lets", passwd="monkeys"
    )
