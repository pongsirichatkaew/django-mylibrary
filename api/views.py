from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from listings.models import Listing, Author
from api.serializers import *
from rest_framework import generics
import json


class BookDetail(View):
    def get(self, request, id):
        book = get_object_or_404(Listing, pk=id)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)


class BookList(generics.ListCreateAPIView):
    def get(self, request):
        books = Listing.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)


class AuthorList(generics.ListCreateAPIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, **kwargs):
        data = request.data
        if 'photo' not in request.FILES:
            response = JsonResponse(
                {'status': '401', 'message': 'PLEASE ADD PHOTO'}, status=401)
        elif 'name' not in data or 'phone' not in data or 'email' not in data:
            response = JsonResponse(
                {'status': '401', 'message': 'PLEASE FILL ALL THE DATA'}, status=401)
        else:
            photo = request.FILES['photo']
            name = data['name']
            phone = data['phone']
            email = data['email']
            if 'description' in data:
                description = data['description']
            new_author = Author(
                name=name, photo=photo, description=description, phone=phone, email=email)
            new_author.save()
            response = JsonResponse(
                {'status': '200', 'message': 'CREATE SUCCESS'}, status=200)

        return response


class AuthorDetail(generics.ListCreateAPIView):
    def get(self, request, id):
        author = get_object_or_404(Author, id=id)
        serializer = AuthorSerializer(author)
        return JsonResponse(serializer.data)

    def put(self, request, id, **kwargs):
        data = request.data
        author = get_object_or_404(Author, id=id)
        if 'photo' not in request.FILES:
            response = JsonResponse(
                {'status': '401', 'message': 'PLEASE ADD PHOTO'}, status=401)
        elif 'name' not in data or 'phone' not in data or 'email' not in data:
            response = JsonResponse(
                {'status': '401', 'message': 'PLEASE FILL ALL THE DATA'}, status=401)
        else:
            author.photo = request.FILES['photo']
            author.name = data['name']
            author.phone = data['phone']
            author.email = data['email']
            if 'description' in data:
                author.description = data['description']
            author.save()
            response = JsonResponse(
                {'status': '200', 'message': 'UPDATE SUCCESS'}, status=200)

        return response

    def delete(self, request, id, **kwargs):
        author = get_object_or_404(Author, id=id)
        response = JsonResponse(
            {'status': '200', 'message': 'UPDATE SUCCESS'}, status=200)
        author.delete()
        return response
