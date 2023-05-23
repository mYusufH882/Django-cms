import datetime
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


# Create your views here.
def IndexView(request):
    blogs = Blog.objects.all()

    return render(request, "index.html", {"blogs": blogs})


def CreateView(request):
    form = BlogForm

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            judul = form.cleaned_data["judul"]
            gambar = form.cleaned_data["gambar"]
            kategori = form.cleaned_data["kategori"]
            deskripsi = form.cleaned_data["deskripsi"]
            tgl_publish = form.cleaned_data["tgl_publish"]

            Blog.objects.create(
                judul=judul,
                gambar=gambar,
                kategori=kategori,
                deskripsi=deskripsi,
                tgl_publish=tgl_publish,
                tgl_dibuat=datetime.datetime.now(),
            )

            messages.success(request, "Blog berhasil dibuat!!!")
            return redirect("index")
    else:
        form = BlogForm()

    return render(request, "form.html", {"form": form})


def EditView(request, id_blog):
    try:
        blog = Blog.objects.get(pk=id_blog)
    except:
        raise HttpResponse("Blog tidak ditemukan!!!")

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog.judul = form.cleaned_data["judul"]
            blog.gambar = form.cleaned_data["gambar"]
            blog.kategori = form.cleaned_data["kategori"]
            blog.deskripsi = form.cleaned_data["deskripsi"]
            blog.tgl_publish = form.cleaned_data["tgl_publish"]
            blog.save()

            messages.success(request, "Blog berhasil diperbaharui!!!")
            return redirect("index")

    else:
        form = BlogForm(
            initial={
                "judul": blog.judul,
                "gambar": blog.gambar,
                "kategori": blog.kategori,
                "deskripsi": blog.deskripsi,
                "tgl_publish": blog.tgl_publish,
            }
        )

    return render(request, "form.html", {"form": form})


def DeleteData(request, id_blog):
    try:
        blog = Blog.objects.get(pk=id_blog)

        if len(blog.gambar) > 0:
            os.remove(blog.gambar.path)
        blog.delete()

        messages.success(request, "Blog berhasil dihapus!!!")
        return redirect("index")

    except Blog.DoesNotExist:
        raise ("Blog tidak ditemukan!!!")
