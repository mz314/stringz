from django.contrib import admin
from strings.models import String, StringSet, StringStringSet, ScaleLength, Guitar

class StringStringsetInline(admin.TabularInline):
    model = StringStringSet

class StringSetAdmin(admin.ModelAdmin):
    inlines = [StringStringsetInline]

admin.site.register(Guitar)
admin.site.register(StringSet, StringSetAdmin)
admin.site.register(String)
admin.site.register(ScaleLength)
