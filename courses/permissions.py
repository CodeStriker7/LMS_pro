from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):
	def has_permissin(self, request, view):
		if request.method in permissins_SAFE_METHODS:
			return True
		# O'zgartirish (POST, PUT, DELETE) uchun foydalanuvchi teacher bo'lishi shart
		return bool(request.user and request.user.is_authentificated and request.user.is_teacher)


