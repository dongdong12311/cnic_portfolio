

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



    
class Algorithm(models.Model):
    algo_name = models.CharField(max_length=300)
    
    algo_author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    update_time = models.DateField(blank=True, null=True)
    STATUS_CHOICES = (('gp','股票'), ('zq','债券'),('jj','基金'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='gp')
    algo_content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    initial_capital = models.CharField(max_length=20, db_index=True)
    
    
    class Meta:
        ordering = ("-update_time",)  # publish的倒序排序。此处是元祖，不要忘写后面的逗号

    def __str__(self):
        return self.algo_name  # 对应后台文章列表中的默认显式字段    
    