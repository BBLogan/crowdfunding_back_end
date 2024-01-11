from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSeralizer
from django.http import Http404
from rest_framework import status

class ProjectList(APIView):

    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSeralizer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSeralizer(project)
        return Response(serializer.data)