

from http.client import ResponseNotReady
from rest_framework.views import APIView
from .serializers import MembershipSerializer
from django.shortcuts import render, HttpResponse
from .models import Membership
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status, generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Membership
from django.http import HttpResponse
from django.template import context, loader



class MembershipViewSet(viewsets.ModelViewSet):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer



def  index(request):
    New_Members=Membership.objects.order_by('-FullName')[:5]
    template=loader.get_template('dlfnepal/index.html')
    context={
        'new_members':New_Members,
    }
    return HttpResponse(template.render(context,request))
    



'''
class MembershipViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer

'''






'''
class MembershipViewSet(viewsets.ViewSet):
    def  list(self, request):
        members=Membership.objects.all()
        serializer=MembershipSerializer(members, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer=MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset=Membership.objects.all()
        member=get_object_or_404(queryset, pk=pk)
        serializer= MembershipSerializer(member)
        return Response(serializer.data)

    def update(self, request, pk=None):
        member=Membership.objects.get(pk=pk)
        serializer=MembershipSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        member=Membership.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        



class MembershipList(generics.GenericAPIView, mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
        


class MembershipDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=Membership.objects.all()
    serializer_class=MembershipSerializer

    lookup_field='id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)    
        '''
