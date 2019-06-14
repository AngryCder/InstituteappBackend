from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	roll = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100,blank=True)
	department = models.CharField(max_length=100)
	phone = models.CharField(max_length=10,blank=True)
	email = models.CharField(max_length=100,blank=True)
	year = models.CharField(max_length=100,blank=True)
	fcmtoken = models.CharField(max_length=500, blank=True)
	reg_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name 


class Complain(models.Model):
	complainby = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,editable=False)
	complain = models.TextField()
	def __str__(self):
		if self.complainby:
			return "complain by " + self.complainby.name 
		return "complain by anonymous"

class CouncilandCell(models.Model):
	name = models.CharField(max_length=100, blank=True)
	image = models.ImageField(null=True,blank=True)
	def __str__(self):
		return self.name

class Club(models.Model):
	councilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	name = models.CharField(max_length=100, blank=True)
	clubimage = models.ImageField(null=True,blank=True)
	def __str__(self):
		return self.name

class Notification(models.Model):
	# coun/cilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	clubname = models.ForeignKey(Club, on_delete = models.CASCADE,verbose_name='Club/Cell Name',blank=False,null =True)

	# clubname = ChainedForeignKey(Club, chained_field="councilname",chained_model_field="councilname",
 #        auto_choose=True,
 #        show_all=False,
 #        sort=True, null=True,blank=True)
	notification = models.CharField(max_length= 1000, verbose_name='Title')
	notification_header = models.CharField(max_length = 100,verbose_name='Description')
	notification_pic = models.ImageField(null=True,blank=True,verbose_name='Image')
	datetime = models.DateTimeField()
	location = models.CharField(max_length = 300)
	viewedby = models.ManyToManyField(Student,editable=False)
	# interested_count = models.ManyToManyField(Student,editable=False)

	def __str__(self):
		return self.notification_header


