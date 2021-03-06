from django.contrib import admin
from .models import AlgorithmPost,MyalgoPost,AlgoColumn,AlgoOpt
# Register your models here.
@admin.register(AlgorithmPost)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'body')
    list_filter = ('author','title')
    
@admin.register(MyalgoPost)
class MyalgoPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'algo_column')
    list_filter = ('author','title')
    
@admin.register(AlgoOpt)
class AlgoOptAdmin(admin.ModelAdmin):
    list_display = ('author', 'task_name','config')    
    
@admin.register(AlgoColumn)
class AlgoColumnAdmin(admin.ModelAdmin):
    list_display = ('column', 'created')
