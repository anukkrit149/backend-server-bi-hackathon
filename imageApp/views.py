from imageApp.models import images_caption
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from imageApp.serializer import imagePostSerializer
from django_q.tasks import async_task


class get_images(generics.ListAPIView):
    queryset = images_caption.objects.filter(caption__isnull=False, keyword__isnull=False)
    serializer_class = imagePostSerializer
    model = images_caption
    paginate_by = 1
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class upload_image(APIView):
    def post(self, request):
        images_captionObj = images_caption.objects.create(image=request.FILES['image'])
        data = {
            "status":status.HTTP_201_CREATED,
            "msg" : "Image id is {}".format(images_captionObj.image_id)
        }
        async_task("imageApp.tasks.ml_model", images_captionObj.image_id, images_captionObj.image)
        return Response(status=status.HTTP_201_CREATED, data=data)


class webhook_image(APIView):
    def post(self, request):
        postObj = images_caption.objects.get(image_id=int(request.POST['image_id']))
        postObj.caption = request.POST['caption']
        postObj.keyword = request.POST['keywords'].split(',')
        postObj.save()
        return Response(status=status.HTTP_200_OK, data={
            "status": status.HTTP_200_OK,
            "msg": "image-caption updated"
        })


class search(APIView):
    def get(self, request):
        status_code = status.HTTP_200_OK
        # print(request.GET['image_id'])
        if ('image_id' in request.GET) and (request.GET['image_id'] is not None):
            posts = imagePostSerializer(images_caption.objects.get(image_id=request.GET['image_id']))
        elif ('keyword' in request.GET) and (request.GET['keyword'] is not None):
            posts = imagePostSerializer(images_caption.objects.filter(keyword__in=request.GET['keyword']),
                                        many=True)
        else:
            posts = None
            status_code = status.HTTP_404_NOT_FOUND
        # data = {
        #     "status": status_code,
        #     "data":posts
        # }
        return Response(status=status_code, data=posts.data)