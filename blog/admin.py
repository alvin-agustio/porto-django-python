from django.contrib import admin

from .models import Tag, Author, Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Project, ProjectAdmin)