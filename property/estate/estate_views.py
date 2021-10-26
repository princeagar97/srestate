from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from property.estate.estate_serializers import EstateSerializer, EstateStatusSerializer, EstateTypeSerializer
from property.models import Estate, EstateStatus, EstateType


# Create your views here.
class ListEstateAPIView(ListAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class CreateEstateAPIView(CreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class UpdateEstateAPIView(UpdateAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer

class DeleteEstateAPIView(DestroyAPIView):
    queryset = Estate.objects.all()
    serializer_class = EstateSerializer


class ListEstateStatusAPIView(ListAPIView):
    queryset = EstateStatus.objects.filter(is_deleted = 0)
    serializer_class = EstateStatusSerializer

class CreateEstateStatusAPIView(CreateAPIView):
    queryset = EstateStatus.objects.all()
    serializer_class = EstateStatusSerializer

    def post(self,request):
        serilizer = EstateStatusSerializer(data=request.data)

        if serilizer.is_valid():
            estate_status,created = EstateStatus.objects.get_or_create(
                estate_status_name = serilizer.data["estate_status_name"]
            )
            estate_status.save()

            context = {
                "msg":"Created Successfully"
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                "msg": serilizer.errors
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)



class UpdateEstateStatusAPIView(UpdateAPIView):
    queryset = EstateStatus.objects.all()
    serializer_class = EstateStatusSerializer
    def put(self,request,**kwargs):
        serilizer = EstateStatusSerializer(data=request.data)
        id = kwargs.get('pk',0)
        if serilizer.is_valid():
            try:
                estate_status = EstateStatus.objects.get(pk = id)
                estate_status.estate_status_name = serilizer.data["estate_status_name"]
                estate_status.save()

                context = {
                    "msg":"Updated Successfully"
                }

                return Response(context, status=status.HTTP_200_OK)

            except EstateStatus.DoesNotExist:
                context = {
                    "msg": "Record Does Not Exists"
                }

                return Response(context, status=status.HTTP_200_OK)


        else:
            context = {
                "msg": serilizer.errors
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)

class DeleteEstateStatusAPIView(DestroyAPIView):
    queryset = EstateStatus.objects.all()
    serializer_class = EstateStatusSerializer
    def delete(self,request,**kwargs):
        id = kwargs.get('pk',0)
        try:
            estate_status = EstateStatus.objects.get(pk = id)
            estate_status.is_deleted = True
            estate_status.save()

            context = {
                "msg":"Deleted Successfully"
            }

            return Response(context, status=status.HTTP_200_OK)

        except EstateStatus.DoesNotExist:
            context = {
                "msg": "Record Does Not Exists"
            }

            return Response(context, status=status.HTTP_200_OK)







class ListEstateTypeAPIView(ListAPIView):
    queryset = EstateType.objects.filter(is_deleted = 0)
    serializer_class = EstateTypeSerializer

class CreateEstateTypeAPIView(CreateAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer

    def post(self,request):
        serilizer = EstateTypeSerializer(data=request.data)

        if serilizer.is_valid():
            estate_type,created = EstateType.objects.get_or_create(
                type_name = serilizer.data["type_name"]
            )
            estate_type.save()

            context = {
                "msg":"Created Successfully"
            }

            return Response(context, status=status.HTTP_200_OK)

        else:
            context = {
                "msg": serilizer.errors
            }

            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class UpdateEstateTypeAPIView(UpdateAPIView):
    queryset = EstateType.objects.all()
    serializer_class = EstateTypeSerializer
    def put(self,request,**kwargs):
        serilizer = EstateTypeSerializer(data=request.data)
        id = kwargs.get('pk',0)
        if serilizer.is_valid():
            try:
                estate_type = EstateType.objects.get(pk = id)
                estate_type.type_name = serilizer.data["type_name"]
                estate_type.save()

                context = {
                    "msg":"Updated Successfully"
                }

                return Response(context, status=status.HTTP_200_OK)

            except EstateType.DoesNotExist:
                context = {
                    "msg": "Record Does Not Exists"
                }

                return Response(context, status=status.HTTP_200_OK)

        else:
            context = {
                "msg": serilizer.errors
            }

            return Response(context, status=status.HTTP_201_CREATED)

class DeleteEstateTypeAPIView(DestroyAPIView):
    queryset = EstateStatus.objects.all()
    serializer_class = EstateStatusSerializer
    def delete(self,request,**kwargs):
        id = kwargs.get('pk','0')
        try:
            estate_type = EstateType.objects.get(pk = id)
            estate_type.is_deleted = 1
            estate_type.save()

            context = {
                "msg":"Deleted Successfully"
            }

            return Response(context, status=status.HTTP_200_OK)

        except EstateType.DoesNotExist:
            context = {
                "msg": "Record Does Not Exists"
            }

            return Response(context, status=status.HTTP_200_OK)





