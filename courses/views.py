from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .permissions import IsTeacherOrReadOnly

# Bu klass hamma kurslarni JSON qilib qaytaradi
class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all().order_by('-created_at')
    serializer_class = CourseSerializer

    permission_classes = [permissions.IsAuthenticated, IsTeacherOrReadOnly]

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


