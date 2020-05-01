from django import forms

class Query(forms.Form):
    name = forms.CharField(max_length = 30)
    email = forms.EmailField(label = 'your email id')
    content = forms.CharField(widget = forms.Textarea)


