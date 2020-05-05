from django import forms
import datetime


display_choice=( ('public', 'public' ), ('private', 'private'))
class Query(forms.Form):
    name= forms.CharField( max_length=100, required=True)
    email = forms.EmailField(label= "Your Email-ID", required= True)
    display= forms.ChoiceField(label="If you choose public, your query will be displayed publicaly", choices=display_choice)
    message= forms.CharField(widget=forms.Textarea,max_length=500)


