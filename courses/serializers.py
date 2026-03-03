from rest_framework import serializers
from .models import Category, Course, Lesson

# 1. Kategoriya tarjimoni
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# 2. Darslar tarjimoni
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'content', 'video', 'order']

# 3. Kurslar tarjimoni (Eng asosiysi)
class CourseSerializer(serializers.ModelSerializer):
    # Kurs ichida darslar ro'yxatini ham ko'rsatish uchun:
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'image','lessons', 'created_at']