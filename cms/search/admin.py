from django.contrib import admin

from search.models import SearchKeyword

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
	
class SearchKeywordInline(admin.StackedInline):
	model = SearchKeyword
	extra = 3

class CustomFlatPageAdmin(FlatPageAdmin):
	def __init__(self,*args, **kwargs):
        	FlatPageAdmin.__init__(self,*args, **kwargs)
		try:
			if self.inlines:
				self.inlines.extend[SearchKeywordInline,]
			else:
				self.inlines = [SearchKeywordInline,]
		
		#Try to be friendly about extending, but don't beat yourself
		#up over it. Todo: Add logger			
		except Exception as e:
			print e
			self.inlines = [SearchKeywordInline,]


#unregister the default FlatPage admin and register CustomFlatPageAdmin.
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
