from django.forms import ModelForm
from studentinfo.models import Info, Marks

class InfoForm(ModelForm):
   class Meta:
         model = Info
         fields = '__all__'

class MarksForm(ModelForm):
      class Meta:
            model = Marks
            # fields= '__all__'
            exclude=('student',)





