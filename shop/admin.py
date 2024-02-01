from django.contrib import admin
from .models import Category, Course
# Register your models here.
# 3 строчки ниже настраивают текст на админ панели
admin.site.site_header = "Store admin panel"
admin.site.site_title = "Shop"
admin.site.index_title = "Welcome to the admin"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('titel', 'price', 'category', 'id')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoruAdmin(admin.ModelAdmin):
    list_display = ('titel', 'created_at')
    fieldsets = [
        (None, {'fields': ['titel']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoruAdmin)
admin.site.register(Course, CourseAdmin)
