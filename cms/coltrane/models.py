from django.db import models
from django.contrib.auth.models import User
import datetime
from markdown import markdown
from tagging.fields import TagField

class Category(models.Model):
	title = models.CharField(max_length=250,help_text='Maximum 250 chars')
	#Prepopulate_from moved to admin
	slug = models.SlugField(unique=True)
	description = models.TextField()

	#Kept but old style
	#Class Admin:
	#	pass

	class Meta:
		verbose_name_plural="Categories"	

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/categories/%s/" % self.slug

class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
                (LIVE_STATUS, 'Live'),
                (DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
        )	

        class Meta:
                verbose_name_plural="Entries"
		ordering = ['-pub_date']
	
	#Changed to DJ1.0 style
	#class Admin:
	#	pass

	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	excerpt_html = models.TextField(editable=False, blank=True)
	body = models.TextField()
	body_html = models.TextField(editable=False, blank=True)

	pub_date = models.DateTimeField()
	slug = models.SlugField(default=datetime.datetime.now,
				unique_for_date='pub_date')
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	categories = models.ManyToManyField(Category)
	tags = TagField()

	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return "weblog/%s/%s/" % (
			self.pub_date.strftime("%Y/%b/%d").lower(),self.slug)

	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save()
