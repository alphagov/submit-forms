from django.contrib import admin
from .models import Organisation, Phase, DataType, InputType, List, ListItem, Item, Field, Question, Section, Form, QuestionField, FormSection, SectionQuestion



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


class QuestionFieldInline(admin.TabularInline):
    model = QuestionField
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'heading']
    inlines = (QuestionFieldInline,)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ['field', 'label', 'inputtype', 'datatype']


class SectionQuestionInline(admin.TabularInline):
    model = SectionQuestion
    extra = 1


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'heading']
    inlines = (SectionQuestionInline,)


class FormSectionInline(admin.TabularInline):
    model = FormSection
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['form', 'heading', 'phase', 'reference']
    inlines = (FormSectionInline,)
