from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    CategorySerializer, CommentSerializer, GenreSerializer,
    ReviewSerializer, TitleSerializer
)
from reviews.models import (
    Category, Genre, Review, Title
)


# POST, GET(list), DEL методы, остальные запрещены
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = ()


# POST, GET(list, single), DEL, PUT, PUTCH методы, остальные запрещены
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = ()

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            review=get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        )


# POST, GET(list), DEL методы, остальные запрещены
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = ()


# POST, GET(list, single), DEL, PUT, PUTCH методы, остальные запрещены
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = ()

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            title=get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        )


# POST, GET(list, single), DEL, PUT, PUTCH методы, остальные запрещены
class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = ()


# Дописать как появится переписанный юзер
class UserViewSet(ModelViewSet):
    pass
