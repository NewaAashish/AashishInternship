from django.db import models

# Create your models here.
class Info(models.Model):
    name_text=models.CharField(max_length=30)
    roll=models.IntegerField(blank=True, null=True)
    grade=models.IntegerField(blank=True, null=True)
    faculty=models.CharField(max_length=20)
    contact=models.IntegerField()
    address=models.CharField(blank=True, null=True,max_length=20)
    email=models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    guardian_name=models.CharField(blank=True, null=True,max_length=20)
    guardian_relation=(
        ('Father','Father'),
        ('Mother','Mother'),
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('Others','Others'),
    )
    guardian_relation = models.CharField(max_length=50, choices=guardian_relation, blank=True, null=True, default='Father')
    guardian_contact=models.IntegerField(blank=True, null=True)
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

    def __str__(self):
        return self.student

class Final(models.Model):
    student=models.ForeignKey(Info,on_delete=models.CASCADE, blank=True, null=True)
    final_english=models.IntegerField(blank=True, null=True)
    final_science=models.IntegerField(blank=True, null=True)
    final_maths=models.IntegerField(blank=True, null=True)
    final_nepali=models.IntegerField(blank=True, null=True)    
    final_computer=models.IntegerField(blank=True, null=True)
    final_social=models.IntegerField(blank=True, null=True)
    final_eph=models.IntegerField(blank=True, null=True)
    final_account=models.IntegerField(blank=True, null=True)
    final_total=models.IntegerField(blank=True, null=True)
    final_percent=models.FloatField(null=True, blank=True)
    final_remarks=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.student.name_text

class AcademicExtra(models.Model):
    student=models.ForeignKey(Info,on_delete=models.CASCADE, blank=True, null=True)
    total_attendance=models.IntegerField(blank=True, null=True)
    extra_cirruculum_remarks=models.TextField(null=True, blank=True)
    academic_activity_remarks=models.TextField(null=True, blank=True)
    achievements=models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.student.name_text