import datetime
from django import forms
from .models import Blog


class BlogForm(forms.Form):
    judul = forms.CharField(max_length=255)
    gambar = forms.CharField(max_length=255)
    kategori = forms.CharField(max_length=200)
    deskripsi = forms.CharField(max_length=255)
    tgl_publish = forms.DateField(initial=datetime.date.today)
    tgl_dibuat = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Blog
        fields = (
            "judul",
            "gambar",
            "kategori",
            "deskripsi",
            "tgl_publish",
            "tgl_dibuat",
        )
