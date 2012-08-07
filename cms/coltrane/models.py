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

	def live_entry_set(self):
		from coltane.models import Entry
		return self.entry_set.filter(status=Entry.LIVE_STATUS)


class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager,self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
                (LIVE_STATUS, 'Live'),
                (DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
        )	

	live = LiveEntryManager()
	objects = models.Manager()

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

	@models.permalink
	def get_absolute_url(self):
		return ('coltrane_entry_detail',(),{
			'year': self.pub_date.strftime("%Y"),
			'month': self.pub_date.strftime("%b").lower(),
			'day': self.pub_date.strftime("%d"),
			'slug': self.slug,
			})

	def save(self):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save()

class Link(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	description_html = models.TextField(blank=True,editable=False)
	url = models.URLField(unique=True)
	posted_by = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(unique_for_date='pub_date')
	tags = TagField()
	enable_comments = models.BooleanField(default = True)
	post_elsewhere = models.BooleanField('Post to Delicious',default=True)
	via_link = models.CharField('Via',max_length='250',blank=True)
	via_url = models.URLField('Via URL',blank=True)
	
	class Meta:
		ordering = ['-pub_date']
	
	# class Admin:
	#	pass

	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		#Not bothering with delicious
		super(Link,self).save()
	

	def __unicode__(self):
		return self 

	@models.permalink
	def get_absolute_url(self):
		return ('coltrane_link_detail',(), {
			'year': self.pub_date.strftime("%Y"),
			'month': self.pub_date.strftime("%b").lower(),
			'day': self.pub_date.strftime("%d"),
			'slug': self.slug,
			})
