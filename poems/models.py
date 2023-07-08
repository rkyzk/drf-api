from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


CATEGORY = (('nature', 'nature'),
            ('love', 'love'),
            ('people', 'people'),
            ('humor', 'humor'),
            ('self', 'self'),
            ('haiku', 'haiku'),
            ('other', 'other'))


class Poem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY,
                                default='other')
    published = models.BooleanField(default=False)
    featured_flag = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        If the poem is newly published, set published_at.
        """
        if self.published and not self.published_at:
            self.published_at = datetime.utcnow()
        super().save(*args, **kwargs)
