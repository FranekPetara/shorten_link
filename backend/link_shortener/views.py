import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Link
from .serializers import LinkSerializer
import secrets



class ShortenLinkAPIView(APIView):
    def post(self, request):
        try:
            serializer = LinkSerializer(data=request.data)
            if serializer.is_valid():
                original_url = serializer.validated_data['original_url']

                link = Link.objects.filter(original_url=original_url).first()
                if link:
                    return Response({'short_url': link.short_url}, status=status.HTTP_200_OK)

                hash_length = int(os.environ["HASH_LENGTH"])
                short_url = f'https://center.ai/{secrets.token_urlsafe(hash_length)}'
                link = Link.objects.create(original_url=original_url, short_url=short_url)
                
                last_three_links = Link.objects.order_by('-created_at')[:3]
                last_three_links_data = [{'original_url': item.original_url, 'short_url': item.short_url} for item in last_three_links]
                
                response_data = {'short_url': link.short_url, 'last_three_links': last_three_links_data}
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

