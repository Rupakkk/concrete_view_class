from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# class StudentList(ListAPIView,CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentUpdate(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class ListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateRetrieveDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
