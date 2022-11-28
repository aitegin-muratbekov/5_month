from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def movies_count(self):
        return len(self.movies.all())

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=255, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.SmallIntegerField(default=5)

    def __str__(self):
        return self.text

