from django import forms


class GetDataForm(forms.Form):
    location = forms.CharField(label="Enter location e.g. 'Leeds'", max_length=255)
