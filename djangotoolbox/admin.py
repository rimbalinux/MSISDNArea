from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser')

class CustomUserAdmin(UserAdmin):
    fieldsets = None
    form = UserForm

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)

class CustomGroupAdmin(GroupAdmin):
    fieldsets = None
    form = GroupForm


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
#admin.site.register(Group, CustomGroupAdmin)
