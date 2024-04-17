from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    cont_eudo = models.TextField()
    data_p = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

