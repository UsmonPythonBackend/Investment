from django.contrib import admin
from .models import Services, Clients, Advisers, FAQs, Features, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'title', 'description', 'image', 'price')
    list_display_links = ('id', 'slug', 'title', 'description', 'image', 'price')
    search_fields = ('id', 'title')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Advisers)
class AdvisersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'slug', 'first_name', 'last_name', 'level', 'email')
    list_display_links = ('id', 'slug', 'first_name', 'last_name', 'level', 'email')
    search_fields = ('id', 'first_name')
    ordering = ('id',)
    prepopulated_fields = {'slug': ('first_name',)}


@admin.register(Clients)
class ClientsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email', 'phone')
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email', 'phone')
    search_fields = ('id', 'first_name')
    ordering = ('id',)


@admin.register(FAQs)
class FAQsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'question', 'answer')
    list_display_links = ('id', 'question', 'answer')
    ordering = ('id',)


@admin.register(Features)
class FeaturesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')
    ordering = ('id',)


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')
    ordering = ('id',)

