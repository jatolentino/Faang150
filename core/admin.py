from django.contrib import admin

# Register your models here.
from .models import User, Membership, Payment, File, TrackedRequest

admin.site.register(User)
admin.site.register(Membership)
admin.site.register(Payment)
admin.site.register(File)
admin.site.register(TrackedRequest)
