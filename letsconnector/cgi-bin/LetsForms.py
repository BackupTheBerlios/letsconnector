import Form
import Fields
import lets_db

class CreateMember(Form.Form):
    """Form for creating a new member"""
    def __init__(self, table):
        Form.Form.__init__(self, table)

    fields = [
        Fields.IntField("Membership number:", "member_id", 5),
#        Fields.PasswordField("Password:", "sha1_password"),
#        Fields.DateField("Date joined:", "date_joined"),
#        Fields.DateField("Date left (or dormant):", "date_left_or_dormant"),
#        Fields.DateField("Next renewal date:", "next_renewal_date"),
#        Fields.DateField("Membership status:", "status"),
        Fields.TextField("Notes:", "notes", 40, 255)
    ]
    title = "Create Member"
    action = "create_member.cgi"
    submit_text = "Add New Member"

    def db_action(self):
        connection = lets_db.connection()
        mysql_string = self.mysql_insert()
        cursor = connection.cursor()
        cursor.execute(mysql_string, [])
        connection.commit()
