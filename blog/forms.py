import datetime
from django import forms
from .models import Blog


class BlogForm(forms.Form):
    judul = forms.CharField(max_length=255)
    gambar = forms.ImageField()
    kategori = forms.CharField(max_length=200)
    deskripsi = forms.CharField(max_length=255)
    tgl_publish = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={"type": "date", "placeholder": "yyyy-mm-dd (DOB)"},
        )
    )

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
