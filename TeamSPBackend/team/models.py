from django.db import models
from TeamSPBackend.account.models import Account
# Create your models here.

class Student(models.Model):
    student_id = models.IntegerField(verbose_name='id', primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    class Meta:
        db_table = 'student'


class Team(models.Model):
    team_id = models.AutoField(verbose_name='id', primary_key=True)
    name = models.CharField(max_length=30, unique= True)
    project_name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    # supervisor = models.ForeignKey('Account',on_delete= models.SET_NULL)
    supervisor_id = models.IntegerField()
    # member = models.ForeignKey('Student',on_delete= models.SET_NULL)
    # member_id = models.IntegerField()
    create_date = models.BigIntegerField(max_length=20, blank=False, null=False)
    expired = models.BigIntegerField(max_length=20, blank=False, null=False, db_index=True)
    class Meta:
        db_table = 'team'

class Team_member(models.Model):
    id = models.AutoField(verbose_name='id', primary_key=True)
    team_id = models.IntegerField()
    student_id = models.IntegerField()
    class Meta:
        db_table = 'team_member'

