from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Student
from .serializer import StudentSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/',
        'GET api/student',
        'GET api/student/ :id'

    ]
    return Response(routes)


@api_view(['GET'])
def getStudents(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStudent(request, id):

    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)