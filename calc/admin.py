from django.contrib import admin
from .models import Status, Subject, Category, Cource, Cource_Subject, User, Department


admin.site.register(Status)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Cource)
admin.site.register(Cource_Subject)
admin.site.register(User)
admin.site.register(Department)
