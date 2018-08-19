import os
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.pdf','.doc','.docx']
        if not ext in valid_extensions:
            raise ValidationError('File not supported!')

class FileSys(models.Model):
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/',validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
