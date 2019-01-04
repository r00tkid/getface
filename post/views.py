# Base rest imports
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Project imports
import time, datetime
from .models import Post
from .factories import PostFactory


@api_view(['GET', 'HEAD'])
@permission_classes([permissions.AllowAny])
def index(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    less = frozenset(["id", "title", "body", "created_at", "updated_at", "author"])

    return Response({
        "posts": [post.to_serialize(less) for post in posts.iterator()],
    })


@api_view(['GET', 'HEAD'])
@permission_classes([permissions.AllowAny])
def fake(request, amount=1):
    start = time.time()
    [PostFactory.create().save() for i in range(amount)]
    end = time.time()

    return Response({
        "message": "Posts has ben created",
        "time": str(datetime.timedelta(seconds=(end - start))),
    }, status=status.HTTP_201_CREATED)


@api_view(['GET', 'HEAD'])
@permission_classes([permissions.AllowAny])
def one(request, post_id=0):
    post = Post.objects.filter(id=post_id).first()

    if not post:
        return Response({
            "message": "Post not found",
        }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        "message": "Post has been found",
        "post": post.to_serialize(frozenset(["id", "title", "body", "created_at", "updated_at", "author"])),
    })
