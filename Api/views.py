from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
# Models
from . import models
# Serializers
from. import serializers
# 

class UserList(APIView):
    @swagger_auto_schema(responses={200: serializers.UserSerializer(many=True)})
    def get(self, request):
        users = models.User.objects.all()
        user_serializer = serializers.UserSerializer(users, many=True)

        return Response(
            user_serializer.data, 
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=serializers.UserSerializer)
    def post(self, request):
        try:
            user_serializer = serializers.UserSerializer(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                
                return Response(
                    {'success': user_serializer.data}, 
                    status=status.HTTP_201_CREATED
                )
            
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserRead(APIView):
    @swagger_auto_schema(responses={200: serializers.UserSerializer()})
    def get(self, request, pk):
        try:
            user = models.User.objects.get(pk=pk)
            user_serializer = serializers.UserSerializer(user)

            return Response(
                user_serializer.data,
                status=status.HTTP_200_OK
            )
        
        except Exception as err:
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QueuesList(APIView):
    @swagger_auto_schema(responses={200: serializers.QueueSerializer()})
    def get(self, request):
        queues = models.Queue.objects.all()
        queue_serializer = serializers.QueueSerializer(queues, many=True)

        return Response(queue_serializer.data, status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializers.QueueSerializer)
    def post(self, request):
        try:
            queue_serializer = serializers.QueueSerializer(data=request.data)
            if queue_serializer.is_valid():
                queue_serializer.save()

                return Response(
                    {'success': queue_serializer.data},
                    status=status.HTTP_201_CREATED
                )

        except Exception as err:
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QueueRead(APIView):
    @swagger_auto_schema(request_body=serializers.QueueSerializer)
    def patch(self, request, pk):
        try:
            queue = models.Queue.objects.get(pk=pk)
            queue_serializer = serializers.QueueSerializer(queue, data=request.data)
            if queue_serializer.is_valid():
                queue_serializer.save()

                return Response(
                    {'Instance Updated': queue_serializer.data},
                    status=status.HTTP_202_ACCEPTED
                )

        except Exception as err:
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ServicesList(APIView):
    @swagger_auto_schema(responses={200: serializers.ServicesSerializer(many=True)})
    def get(self, request):
        services = models.Services.objects.all()
        service_serializer = serializers.ServicesSerializer(services, many=True)

        return Response(
            service_serializer.data,
            status=status.HTTP_200_OK
        )

    @swagger_auto_schema(request_body=serializers.ServicesSerializer)
    def post(self, request):
        try:
            service_serializer = serializers.ServicesSerializer(data=request.data)
            if service_serializer.is_valid():
                service_serializer.save()
                
                return Response(
                    {'success': service_serializer.data}, 
                    status=status.HTTP_201_CREATED
                )
            
            return Response(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
