from django.db import models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)
    kategori = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tgl_publish = models.DateField()
    tgl_dibuat = models.DateField()

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.judul