from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Author

# Define an inline admin descriptor for Author model
# which acts a bit like a singleton
class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)