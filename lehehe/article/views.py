from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn,AlgorithmPost,MyalgoPost,AlgoColumn
from .forms import ArticleColumnForm,ArticlePostForm

from django.views.decorators.http import require_POST  
@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html", {"columns": columns, 'column_form': column_form})

    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")
@login_required(login_url='/account/login/')
@csrf_exempt
def myalgo_column(request):
    if request.method == "GET":
        columns = AlgoColumn.objects.filter(user=request.user)
        column_form = MyalgoPostPostForm()
        return render(request, "algo/column/algo_column.html", {"columns": columns, 'column_form': column_form})

    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse("1")        
@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

      
@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def rename_article_column(request):
    column_name = request.POST["column_name"]
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")
    
    
@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request, "article/column/article_post.html",
                      {"article_post_form": article_post_form, 
                       "article_columns": article_columns})

@login_required(login_url='/account/login')
def article_list(request):
    articles = AlgorithmPost.objects.filter(author=request.user)
    return render(request, "article/column/article_list.html", {"articles": articles})
from django.shortcuts import  get_object_or_404

@login_required(login_url='/account/login')
def article_detail(request, id, slug):
    article = get_object_or_404(AlgorithmPost, id=id, slug=slug)
    return render(request, "article/column/article_detail.html", {"article": article})

@login_required(login_url='/account/login')
def myalgo_list(request):
    algos = MyalgoPost.objects.filter(author=request.user)
    return render(request, "algo/column/myalgo_list.html", {"algos": algos})

@login_required(login_url='/account/login')
def myalgo_detail(request, id, slug):
    algo = get_object_or_404(MyalgoPost, id=id, slug=slug)
    return render(request, "algo/column/algo_detail.html", {"algo": algo})





@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST['article_id']
    
    try:
        article = AlgorithmPost.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_myalgo(request):
    algo_id = request.POST['article_id']
    
    try:
        article = MyalgoPost.objects.get(id=algo_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")  
    
    
@login_required(login_url='/account/login')
@csrf_exempt
def redit_article(request, article_id):
    if request.method == "GET":
        article_columns = request.user.article_column.all()
        article = AlgorithmPost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={"title": article.title})
        this_article_column = article.column
        return render(request, "article/column/redit_article.html",
                      {"article": article, "article_columns": article_columns, "this_article_column": this_article_column, "this_article_form": this_article_form})
    else:
        redit_article = AlgorithmPost.objects.get(id=article_id)
        try:
            redit_article.column = request.user.article_column.get(id=request.POST['column_id'])
            redit_article.title = request.POST['title']
            redit_article.body = request.POST['body']
            redit_article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
        

        
        
        
        
def date_to_int(date):
    return date.year * 10000 + date.month * 100 + date.day
        
        
from .models import name_map
def ParseMyalgoPost(algo):
    name_map = {"均值方差模型":"sample_markowitz",
            "CVaR模型":"sample_hpr",
            "VaR模型":"sample_cvar",
            "Bl模型":"sample_bl_model",
            "Hpr模型":"sample_hpr"}
    name = algo.algo_column.column
    initial_capital = float(algo.initial_capital)
    target_return = algo.target_return
    target_risk = algo.target_risk
    expected_return_days= int(algo.expected_return_days)
    cov_method  = algo.cov_method
    balanced_dates = int(algo.balanced_dates)
    benchmark = algo.benchmark
    
    res = {"stragety": name_map[name], "start": date_to_int(algo.start_date), 
     "end": date_to_int(algo.end_date), "initial_capital": initial_capital, 
     "benchmark": benchmark, 
     "balanced_dates": {"method": "equal_difference", "param": balanced_dates},
     "stocks": ["000001.SZ", "000002.SZ", "000004.SZ", "000005.SZ", 
                "000006.SZ", "000007.SZ", "000008.SZ", "000009.SZ", "000010.SZ"], 
                "expected_return_days": expected_return_days,
                "cov_method": "sample", 
                "opt_criterion": "max_sharpe",
                "cleaned_weights": True, 
                "target_return": target_return, 
                "target_risk": target_risk, 
                "risk_free_rate": 0.02, 
                "opt_param": {}
            }


    return res
       
        
        
