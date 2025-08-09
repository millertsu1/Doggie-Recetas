from django.contrib import admin
from .models import Receta, Paso, Ingrediente, Tips, Paciente

# Inline model para los pasos de la receta
class PasoInline(admin.TabularInline):
    model = Paso
    extra = 1  # Muestra un formulario vacío para agregar pasos (si se desea)

# Registro del modelo Receta
class RecetaAdmin(admin.ModelAdmin):
    inlines = [PasoInline]  # Los pasos aparecerán dentro de Receta
    list_display = ('nombre', 'tiempo_preparacion', 'porciones', 'activa', 'created', 'updated')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('created',)

# Registro de los otros modelos
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'created', 'updated')
    search_fields = ('nombre',)

class TipsAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'receta', 'created', 'updated')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('created',)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'peso', 'altura', 'enfermedades', 'alergias', 'created', 'updated')
    search_fields = ('nombre', 'enfermedades', 'alergias')
    list_filter = ('created',)

# Registro de los modelos en el admin
admin.site.register(Receta, RecetaAdmin)
admin.site.register(Paso)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Tips, TipsAdmin)
admin.site.register(Paciente, PacienteAdmin)    
