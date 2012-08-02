from django.db import models
from django.contrib.flatpages.models import FlatPage

## See https://docs.djangoproject.com/en/dev/releases/1.0-porting-guide/
class SearchKeyword(models.Model):
	keyword = models.CharField(max_length=50) # ,core=True) ## core has been deprecated in dj1.0+
	page	= models.ForeignKey(FlatPage) #, edit_inline=models.STACKED, 
					# min_num_in_admin=3, num_extra_on_change=1) ## deprecated in dj1.0+

	#Converted to DJ1.0 way of doing things, see admin.py
	#class Admin:
	#	pass

	def __unicode__(self):
		return self.keyword


