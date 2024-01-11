from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Projects
from .serializers import ProjectSeralizer

class ProjectList(APIView):

    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSeralizer(projects, many=True)
        return Response(serializer.data)

