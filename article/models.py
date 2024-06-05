from django.db import models

# Create your models here.
# Author title content created_date >> Article


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=150, verbose_name="Başlıq")  # input

    created_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="Article Images",blank=True, null=True,verbose_name="Şəkil")

    def __str__(self):
        return f"{self.title} | {self.author}"

    
    
