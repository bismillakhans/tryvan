from django import forms
from .models import Paper

class PaperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        self.fields['cname'].disabled = True
        self.fields['ccity'].disabled = True

    class Meta:
       model=Paper
       fields = '__all__'