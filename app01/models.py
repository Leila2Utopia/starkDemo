from django.db import models

# Create your models here.
class Book(models.Model):
    nid=models.AutoField(primary_key=True,verbose_name='编号')
    title=models.CharField(max_length=32,verbose_name='名称')
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='价格')

    publish=models.ForeignKey(to='Publish',to_field='nid',on_delete=models.CASCADE)
    authors=models.ManyToManyField(to='Author',)

    def __str__(self):
        return self.title


class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='出版社')
    city=models.CharField(max_length=32)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='作者')
    age=models.IntegerField()

    def __str__(self):
        return self.name