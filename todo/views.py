from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Books
from .serializers import BookSerializer
from .permissions import IsSuperUserOrReadOnly,IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# here is we are using generic view
class BookList(APIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]

    # to retrieve a list of books
    def get(self,request):
        books = Books.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    # to create a new book
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

class BookListIV(APIView):

    permission_classes = [IsAuthenticated,IsSuperUserOrReadOnly]

    def get(self,request,pk):

        # Retrieve a specific book by its primary key.
        try:
            book = Books.objects.get(pk=pk)

        except Books.DoesNotExist:
            return Response({'Error' : 'Book Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self,request, pk):

        #  Update a specific book by its primary key.
        book = Books.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, pk):

        #   Delete a specific book by its primary key..
        book =Books.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)