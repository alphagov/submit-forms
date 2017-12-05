from django.contrib import admin
from .models import Organisation, Phase, DataType, InputType, List, ListItem, Item, Field, Page, Section, Form, PageField, FormSection, SectionPage



@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['organisation', 'name']


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ['phase']


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('datatype', 'description')


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['inputtype']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['label', 'value']


class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 1


@admin.register(List)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'datatype']
    inlines = (ListItemInline,)


class PageFieldInline(admin.TabularInline):
    model = PageField
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page', 'pagetype', 'heading']
    inlines = (PageFieldInline,)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['field', 'label', 'inputtype', 'datatype']


class SectionPageInline(admin.TabularInline):
    model = SectionPage
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'heading']
    inlines = (SectionPageInline,)


class FormSectionInline(admin.TabularInline):
    model = FormSection
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['form', 'heading', 'phase', 'reference']
    inlines = (FormSectionInline,)
