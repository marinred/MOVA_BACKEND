from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BaseImageSerializer
from .serializers import FanartImageSerializer
from .serializers import FanartImageCreateSerializer
from .serializers import FanartImageGetSerializer
from .serializers import FanartSerializer
from .serializers import FanartGetListSerializer
from rest_framework.response import Response
from rest_framework import status
from .colorization import sketchProcess
from .colorization import colorization
from uuid import uuid4
from .models import FanartImage
from .models import BaseImage
from .models import Fanart

# Create your views here.
class BaseImageView(APIView):
    def post(self,request):
        serializer = BaseImageSerializer(data=request.data)

        # origin 이미지 저장
        base_image = request.FILES['image']
        path = "media/fanart/origin/"
        img_name = uuid4().hex + '.png'
        img_dir = path + img_name
        data = base_image.file.read()
        with open(img_dir, 'wb') as f:
            f.write(data)

        if serializer.is_valid():
            image_url = sketchProcess(img_name)
            serializer.save(image=image_url)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data,status=status.HTTP_200_OK)

class ColorizationView(APIView):
    def post(self, request):
        serializer = FanartImageSerializer(data=request.data) # resize_image, hint_image 불러와서
        if serializer.is_valid():
            serializer.save() # resize_image, hint_image 저장
            resize_image = BaseImage.objects.get(id=serializer.data['resize_image']).image.name # colorization 함수 실행을 위해 resize_image 이름 가져옴
            hint_image = serializer.data['hint_image'][1:] # colorization 함수 실행을 위해 hint_image 이름 가져옴
            result_image = colorization(resize_image, hint_image) 
            fanart_image = FanartImage.objects.get(id=serializer.data['id'])
            fanart_image.result_image = result_image
            fanart_image.save()
            return Response(FanartImageGetSerializer(fanart_image).data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

class FanartView(APIView):
    def post(self, request):
        serializer = FanartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        fanart = Fanart.objects.all()
        serializer = FanartGetListSerializer(fanart, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)