from django.contrib import admin
from .models import Member
import uuid

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("id", "firstname", "lastname", "joined_date", "slug")
  prepopulated_fields = {"slug": ("firstname", "lastname")}
  
admin.site.register(Member, MemberAdmin)