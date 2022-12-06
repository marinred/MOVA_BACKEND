from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BaseImageSerializer
from rest_framework.response import Response
from rest_framework import status
from .colorization import sketchProcess
from uuid import uuid4

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

