from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = '__all__' # stands for all the fields in the model --hitesh
        
#class PropertySearch(forms.ModelForm) 
    #class Meta:
        #model = property
        #fields = ['address', 'property_type']