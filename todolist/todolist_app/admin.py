from django.contrib import admin
from .models import Todo, Review, Tag

admin.site.register(Todo)
admin.site.register(Review)
admin.site.register(Tag)