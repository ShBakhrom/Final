from django.db import models
from slugify import slugify
# # Create your models here.
class Quote(models.Model):
    fistName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)

    def __str__(self):
       return str(self.id)

def get_image_filename(instance, filename):
    title = str(instance.quote.id)
    slug = slugify(title)
    return "index/static/upload/upload/%s-%s" % (slug, filename)  


class Images(models.Model):
    quote = models.ForeignKey(Quote, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')
                              
    def __str__(self):
       return str(self.quote.id)
