from django import forms
from website.models import Contact, Subscribe
from captcha.fields import CaptchaField

class Contacts(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = Contact
        fields = "__all__"
        #exclude = ["name"]
    
    
        
class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        fields = "__all__"
