from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Rating
from .serializers import RatingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics, status


class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }

        return Response(data)


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get_object_or_404(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Successfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "Message": "Book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class RatingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)