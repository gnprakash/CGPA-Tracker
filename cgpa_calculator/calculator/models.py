from django.db import models

class User1(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    no_of_semesters = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.username
    
class Semester1(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    subject1 = models.CharField(max_length=2, null=True, blank=True)
    subject2 = models.CharField(max_length=2, null=True, blank=True)
    subject3 = models.CharField(max_length=2, null=True, blank=True)
    subject4 = models.CharField(max_length=2, null=True, blank=True)
    subject5 = models.CharField(max_length=2, null=True, blank=True)
    subject6 = models.CharField(max_length=2, null=True, blank=True)
    subject7 = models.CharField(max_length=2, null=True, blank=True)
    subject8 = models.CharField(max_length=2, null=True, blank=True)
    subject9 = models.CharField(max_length=2, null=True, blank=True)
    gpa = models.CharField(max_length=4, null=True, blank=True)

class Semester2(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    subject1 = models.CharField(max_length=2, null=True, blank=True)
    subject2 = models.CharField(max_length=2, null=True, blank=True)
    subject3 = models.CharField(max_length=2, null=True, blank=True)
    subject4 = models.CharField(max_length=2, null=True, blank=True)
    subject5 = models.CharField(max_length=2, null=True, blank=True)
    subject6 = models.CharField(max_length=2, null=True, blank=True)
    subject7 = models.CharField(max_length=2, null=True, blank=True)
    subject8 = models.CharField(max_length=2, null=True, blank=True)
    subject9 = models.CharField(max_length=2, null=True, blank=True)
    gpa = models.CharField(max_length=4, null=True, blank=True)

class Semester3(models.Model):
    user = models.OneToOneField(User1, on_delete=models.CASCADE, primary_key=True)
    subject1 = models.CharField(max_length=2, null=True, blank=True)
    subject2 = models.CharField(max_length=2, null=True, blank=True)
    subject3 = models.CharField(max_length=2, null=True, blank=True)
    subject4 = models.CharField(max_length=2, null=True, blank=True)
    subject5 = models.CharField(max_length=2, null=True, blank=True)
    subject6 = models.CharField(max_length=2, null=True, blank=True)
    subject7 = models.CharField(max_length=2, null=True, blank=True)
    subject8 = models.CharField(max_length=2, null=True, blank=True)
    subject9 = models.CharField(max_length=2, null=True, blank=True)
    gpa = models.CharField(max_length=4, null=True, blank=True)

