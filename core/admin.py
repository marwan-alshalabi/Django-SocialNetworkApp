from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('caption'),
# Register your models here.
admin.site.register(User)
admin.site.register(Post,PostAdmin)
admin.site.register(Friends)
