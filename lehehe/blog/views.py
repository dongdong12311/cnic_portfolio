

# Create your views here.
from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Algorithm


def blog_list(request):
    algos = Algorithm.objects.all()
    return render(request, "algos/algo_list.html", {"algos": algos})

def blog_detail(request, algo_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(Algorithm, id=algo_id)
    pub = article.update_time
    return render(request, "algos/algo_detail.html", {"article": article, "publish": pub})


