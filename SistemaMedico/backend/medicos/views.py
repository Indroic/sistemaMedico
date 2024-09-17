from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import MedicoSerializer
from .models import Medico


class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]
    
    
    def list(self, request, *args, **kwargs):
        medicos = Medico.objects.all().filter(agregado_por=self.request.user)
        
        return Response({"medicos": MedicoSerializer(medicos, many=True).data})
    
