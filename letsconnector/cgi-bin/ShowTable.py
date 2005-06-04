import lets_db


def ShowTableMembers():
    connection = lets_db.connection()
    cursor = connection.cursor()
    n = cursor.execute('SELECT * FROM members')
    table = cursor.fetchmany(n)
    connection.close()
    for x in table:
        if type(x[1]) == type(''):
            date = x[1]
        else:
            date = '%04d-%02d-%02d' % (x[1].year, x[1].month, x[1].day)
        print '   '.join(['%8d' % x[0], date, x[2]])


def ShowTableTrades():
    connection = lets_db.connection()
    cursor = connection.cursor()
    n = cursor.execute('SELECT * FROM trades')
    table = cursor.fetchmany(n)
    connection.close()
    for x in table:
        if type(x[1]) == type(''):
            date = x[1]
        else:
            date = '%04d-%02d-%02d,%02d:%02d' % (x[1].year, x[1].month, x[1].day, x[1].hour, x[1].minute)

        print """\
  Trade [%4d] at [%s] entered by member [%4d]:
      Sum of [%4d] reekies paid from member [%4d] to member [%4d]
      for [%s].
""" % (x[0], date, x[2], x[3], x[4], x[5], x[6])

