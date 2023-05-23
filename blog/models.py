from django.db import models
from django.conf import settings


# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255)
    gambar = models.ImageField(upload_to="foto/", null=True)
    kategori = models.CharField(max_length=200)
    deskripsi = models.TextField()
    tgl_publish = models.DateField()
    tgl_dibuat = models.DateField()

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.judul

    # Tambahkan kode dibawah ini jika gambar tidak muncul
    @property
    def gambar_url(self):
        return "%s%s" % (settings.MEDIA_HOST, self.gambar.url) if self.gambar else ""
