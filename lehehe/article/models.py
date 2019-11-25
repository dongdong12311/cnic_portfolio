

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify

"投资的类型"
class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='article_column', on_delete=models.CASCADE)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column
    
    def __len__(self):
        return True

class AlgoColumn(models.Model):
    #user = models.ForeignKey(User, related_name='algo_column', on_delete=models.CASCADE)
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column    

    def __len__(self):
        return True
class ListToDisplay:
    def __init__(self):
        pass

map_dic = {"title":"模型名称","column":"投资类别",
           "algo_column":"模型类别",
           "initial_capital":"初始资金",
           "start_date":"初始日期",
           "end_date":"结束日期",
           "portfolio":"投资标的",
           "benchmark":"基准标的",
           "balanced_dates":"调仓间隔",
           "expected_return_days":"数据周期",
           "cov_method":"协方差算法",
           "beta":"贝塔值",
           "opt_criterion":"最优化方法",
           "target_risk":"预期风险",
           "target_return":"预期收益",
           "p_matrix":"BL模型P矩阵",
           "q_matrix":"BL模型Q矩阵",
           }
class MyalgoPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="algo")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, related_name="algo_type_column")
    
    algo_column = models.ForeignKey(AlgoColumn, on_delete=models.CASCADE, related_name="algo_column")
    updated = models.DateTimeField(auto_now=True)
    
    initial_capital = models.CharField(max_length=20)
    
    start_date = models.DateField()
    
    end_date =  models.DateField()
    
    portfolio =  models.TextField()
    
    benchmark = models.CharField(max_length=10)
    
    balanced_dates = models.CharField(max_length=30)
    
    expected_return_days = models.CharField(blank=True,max_length=30)
    
    cov_method  = models.CharField(blank=True,max_length=20)

    beta =  models.CharField(blank=True,max_length=30)
    
    opt_criterion = models.CharField(blank=True,max_length=30)
    
    target_risk = models.CharField(blank=True,max_length=30)
    
    target_return =  models.CharField(blank=True,max_length=30)
    # bl_model 的观点矩阵
    p_matrix  = models.TextField(blank=True,)
    q_matrix  = models.TextField(blank=True,)
    
    class Meta:
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)    
    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(MyalgoPost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:myalgo_detail", args=[self.id, self.slug])  
    
    
    def get_attrs_that_is_not_None(self):
        result = []
        for data in map_dic.keys():
            temp = getattr(self,data)
            if temp:
                res = ListToDisplay()
                res.first = map_dic[data]
                res.second = temp
                result.append(res)
        return result
    
    
class AlgorithmPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, related_name="article_column")

    updated = models.DateTimeField(auto_now=True)
    
    STATUS_CHOICES = (('gp','股票'), ('zq','债券'),('jj','基金'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='gp')
    
    body = models.TextField()
    

    
    class Meta:
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(AlgorithmPost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])