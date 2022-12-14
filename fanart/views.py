from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import BaseImageSerializer
from .serializers import FanartImageSerializer
from .serializers import FanartImageCreateSerializer
from .serializers import FanartImageGetSerializer
from .serializers import FanartSerializer
from .serializers import FanartGetListSerializer
from .serializers import FanartGetSerializer
from .serializers import FanartCommentCreateSerializer
from .serializers import FanartPutSerializer
from rest_framework.response import Response
from rest_framework import status
from .colorization import sketchProcess
from .colorization import colorization
from uuid import uuid4
from .models import FanartImage
from .models import BaseImage
from .models import Fanart
from .models import FanartComment
from django.db.models import Count

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
        print(request.data)
        if serializer.is_valid():
            serializer.save() # resize_image, hint_image 저장
            resize_image = BaseImage.objects.get(id=serializer.data['resize_image']).image.url[1:] # colorization 함수 실행을 위해 resize_image 이름 가져옴
            hint_image = serializer.data['hint_image'][1:] # colorization 함수 실행을 위해 hint_image 이름 가져옴
            print(resize_image, hint_image)
            result_image = colorization(resize_image, hint_image) 
            fanart_image = FanartImage.objects.get(id=serializer.data['id'])
            fanart_image.result_image = result_image
            fanart_image.save()
            return Response(FanartImageGetSerializer(fanart_image).data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            


class FanartListView(APIView):
    def post(self, request):
        serializer = FanartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        serializer_list = []
        fanart = Fanart.objects.all()
        serializer = FanartGetListSerializer(fanart, many=True)
        serializer_list.append(serializer.data)
        fanart_likes = Fanart.objects.annotate(like_count=Count('likes')).order_by('-like_count')
        serializer_likes = FanartGetListSerializer(fanart_likes,many=True)
        serializer_list.append(serializer_likes.data)
        return Response(serializer_list,status=status.HTTP_200_OK)

class FanartWebtoonListView(APIView):
    def get(self, request, webtoon_id):
        serializer_list = []
        fanart = Fanart.objects.filter(webtoon_id=webtoon_id)
        serializer = FanartGetListSerializer(fanart, many=True)
        serializer_list.append(serializer.data)
        fanart_likes = Fanart.objects.all()
        serializer_likes = FanartGetListSerializer(fanart_likes,many=True)
        serializer_list.append(serializer_likes.data)
        return Response(serializer_list,status=status.HTTP_200_OK)

class FanartView(APIView):

    def get(self, request, fanart_id):
        print(fanart_id)
        print(type(fanart_id))
        fanart = Fanart.objects.get(id=fanart_id)
        print(fanart)
        serializer = FanartGetSerializer(fanart)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, fanart_id):
        fanart = Fanart.objects.get(id=fanart_id)
        fanart.delete()
        return Response("삭제완료",status=status.HTTP_200_OK)

class FanartCommentView(APIView):
    def post(self, request, fanart_id):
        serializer = FanartCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(fanart_id=fanart_id,user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, fanart_id, comment_id):
        comment = FanartComment.objects.get(id=comment_id)
        serializer = FanartPutSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, fanart_id, comment_id):
        comment = FanartComment.objects.get(id=comment_id)
        comment.delete()
        return Response("삭제완료",status=status.HTTP_200_OK)

class FanartLike(APIView):
    def post(self, request, fanart_id):
        fanart = Fanart.objects.get(id=fanart_id)
        print(request.user)
        if request.user in fanart.likes.all():
            fanart.likes.remove(request.user)
            return Response("좋아요 취소 완료!", status=status.HTTP_200_OK)
        else:
            fanart.likes.add(request.user)
            return Response("좋아요 등록 완료!", status=status.HTTP_200_OK)