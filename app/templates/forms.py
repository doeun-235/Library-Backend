from django import forms
from app.models import Book_owned, Book_disposal

class OwnedForm(forms.ModelForm):
    class Meta :
        model = Book_owned
        fields = "__all__"