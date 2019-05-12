from django.contrib import admin

# Register your models here.
from .models import Posts, AllComment

admin.site.register(Posts)
admin.site.register(AllComment)