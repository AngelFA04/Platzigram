"""User admin classes."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

#Models
from users.models import Profile

# Register your models here.
## Forma 1 de registrar los perfiles en el admin
## admin.site.register(Profile)

## Forma 2
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"Profile admin"""
    
    list_display = ('pk','user', 'phone_number', 'website', 'biography' ,'picture', )
    list_display_links = ("user",'phone_number')
    list_editable = []
    search_fields = ['user__email']

    list_filter = ['created', 'modified','user', 'user__is_active']
    pass

    fieldsets=(
        ('Profile', {
            'fields':(
                ('user', 'picture'),
                ),
        }),
        ('Extra info', {
            'fields':(
            ('website', 'phone_number'),
            ('biography'), 
            )
        }),
        ('Metadata',{
            'fields':(
                ('created', 'modified'),
            )
        }),
    )

    readonly_fields =('created', 'modified', 'user')


class ProfileInline(admin.StackedInline):
    """Profile in-line for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)