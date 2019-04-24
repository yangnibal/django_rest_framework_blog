from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

class Post(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    passage = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    linenos = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(linenos=linenos, full=True, **options)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)
# Create your models here.
