# in your `forms.py`
from django import forms
from .models import Contact
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")

    widgets = {
        "name": forms.TextInput(attrs={"autofocus": True}),
    }

    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = "POST"
    #     self.helper.add_input(Submit("submit", "Send", css_class="btn btn-primary"))
