# recetas/models.py
from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    beneficios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    CATEGORIAS = [
        ('desayuno', 'Desayuno'),
        ('almuerzo', 'Almuerzo'),
        ('cena', 'Cena'),
        ('snack', 'Snack'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='desayuno')
    porciones = models.IntegerField(help_text="Cantidad de porciones", default=1)
    imagen = models.ImageField(upload_to='imagenes_recetas/', blank=True, null=True)
    activa = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Tips(models.Model):
    patient_photo = models.ImageField(upload_to='tips_photos/', blank=True, null=True) 
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='tips', default=1)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tip"
        verbose_name_plural = "Tips"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class Paso(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='pasos')  # Relación con Receta
    descripcion = models.TextField()
    orden = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Paso"
        verbose_name_plural = "Pasos"
        ordering = ["orden"]

    def __str__(self):
        return f"{self.orden}: {self.descripcion[:20]}"

""" modelo de crear paciente """

class Paciente(models.Model):
    imagen = models.ImageField(upload_to='imagenes_pacientes/', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    peso = models.FloatField()
    altura = models.FloatField()
    enfermedades = models.TextField()
    alergias = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

""" modelo de crear veterinario """

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    experiencia = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

""" modelo de crear cita """