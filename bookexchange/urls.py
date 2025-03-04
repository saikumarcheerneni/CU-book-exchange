from django.urls import path
from . import views

urlpatterns = [

    path('textbooks/<str:course_code>/', views.textbooks_by_course, name='textbooks_by_course'),
]



