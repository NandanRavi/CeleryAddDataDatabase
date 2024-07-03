from django.views import View
from django.http import HttpResponse
from .tasks import update_books_ratings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Books
from .serializers import BookSerializers
from django.core.paginator import Paginator
import datetime
from django.shortcuts import get_object_or_404
import time
# Create your views here.

class UpdatedData(APIView):
    def post(self, request, pk):
        notify = get_object_or_404(Books, id=pk)
        notify.updated_at=datetime.now()
        notify.save()
        return Response({'status': 'Books Updated successfully'})


class BooksView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                book = Books.objects.get(pk=pk)
                serializer = BookSerializers(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Books.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            books = Books.objects.order_by('id')
            paginator = Paginator(books, 20)
            page_number = request.GET.get('page')
            page_objects = paginator.get_page(page_number)
            serializer = BookSerializers(page_objects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, pk=None):
        if pk:
            try:
                book = Books.objects.get(pk=pk)
            except Books.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            book = None
        serializer = BookSerializers(data=request.data, instance=book)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK if pk else status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class TriggerRatingUpdateView(View):
    def get(self, request, *args, **kwargs):
        start_id = kwargs.get('start_id', 100)
        a=update_books_ratings.delay(start_id)
        print(200)
        b=update_books_ratings.delay(200)
        # print(a)
        # print(start_id)
        return HttpResponse(f"Start id {start_id}")