import json
import sys
from django.conf import settings
import pandas as pd
sys.path.append(settings.EXAMPLE_PATH)
from trading_system.engine import Run_func
from trading_system.plot.plot import plot_result
from trading_system.generate_parameter import generate,print_tree,generate_all_param
from trading_system.portfolio.summarise import Cal
@login_required(login_url='/account/login')
@csrf_exempt
def run_test(request,article_id):
    if request.method == "GET":
        algo = MyalgoPost.objects.get(id=article_id)
        config = ParseMyalgoPost(algo)
        stragety = __import__(config['stragety'])
        try:
            res = Run_func(stragety.initialize,stragety.handle_data,config)
        except Exception as  e:
            return HttpResponse(str(e))
        data = res['sys_analyser']
        portfolio_series = data['portfolio']['unit_net_value']
        market_series = data['benchmark_portfolio']['unit_net_value']
        market_value = list(market_series)
        portfolio_value = list(portfolio_series)
        temp = list(data['benchmark_portfolio'].index)
        for i in range(len(temp)):
            temp[i] = temp[i].strftime("%Y-%m-%d")
            market_value[i] = market_value[i] -1
            portfolio_value[i] = portfolio_value[i] - 1
        xaxis = temp
        ymin = int(min(min(portfolio_value),min(market_value)) * 100 - 10) /100 
        ymax = int(max(max(portfolio_value),max(market_value)) * 100 + 10) /100 
        trade_data = data['trade']
        del trade_data['commission']
        del trade_data['exec_id']
        del trade_data['order_id']
        del trade_data['order_book_id']
        del trade_data['tax']
        trade_data.columns = ['成交价格','成交数量','成交标的','交易方向','side',
                              '交易日期','交易费用']
        trade = data['trade'].to_html(classes='table table-hover')
        trade = trade.replace('dataframe ','')
        trade = trade.replace('border="1"','border="1" id ="tradetable1" data-pagination="true" ')
        trade = trade.replace('\n','')
        trade = trade.replace('<th>trade_date</th>','')
        trade = trade.replace('<th></th>','')
        trade = trade.replace('<tr></tr>','')
        trade = trade.replace('<tr style="text-align: right;">','<tr style="text-align: right;"><th>日期</th>')
        
        trade_info = data['stock_positions']
        del trade_info['order_book_id']
        trade_info.columns = ['持仓成本','最新价格','总市值','持仓数量','交易标的',
                              ]

        trade2 = trade_info.to_html(classes='table table-hover')
        trade2 = trade2.replace('\n','')
        trade2 = trade2.replace('<th>trade_date</th>','')
        trade2 = trade2.replace('<th></th>','')
        trade2 = trade2.replace('<tr></tr>','')
        trade2 = trade2.replace('<tr style="text-align: right;">','<tr style="text-align: right;"><th>日期</th>')

        calculator = Cal()
        alpha =  round(calculator._alpha(portfolio_series,market_series),2)
        annualized_returns = round(100*calculator._annualized_returns(portfolio_series),2)
        benchmark_annualized_returns = calculator._annualized_returns(market_series)
        benchmark_total_returns = calculator._total_returns(market_series)
        max_drawdown = round(100*calculator._downside_risk(portfolio_series),2)
        beta = round(calculator._beta(portfolio_series,market_series),2)
        sharpe = round(calculator._sharpe(portfolio_series),2)
        total_returns = round(100*calculator._total_returns(portfolio_series),2)
        market_returns = round(100*calculator._total_returns(market_series),2)
        chao_e  = total_returns - market_returns
        volatility = round(calculator._var(portfolio_series),2)
        market_volatility = round(calculator._var(market_series),2)
        daily_ratio = list(calculator._ratio(portfolio_series))
        start_date = temp[0]
        end_date = temp[-1]
        initial_capital = config['initial_capital']
        return render(request,'algo/back_test.html',locals())
        

import os
from .forms import MyalgoPostPostForm
from .models import name_map
@login_required(login_url='/account/login')
@csrf_exempt
def myalgo_post(request):
    if request.method == "POST":
        algo_post_form = MyalgoPostPostForm(data=request.POST)

        if algo_post_form.is_valid():
            cd = algo_post_form.cleaned_data
            try:
                new_algo = algo_post_form.save(commit=False)
                new_algo.author = request.user
                new_algo.column = request.user.article_column.get(id=request.POST['column_id'])
                new_algo.algo_column = AlgoColumn.objects.get(id=request.POST['algo_column'])

                try:
                    name = name_map[new_algo.algo_column.column] + ".py"
                    with open(os.path.join(settings.EXAMPLE_PATH,name)) as f:
                        codes = f.readlines()
                        for code in codes:
                            new_algo.algo_code += code           
                except Exception as e:
                    pass
                    
                new_algo.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        algo_post_form = MyalgoPostPostForm()
        algo_type_columns = AlgoColumn.objects.all()
        article_columns = request.user.article_column.all()
        return render(request, "algo/algopost.html", {"algo_post_form": algo_post_form,
                                                      "article_columns": article_columns,
                                                      "algo_type_columns":algo_type_columns})


from .models import map_dic
@login_required(login_url='/account/login')
@csrf_exempt
def redit_myalgo(request, article_id):
    if request.method == "GET":
        article_columns = request.user.article_column.all()
        algo_type_columns = AlgoColumn.objects.all()
        algo = MyalgoPost.objects.get(id=article_id)

        algo_post_form = MyalgoPostPostForm(
              instance=algo )
        this_article_column = algo.column
        this_algo_type_column = algo.algo_column
        return render(request, "algo/column/redit_algo.html",
                      {"algo": algo, "article_columns": article_columns,
                       "algo_type_columns":algo_type_columns,
                       "this_algo_type_column":this_algo_type_column,
                       "this_article_column": this_article_column, 
                       "algo_post_form": algo_post_form})
    else:
        redit_article = MyalgoPost.objects.get(id=article_id)
        list_to_edit = ["title","portfolio","initial_capital",
                        "start_date","end_date","benchmark",
         "balanced_dates",
           "expected_return_days",
           "cov_method",
           "beta",
           "opt_criterion",
           "target_risk",
           "target_return",
           "p_matrix",
           "q_matrix"]  
        for dd in list_to_edit:
                setattr(redit_article,dd,request.POST[dd])
        try:
            redit_article.column = request.user.article_column.get(id=request.POST['column_id'])
            redit_article.algo_column = AlgoColumn.objects.get(id =request.POST['algo_column'])
            redit_article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")    
        







from django.shortcuts import render_to_response
 
# 表单
@login_required(login_url='/account/login')
@csrf_exempt
def myalgo_post2(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        if ctx['rlt']:
            return HttpResponse(str(ctx['rlt']))
    return render(request, "algo/algopost.html", ctx)
 
# 接收请求数据
def save_algo_form(request):  
    request.encoding='utf-8'
    message = '你提交了空表单'
    return HttpResponse(message)







