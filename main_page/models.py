from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator




class Books(models.Model):
    GENRE_CHOICE = (
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Детские', 'Детские')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку',null=True)
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Напишите описание книги', default='Lorem Ipsum')
    price = models.FloatField(verbose_name='Укажите цену книги')
    date_published = models.DateField(verbose_name='Укажите дату публикации книги')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Детектив',verbose_name='Укажите жанр книги',null=True)
    pages = models.CharField(max_length=50, verbose_name='Укажите количество страниц в книге')
    author = models.CharField(max_length=30, verbose_name='Укажите автора книги')
    audio_book = models.URLField(verbose_name='Укажите ссылку на аудио-книгу')
    created_at = models.DateTimeField(auto_now_add=True)
    stock_count = models.PositiveIntegerField(default=0, verbose_name="Количество книг в наличии")

    def reduce_stock(self):
        if self.stock_count > 0:
            self.stock_count -= 1
            self.save()

    def average_rating(self):
        reviews = self.reviews_books.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
            return f'{self.title}-{self.price}$'

class ReviewBooks(models.Model):
    review_books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews_books')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Напишите отзыв о книге',null=True)
    mark = models.PositiveIntegerField(verbose_name='Оцените книгу от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_books}-{self.created_at}'

    class Meta:
        verbose_name = 'Отзыв к книге'
        verbose_name_plural = 'Отзывы к книгам'



