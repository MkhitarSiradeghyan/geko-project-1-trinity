from rest_framework.generics import RetrieveAPIView
from .models import About
from .serializers import AboutSerializer

class AboutDetailView(RetrieveAPIView):
    serializer_class = AboutSerializer

    def get_object(self):
        # Վերադարձնում է Admin-ում ավելացված առաջին գրանցումը
        return About.objects.first()