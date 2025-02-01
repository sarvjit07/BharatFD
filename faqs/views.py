from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request, *args, **kwargs):
        """ Fetch FAQs with optional language translation """
        lang = request.GET.get('lang', 'en')

        # Check cache
        cache_key = f"faqs_{lang}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        # Fetch data from DB
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})

        # Cache the result for 10 minutes
        cache.set(cache_key, serializer.data, timeout=600)

        return Response(serializer.data)
