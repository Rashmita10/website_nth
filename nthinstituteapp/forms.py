from django import forms
from django.contrib.auth.models import User
from.models import CommentData
class CommentForm(forms.ModelForm):
    content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control','placeholder':'text here...','cols':10,'rows':10}))
    class Meta:
        model=CommentData
        fields=('content',)
class ContactForm(forms.Form):
    first_name=forms.CharField(
         label='Enter First Name:',
         widget=forms.TextInput(
           attrs={
               'class':'form-control',
                'placeholder':'First Name...'

           }
         )
    )
    last_name=forms.CharField(
         label='Enter Last Name:',
         widget=forms.TextInput(
           attrs={
               'class':'form-control',
                'placeholder':'Last Name...'
        }
    )
)

email=forms.EmailField(
     label='Enter Email:',
     widget=forms.EmailInput(
       attrs={
           'class':'form-control',
            'placeholder':'Email'
            }
     )
)


mobile=forms.IntegerField(
     label='Enter mobile Number:',
     widget=forms.NumberInput(
       attrs={
           'class':'form-control',
            'placeholder':'MobileNo'
    }
   )
)
location=forms.CharField(
     label='Enter Your Location:',
     widget=forms.TextInput(
       attrs={
           'class':'form-control',
            'placeholder':'Your Location...'
    }
)
)

courses=forms.CharField(
     label='Enter Your Course:',
     widget=forms.TextInput(
       attrs={
           'class':'form-control',
            'placeholder':'Course...'
    }
)
)

referred_by=forms.CharField(
     label='Enter Name:',
     widget=forms.TextInput(
       attrs={
           'class':'form-control',
            'placeholder':'Refered Person NAME...'
    }
)
)
