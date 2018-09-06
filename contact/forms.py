from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject= forms.CharField(required=True)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea,
        required=True,
        help_text='Hier kommt der Text hin!')
    captcha = ReCaptchaField(widget=ReCaptchaWidget())


    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        from_email = cleaned_data.get('from_email')
        subject = cleaned_data.get('subject')
        message = cleaned_data.get('message')
        if not from_email and not subject and not message:
            raise forms.ValidationError('Du musst schon was schreiben!')
