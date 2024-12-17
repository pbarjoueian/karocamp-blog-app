from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "body",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("id", "created_at", "updated_at")
    list_filter = ("author", "title")


admin.site.register(Post, PostAdmin)
