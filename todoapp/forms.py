from django import forms

class TaskForm(forms.Form):
    note = forms.CharField(label='Task :',widget=forms.Textarea())
    # note = forms.BooleanField(label='Task :',widget=forms.CheckboxInput())
    
