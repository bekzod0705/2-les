from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import TodoModel
from rest_framework.response import Response
from .permissions import StaffPermissionClass,AdminPermissionClass
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# class CreateApiView(APIView):
#     def post(self,request):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==2:
#                 serializer=TodoSerializer(data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'only for staffs'})
class CreateApiView(generics.CreateAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,StaffPermissionClass)
        
# class ListApiView(APIView):
#     def get(self,request):
#         print(request.user)
#         if str(request.user)=='AnonymousUser':
#             return Response({'msg':'log in !!'})
#         all=TodoModel.objects.filter(status=True)
#         serializer=TodoSerializer(all,many=True)
#         return Response(serializer.data)
class ListApiView(generics.ListAPIView):
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,)
    def get_queryset(self):
        return TodoModel.objects.filter(status=True)

# class UpdateStatus(APIView):
#     def patch(self,request,*args,**kwargs):
#         if str(request.user)!='AnonymousUser':
#             if request.user.roles==3:
#                 news=get_object_or_404(TodoModel,id=kwargs['news_id'])
#                 serializer=TodoSerializer(news,data=request.data,partial=True)
#                 if serializer.is_valid():
#                     serializer.save()(
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#         else:
#             return Response({'msg':'only admins can change'})
class UpdateStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset=TodoModel.objects.all()
    serializer_class=TodoSerializer
    permission_classes=(IsAuthenticated,AdminPermissionClass)