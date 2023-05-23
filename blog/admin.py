from django.contrib import admin
from .models import Blog
from django.utils.html import mark_safe


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("judul", "kategori", "gambar_preview", "tgl_publish", "tgl_dibuat")
    readonly_fields = ["gambar_preview"]

    def gambar_preview(self, obj):
        return mark_safe(
            '<img src="{url}" width={width} height={height} />'.format(
                url=obj.gambar_url, width=300, height=300
            )
        )


admin.site.register(Blog, BlogAdmin)
