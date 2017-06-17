from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EntryQuerySet(models.QuerySet):
	"""docstring for EntryQuerySet"""
	def published(self):
		return self.filter(publish=True)
		

class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	slug = models.slugField(max_length=200,unique=True)
	publish = models.BoolenField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = EntryQuerySet.as_manager()
	def __str__(self):
		return self.title

	class Meta:
			verbose_name = " Blog Entry "
			verbose_name_plural = " Blog Entries "
			ordering = ["-created"]
					

		