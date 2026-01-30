from django import forms
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        exclude = ['created_at','updated_at']
        
        #for widgets we customise the layouts
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Menu Item Name',
                'required':True}
            ),
            'description': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Menu Item Description',
                'required':True,
                'rows':4}
            ),
            'price': forms.NumberInput(attrs={
                'class':'form-control',
                'min':0,
                'step':0.01,
                'required':True}
            ),
            'category':forms.Select(attrs={
                'class':'form-control'
            }),
            'is_available':forms.CheckboxInput(attrs={
                'class':'form-control'
            })
        }
        
