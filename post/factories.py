from factory import Factory, Faker
from .models import Post


class PostFactory(Factory):
    class Meta:
        model = Post

    title = Faker('sentence', nb_words=4)
    body = Faker('sentence', nb_words=80)
    author_id = 1
