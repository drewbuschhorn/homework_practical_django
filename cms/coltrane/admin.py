from django.contrib import admin
from coltrane.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
	model = Entry
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Entry, EntryAdmin)
