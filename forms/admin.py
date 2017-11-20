from django.contrib import admin
from .models import Organisation, Phase, DataType, InputType, Validation, Field, Question, Section, Form, FormSection


admin.site.register(Organisation)
admin.site.register(Validation)
admin.site.register(Field)

admin.site.register(Question)
admin.site.register(Section)


class FormSectionInline(admin.TabularInline):
    model = FormSection
    extra = 1


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ['form', 'phase', 'reference', 'name', 'description']
    inlines = (FormSectionInline,)


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
    list_display = ['inputtype']


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('datatype', 'description')


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ['phase']
