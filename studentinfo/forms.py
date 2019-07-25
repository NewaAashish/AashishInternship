from django import forms
from studentinfo.models import Info, Marks, Final, AcademicExtra

class InfoForm(forms.ModelForm):
      Gender=[('Male','Male'),
            ('Female','Female'),
            ('Other','Other')]
      gender = forms.ChoiceField(choices=Gender, widget=forms.RadioSelect())

      class Meta:
            model = Info
            fields = '__all__'

class MarksForm(forms.ModelForm):
      class Meta:
            model = Marks
            # fields= '__all__'
            exclude=('student',)

class FinalForm(forms.ModelForm):
      class Meta:
            model = Final
            fields = '__all__'

class AcademicForm(forms.ModelForm):
      class Meta:
            model = AcademicExtra
            fields = '__all__'

class ContactForm(forms.Form):
      email = forms.CharField(required=True)
      contact = forms.CharField(required=True)
      subject = forms.CharField(required=True)
      msg = forms.CharField(required=True, widget=forms.Textarea)