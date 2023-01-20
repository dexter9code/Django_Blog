from django.db import models


class Tag(models.Model):
    caption = models.CharField('Tag Name', max_length=50)

    def __str__(self) -> str:
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField('image', max_length=255)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, db_index=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag)
