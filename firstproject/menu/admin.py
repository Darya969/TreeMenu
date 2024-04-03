from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Records, Category


class RecordsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Records, RecordsAdmin)


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)