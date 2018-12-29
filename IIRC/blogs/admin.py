from django.contrib import admin

# Register your models here.
from .models import Post, SignUp, Blog, Author, Entry
from .form import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'timestamp', 'updated']
	form = SignUpForm

	class Meta:
		model = SignUp


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
