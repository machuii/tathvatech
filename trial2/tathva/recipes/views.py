from ast import Delete
from cgitb import reset
from urllib import response
from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from django.utils.text import slugify


# Create your views here.


class RecipeAPIView(APIView):

    def get_object(self,pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
    def get(self,request,pk=None,format=None):
        if pk:
            data=self.get_object(pk)
            serializer=RecipeSerializer(data)
        else:
            data=Recipe.objects.all()
            serializer=RecipeSerializer(data,many=True)

        return Response(serializer.data)


    def post(self,request,format=None):
        serializer=RecipeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.slugs=slugify(serializer.validated_data['name'])


        serializer.save(slugs=self.slugs)
        

        
        response=Response()



        response.data={'message':'Recipe created successfully','data':serializer.data}

        return Response()


    def put(self,request,pk=None,format=None):
        recipe_to_update=self.get_object(pk)
        serializer=RecipeSerializer(instance=recipe_to_update,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response=Response()


        response.data={'message':'Recipe updated successfully','data':serializer.data}

        return Response()

    def delete(self,request,pk=None,format=None):
        recipe_to_delete=self.get_object(pk)
        recipe_to_delete.delete()


        return Response({'message':'Recipe deleted successfully'})