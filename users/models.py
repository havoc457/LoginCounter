from django.db import models

class User (models.Model):
	user = models.CharField(max_length = 128, primary_key = True)
	password = models.CharField(max_length = 128)
	count = models.IntegerField(default = 0)
	def __unicode__(self):
	    return self.user

