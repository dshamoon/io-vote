from checklist.models import Check, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class CheckAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,                {'fields': ['question']}),
	('Date Information',  {'fields': ['pub_date'],
							'classes': ['collapse']}) 
	]
	inlines = [ChoiceInline]

admin.site.register(Check, CheckAdmin)
admin.site.register(Choice)