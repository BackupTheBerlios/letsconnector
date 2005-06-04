import Form
import Fields
import lets_db
import datetime

class CreateMember(Form.Form):
    """Form for creating a new member"""
    def __init__(self, table):
        Form.Form.__init__(self, table)

    date_field = Fields.DateField("Date joined:", "date_joined", suppress_input=True)
    fields = [
        Fields.IntField("Membership number:", "member_id", 5),
#        Fields.PasswordField("Password:", "sha1_password"),
        date_field,
#        Fields.DateField("Date left (or dormant):", "date_left_or_dormant"),
#        Fields.DateField("Next renewal date:", "next_renewal_date"),
#        Fields.DateField("Membership status:", "status"),
        Fields.TextField("Notes:", "notes", 40, 255)
    ]
    title = "Create Member"
    action = "create_member.cgi"
    submit_text = "Add New Member"

    def receive_input(self, form):
        Form.Form.receive_input(self, form)
        self.date_field.SetValue(datetime.date.today())

    def db_action(self):
        connection = lets_db.connection()
        mysql_string = self.mysql_insert()
        cursor = connection.cursor()
        cursor.execute(mysql_string, [])
        connection.commit()
        connection.close()

class Trade(Form.Form):
    """Form for making a payment"""
    def __init__(self, table):
        Form.Form.__init__(self, table)

    date_field = Fields.DateField("Date entered:", "date_of_trade", suppress_input=True)
    fields = [
        date_field,
        Fields.IntField("Entered by member (ID):", "member_id_entered_by", 5),
        Fields.IntField("Amount:", "amount", 5),
        Fields.IntField("From member (ID):", "member_id_from", 5),
        Fields.IntField("To member (ID):", "member_id_to", 5),
        Fields.TextField("Description:", "description", 40, 255)
    ]
    title = "Trade"
    action = "trade.cgi"
    submit_text = "Make A Trade"

    def receive_input(self, form):
        Form.Form.receive_input(self, form)
        self.date_field.SetValue(datetime.datetime.now())

    def db_action(self):
        connection = lets_db.connection()
        mysql_string = self.mysql_insert()
        cursor = connection.cursor()
        cursor.execute(mysql_string, [])
        connection.commit()
        connection.close()
