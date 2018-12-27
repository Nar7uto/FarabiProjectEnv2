from django.contrib import admin

# Register your models here.
from .models import Post, SignUp
from .form import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp', 'updated']
	form = SignUpForm

	class Meta:
		model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Post)
