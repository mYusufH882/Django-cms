from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Blog
from .forms import BlogForm

import datetime


# Create your views here.
def IndexView(request):
    blogs = Blog.objects.all()

    return render(request, "index.html", {"blogs": blogs})


def CreateView(request):
    form = BlogForm

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            judul = form.cleaned_data["judul"]
            gambar = form.cleaned_data["gambar"]
            kategori = form.cleaned_data["kategori"]
            deskripsi = form.cleaned_data["deskripsi"]

            Blog.objects.create(
                judul=judul,
                gambar=gambar,
                kategori=kategori,
                deskripsi=deskripsi,
                tgl_publish=datetime.datetime.now(),
                tgl_dibuat=datetime.datetime.now(),
            )

            messages.success(request, "Blog Berhasil Dibuat!!!")
            return redirect("index")
        else:
            form = BlogForm()

    return render(request, "form.html", {"forms": form})


def EditView(request, id_blog):
    try:
        blog = Blog.objects.get(pk=id_blog)
    except Blog.DoesNotExist:
        raise ("Data blog tidak ditemukan!!!")

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            blog.judul = form.cleaned_data["judul"]
            blog.gambar = form.cleaned_data["gambar"]
            blog.kategori = form.cleaned_data["kategori"]
            blog.deskripsi = form.cleaned_data["deskripsi"]
            blog.save()

            messages.success(request, "Blog telah diperbaharui !!!")
            return redirect("index")
    else:
        form = BlogForm(
            initial={
                "judul": blog.judul,
                "gambar": blog.gambar,
                "kategori": blog.kategori,
                "deskripsi": blog.deskripsi,
                "tgl_publish": datetime.datetime.now(),
                "tgl_dibuat": datetime.datetime.now(),
            }
        )

    return render(request, "form.html", {"forms": form})


def DeleteData(request, id_blog):
    try:
        blog = Blog.objects.get(pk=id_blog)
        blog.delete()

        messages.success(request, "Blog Berhasil Dihapus!!!")
        return redirect("index")

    except Blog.DoesNotExist:
        raise ("Data blog tidak ditemukan!!!")
