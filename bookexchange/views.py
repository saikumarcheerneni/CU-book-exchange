# # bookexchange/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Textbook
from .serializer import TextbookSerializer

class TextbooksByCourseView(APIView):
    def get(self, request, course_code, format=None):
        textbooks = Textbook.objects.filter(course_code=course_code)
        if textbooks.exists():
            serializer = TextbookSerializer(textbooks, many=True)
            return Response(serializer.data)
        return Response({"detail": "No textbooks found for this course."}, status=status.HTTP_404_NOT_FOUND)


