from django.db import models

# Create your models here.
class Info(models.Model):
    name_text=models.CharField(max_length=30)
    batch_no=models.IntegerField()
    faculty=models.CharField(max_length=20)
    contact=models.IntegerField()
    image=models.ImageField(upload_to='documents/', blank=True, null=True, default='documents/dummyprofile.png')
    
    def __str__(self):
        return self.name_text
    
class Marks(models.Model):
    TERMINAL    = (
    ('first_term', 'first_term'),
    ('second_term', 'second_term'),
    ('third_term', 'third_term'),  
    )
    terminal = models.CharField(max_length=50, choices=TERMINAL, blank=True, null=True, default='first_term')

    student=models.ForeignKey(Info,on_delete=models.CASCADE, blank=True, null=True)
    roll=models.IntegerField()
    english=models.IntegerField()
    science=models.IntegerField()
    maths=models.IntegerField()
    nepali=models.IntegerField()
    computer=models.IntegerField()
    social=models.IntegerField()
    eph = models.IntegerField()
    account = models.IntegerField()
    total = models.IntegerField(blank=True, null=True)
    percent = models.FloatField(null=True, blank=True)

    def __int__(self):
        return self.roll