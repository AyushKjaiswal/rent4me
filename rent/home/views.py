from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView, RetrieveAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import render

# class studentAPI_list_create(ListCreateAPIView):
#     queryset = students_Details.objects.all()
#     serializer_class = students_Details_serializer

# class student_update_retrieve_destroy(RetrieveUpdateDestroyAPIView):
#     queryset  = students_Details.objects.all()
#     serializer_class = students_Details_serializer


class Room_list_create(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    # queryset = Room.objects.all()
    serializer_class = RoomSerializer
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Room.objects.all()
        sortby = self.request.query_params.get('sort_by')
        amount = self.request.query_params.get('amount')
        tag_id = self.request.query_params.get('tag_id')
        if sortby == 'asc':
            queryset = queryset.order_by('room_price')
        elif sortby == 'dsc':
            queryset = queryset.order_by('-room_price')
        if amount is not None:
            queryset = queryset.filter(room_price__lte = amount)
        if tag_id is not None:
            tag_id = str(tag_id).split(',')
            ids = []
            for id in tag_id:
                ids.append(int(id))
            queryset = queryset.filter(room_tag__in = ids).distinct()
        return queryset


    
# class Room_list(ListAPIView):
#     serializer_class = RoomSerializer
#     def get_queryset(self):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Room.objects.all()
#         username = self.request.query_params.get('sort_by')
#         if username == 'asc':
#             queryset = queryset.order_by('room_price')
#         elif username == 'dsc':
#             queryset = queryset.order_by('-room_price')
#         return queryset
    