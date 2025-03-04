# bookexchange/urls.py
from django.urls import path
from .views import TextbooksByCourseView

urlpatterns = [
    path('textbooks/<str:course_code>/', TextbooksByCourseView.as_view(), name='textbooks_by_course'),
]




