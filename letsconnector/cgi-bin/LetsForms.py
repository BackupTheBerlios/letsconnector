import Form
import Fields

class CreateMember(Form.Form):
    """Form for creating a new member"""
    def __init__(self):
        Form.Form.__init__(self)
    title = "Create Member"
    fields = [
        Fields.TextField("Name:", "name", 40, 128, None),
        Fields.TextField("Address:", "address", 40, 255, None),
        Fields.TextField("Phone:", "phone_number_1", 20, 20, None),
        Fields.TextField("Alt. Phone:", "phone_number_2", 20, 20, None),
        Fields.TextField("Email:", "email_1", 40, 128, None),
        Fields.TextField("Alt. Email:", "email_2", 40, 128, None),
        Fields.DateField("Date Joined:", "date_joined"),
        Fields.TextField("Notes:", "notes", 40, 255, None)
    ]
