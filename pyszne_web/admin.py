from django.contrib import admin
from .models import Article


# Register your models here.
admin.site.register(Article)
list_filter = ["year", "author", "category"]
search_fields = ["title", "content"]
list_display = ["title", "author", "category", "published"]
list_editable = ["category"]
list_per_page = 10
admin.site.site_header = "Pyszne Admin"
admin.site.site_title = "Pyszne Admin Portal"
admin.site.index_title = "Welcome to Pyszne Portal"
