from __future__ import unicode_literals

from django.db import models

class post(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	date = models.DateTimeField()
	
	def__unicode__(self):
		return self.tile
		

# Create your models here.
