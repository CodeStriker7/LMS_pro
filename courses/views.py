from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

# Bu klass hamma kurslarni JSON qilib qaytaradi
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer