from django.contrib import admin
from .models import Category, Adv


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class AdvAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phone')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Adv, AdvAdmin)
