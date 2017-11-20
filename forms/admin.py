from django.contrib import admin
from .models import Organisation, Phase, DataType, InputType, Validation, FieldType, Question, Section, Form


admin.site.register(Organisation)
admin.site.register(Validation)
admin.site.register(FieldType)

admin.site.register(Question)
admin.site.register(Section)
admin.site.register(Form)


@admin.register(InputType)
class InputTypeAdmin(admin.ModelAdmin):
        list_display = ['inputtype']


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
        list_display = ('datatype', 'description')


@admin.register(Phase)
class PhaseAdmin(admin.ModelAdmin):
        list_display = ['phase']
