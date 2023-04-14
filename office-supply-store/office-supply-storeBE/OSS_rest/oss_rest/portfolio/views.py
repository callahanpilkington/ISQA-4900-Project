# from rest_framework import status, generics
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# from .serializers import *
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny



# @csrf_exempt
# @api_view(['GET', 'POST'])
# def inventory_list(request):
#     permission_classes = (IsAuthenticatedOrReadOnly)
#     if request.method == 'GET':
#         inventory = Inventory.objects.all()
#         serializer = InventorySerializer(inventory, context={'request': request}, many=True)
#         return Response({'data': serializer.data})

#     elif request.method == 'POST':
#         serializer = InventorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getInventory(request, pk):
#     """
#     Retrieve, update or delete a customer instance.
#     """
#     try:
#         inventory = Inventory.objects.get(pk=pk)
#     except Inventory.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = InventorySerializer(inventory,context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = InventorySerializer(inventory, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         inventory.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# # class RegisterView(generics.CreateAPIView):
# #   queryset = User.objects.all()
# #   permission_classes = (AllowAny,)
# #   serializer_class = RegisterSerializer


from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from .serializers import InventorySerializer
from .models import Inventory

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def inventory_list(request):
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getInventory(request, pk):
    """
    Retrieve, update or delete an inventory instance.
    """
    try:
        inventory = Inventory.objects.get(pk=pk)
    except Inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(inventory, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventorySerializer(inventory, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)