from django import forms
from .models import Quote, Images

class QuoteForm(forms.ModelForm):
    fistName = forms.CharField(required=True, max_length=25, label="First Name")
    lastName = forms.CharField(required=True, max_length=25, label="Last Name")
    

    class Meta:
        model = Quote
        fields = ('fistName', 'lastName',)

    def __init__(self, *args, **kwargs):
        super(QuoteForm, self).__init__(*args, **kwargs)
        self.fields['fistName'].widget.attrs.update({'placeholder' : 'First Name'})
        self.fields['lastName'].widget.attrs.update({'placeholder' : 'Last Name'})
        
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='')    
    class Meta:
        model = Images
        fields = ('image', )

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class' : 'dragDropBox'})
