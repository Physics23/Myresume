from django import forms
from contactform.models import Touch


class TouchForm(forms.ModelForm):

    class Meta:

        model = Touch
        fields = "__all__"
