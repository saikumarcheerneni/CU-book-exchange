
from django.shortcuts import render
from .models import Textbook

def textbooks_by_course(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, available=True)

    if textbooks.exists():
        context = {'textbooks': textbooks, 'course_code': course_code}
    else:
        context = {'no_results': True, 'course_code': course_code}
    
    return render(request, 'bookexchange/book_list.html', context)
