import Faker as f

# fake = f('it_IT')
# for _ in range(10):
#     print(fake.book())

from myapp.models import Book

class BookFactory(factory.Factory):
    class Meta:
        model = Book

    title = factory.f('sentence', nb_words=4)
    author_name = factory.f('name')