from django.contrib import admin
from app1.models import *

# Register your models here.
class InscripcionInline(admin.TabularInline):
	model = Inscripcion
	extra = 1
	verbose_name = "Inscripcion"
	verbose_name_plural = "Inscripciones"

class CursoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'departamento', 'instructor')
	list_filter = ('departamento', 'instructor')
	search_fields = ('titulo',)
	inlines = (InscripcionInline,)

class EntregaInline(admin.TabularInline):
	model = Entrega
	extra = 1
	verbose_name = "Entrega"
	verbose_name_plural = "Entregas"

class TareaAdmin(admin.ModelAdmin):
	list_display = ('curso', 'titulo', 'fecha_entrega')
	list_filter = ('curso', 'fecha_entrega')
	search_fields = ('titulo',)
	inlines = (EntregaInline,)

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)