#!/usr/bin/python

import MySQLdb

def connection():
    """Test connection for running on local machine -- assumes no restrictions
    on the database"""
    return MySQLdb.connect(
        db="lets_test", host="localhost", user="lets", passwd="monkeys"
    )
