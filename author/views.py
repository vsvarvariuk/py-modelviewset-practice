from rest_framework import viewsets
from author.serializers import AuthorSerializer
from author.models import Author


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
