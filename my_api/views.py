from rest_framework import serializers,status
from products.serializers import Productserializer,productcreate
from rest_framework.views import APIView
from products.models import Products
from rest_framework.response import Response



class productview(APIView):
    def get(self,request,id=None):
        if id:
       
            product = Products.objects.filter(id = id)

            serializer = Productserializer(product,many = True).data
            
            return Response(serializer,status=status.HTTP_202_ACCEPTED)
        else: 
            
            product = Products.objects.all()

            serializer = Productserializer(product,many = True).data
            
            return Response(serializer,status=status.HTTP_202_ACCEPTED)


    def post(self,request):

        serializer    = productcreate(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer)
        return Response(status=status.HTTP_400_BAD_REQUEST)

        

       
   