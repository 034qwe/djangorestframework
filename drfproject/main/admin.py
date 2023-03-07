from django.contrib import admin
from .models import Articles,Category_Articles
# Register your models here.

admin.site.register(Articles)
admin.site.register(Category_Articles)