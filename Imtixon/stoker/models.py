from django.db import models



class Services(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=50)
    image = models.URLField(null=True)
    description = models.TextField()
    seen = models.PositiveSmallIntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title


class Advisers(models.Model):
    slug = models.SlugField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    level = models.CharField(max_length=50)
    email = models.EmailField()
    seen = models.PositiveSmallIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.first_name


class Clients(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    image = models.URLField(null=True)
    email = models.EmailField()
    phone = models.PositiveIntegerField(unique=True, null=True, blank=True)
    seen = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.first_name


class Features(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    seen = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Comments(models.Model):
    service = models.ManyToManyField(Services)
    comment = models.TextField()
    client = models.ManyToManyField(Clients)
    seen = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['id']


def __str__(self):
    return self.comment


class FAQs(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question
