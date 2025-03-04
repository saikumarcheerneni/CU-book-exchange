from django.contrib import admin
from bookexchange.models import Textbook
# This is for Registering the Textbook model to make it available in the admin interface
admin.site.register(Textbook)
