from django.db import models

# Create your models here.

class Check(models.Model):
	question = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question
	
	
class Choice(models.Model):
	check = models.ForeignKey(Check)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField() 
	def __unicode__(self):
			return self.choice
