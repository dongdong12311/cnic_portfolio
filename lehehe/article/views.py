from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import ArticleColumn,AlgorithmPost,MyalgoPost,AlgoColumn,AlgoOpt
from .forms import ArticleColumnForm,ArticlePostForm,AlgoOptPostForm,AlgoOptPostForm
import os
from .forms import MyalgoPostPostForm
from .models import name_map
from django.views.decorators.http import require_POST  
import json  
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
                #new_article.column = request.user.article_column.get(id=request.POST['column_id'])
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
def myalgo_list(request):
    algos = MyalgoPost.objects.filter(author=request.user)
    return render(request, "algo/column/myalgo_list.html", {"algos": algos})
    
@login_required(login_url='/account/login')
def myalgoopt_list(request):
    algoopts = AlgoOpt.objects.filter(author=request.user)
    for i in range(len(algoopts)):
        alggoopt = algoopts[i]
        task_id = alggoopt.task_name
        try:
            myalgopost = MyalgoPost.objects.get(id = task_id)
            alggoopt.task_name =myalgopost.title
        except:
            _del_myalgoopt(request,alggoopt.id)
        
    return render(request, "algo/column/myalgoopt_list.html",{"algoopts":algoopts})    
    
@login_required(login_url='/account/login')
def myalgo_list_to_edit(request):
    algos = MyalgoPost.objects.filter(author=request.user)
    return render(request, "algo/column/myalgo_list_to_edit.html", {"algos": algos})
    
    
@login_required(login_url='/account/login')
def myalgo_detail(request, id, slug):
    algo = get_object_or_404(MyalgoPost, id=id, slug=slug)

    algo_json = json.dumps(ParseMyalgoPost(algo))

    return render(request, "algo/column/algo_detail.html", {"algo": algo,"algo_json":algo_json})
import pandas as pd

def load_algoopt(algoopt):
    data = json.loads(algoopt.config)
    biaotou = data[0]
    data = pd.DataFrame(data[1:])
    data.columns = biaotou
    del data[biaotou[-1]]
    return data    
@login_required(login_url='/account/login')
def myalgo_opt_detail(request, id, slug):
    algoopt = get_object_or_404(AlgoOpt, id=id, slug=slug)
    
    data = load_algoopt(algoopt)
    opt_table = data.to_html(classes='table table-hover')
    return HttpResponse(opt_table)
    #return HttpResponse("1111")
    #algo_json = json.dumps(ParseMyalgoPost(algo))

    #return render(request, "algo/column/algo_detail.html", {"algo": algo,"algo_json":algo_json})




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
@require_POST
@csrf_exempt
def del_myalgoopt(request):
    algo_id = request.POST['article_id']
    return _del_myalgoopt(request,algo_id)
  

@login_required(login_url='/account/login')
@csrf_exempt
def _del_myalgoopt(request,algo_id):
    try:
        article = AlgoOpt.objects.get(id=algo_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")       

        
        
        
        
def date_to_int(date):
    return date.year * 10000 + date.month * 100 + date.day
        

def ParseMyalgoPost(algo):
    name_map = {"均值方差模型":"sample_markowitz",
            "CVaR模型":"sample_hpr",
            "VaR模型":"sample_cvar",
            "Bl模型":"sample_bl_model",
            "Hpr模型":"sample_hpr"}
    name = algo.algo_column.column
    initial_capital = 0
    balanced_dates= 0
    expected_return_days = 0
    target_return = 0
    target_risk = 0
    try:
        initial_capital = float(algo.initial_capital)
        balanced_dates = int(algo.balanced_dates)
        expected_return_days= int(algo.expected_return_days)
        target_return = float(algo.target_return)
        target_risk = float(algo.target_risk)
    except:
        pass
    

    
    cov_method  = algo.cov_method
    
    benchmark = algo.benchmark
    opt_criterion = algo.opt_criterion
    json_stocks = algo.portfolio
    if len(json_stocks):
        stocks = json.loads(json_stocks)
    else:
        stocks = "[]"
    res = {"stragety": name_map[name], "start": date_to_int(algo.start_date), 
     "end": date_to_int(algo.end_date), "initial_capital": initial_capital, 
     "benchmark": benchmark, 
     "balanced_dates": {"method": "equal_difference", "param": balanced_dates},
     "stocks": stocks, 
                "expected_return_days": expected_return_days,
                "cov_method": cov_method, 
                "opt_criterion": opt_criterion,
                "cleaned_weights": True, 
                "target_return": target_return, 
                "target_risk": target_risk, 
               
                "opt_param": {} ,
                #"risk_free_rate": 0.02, 
            }
    

    return res
       
        
        

import sys
from django.conf import settings

sys.path.append(settings.EXAMPLE_PATH)
from trading_system.engine import Run_func
from trading_system.portfolio.summarise import Cal

@login_required(login_url='/account/login')
@csrf_exempt
def run_test(request,article_id):
    if request.method == "GET":
        
        algo = MyalgoPost.objects.get(id=article_id)
        config = ParseMyalgoPost(algo)
        
        stragety = __import__(config['stragety'])

        res = Run_func(stragety.initialize,stragety.handle_data,config)
        
        
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


def get_key(res,key):
    return res['sys_analyser']['summary'][key]






def grid_search(config):
    stragety = __import__(config['stragety'])
    result = []
    params,all_param = generate_all_param(config)

    for param in all_param:
        for i in range(len(param)):
            config[params[i]] = param[i]
        

        res = Run_func(stragety.initialize,stragety.handle_data,config)

        result.append([ param,get_key(res,'sharpe'),get_key(res,'alpha'),
                       get_key(res,'max_drawdown'),get_key(res,'annualized_returns')])  
    return result

from trading_system.generate_parameter import generate,print_tree,generate_all_param    
@login_required(login_url='/account/login')
@csrf_exempt
def run_algo_opt(request,algo_opt_id):

    if request.method == "GET":
        algoopt = get_object_or_404(AlgoOpt, id=algo_opt_id)
        task_id = algoopt.task_name
        algo = get_object_or_404(MyalgoPost,id = task_id)
        config = ParseMyalgoPost(algo)
        data = load_algoopt(algoopt)
        opt_map = {"调仓间隔":["balanced_date","int"],
                   "预期收益":["target_return","float"],
                   "预期风险":["target_risk","float"]}
        all_canshu = []
        for i in range(len(data.index)):
            slices = data.iloc[i]
            all_canshu.append(slices['优化参数'])
            canshu = opt_map[slices['优化参数']][0]
            step = float(slices['寻参步长'])
            start = float(slices['优化初值'])
            dt = int(slices['网格数量'])
            data_type = opt_map[slices['优化参数']][1]
            config['opt_param'].update({canshu:{"start": start, "step": step, "dt": dt,
                  "data_type": data_type}})

        res = []
        data  = []
        if len(config['opt_param']):
            res = grid_search(config)
            for i in range(len(res)):
                data.append(res[i][0]+res[i][1:])
            data = pd.DataFrame(data)
            data.columns = all_canshu + ['夏普比率','alpha','最大回撤','年化收益率']
        trade = data.to_html(classes='table table-hover')
        return render(request,'algo/algo_opt_back_test.html',{"trade":trade})
def load_code(algo_column):
    name = name_map[algo_column] + ".py"
    res = ""
    try:     
        with open(os.path.join(settings.EXAMPLE_PATH,name)) as f:
            codes = f.readlines()
            for code in codes:
                res += code   
    except:
        pass
    return res

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
                new_algo.column = ArticleColumn.objects.get(id=request.POST['column_id'])
                new_algo.algo_column = AlgoColumn.objects.get(id=request.POST['algo_column'])
                new_algo.algo_code = load_code(new_algo.algo_column.column)    
                new_algo.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        algo_post_form = MyalgoPostPostForm()
        algo_type_columns = AlgoColumn.objects.all()
        article_columns = ArticleColumn.objects.all()
        return render(request, "algo/algopost.html", {"algo_post_form": algo_post_form,
                                                      "article_columns": article_columns,
                                                      "algo_type_columns":algo_type_columns})

@login_required(login_url='/account/login')
@csrf_exempt
def myalgoopt_post(request):
    if request.method == "POST":
        algo_opt_post_form = AlgoOptPostForm(data=request.POST)
        if algo_opt_post_form.is_valid():
            #cd = algo_post_form.cleaned_data
            try:
                new_algo = algo_opt_post_form.save(commit=False)
                new_algo.author = request.user
                new_algo.task_name = request.POST['task_id'] 
                new_algo.save()
                return HttpResponse("1")
            except:
                return HttpResponse("2")
        else:
            return HttpResponse("3")
    else:
        algo_post_form = AlgoOptPostForm()
        youhua = {"balanced_dates":"调仓间隔",
           "expected_return_days":"数据周期",
           "beta":"贝塔值",
           "target_risk":"预期风险",
           "target_return":"预期收益"}
        myalgoPosts = MyalgoPost.objects.filter(author=request.user)
        return render(request, "algo/algo_opt_post.html", 
                      {"algo_post_form": algo_post_form,
                      "myalgoPosts": myalgoPosts,"youhua":youhua.values(),
                                                      })


@login_required(login_url='/account/login')
@csrf_exempt
def redit_myalgo(request, article_id):
    if request.method == "GET":
        article_columns = ArticleColumn.objects.all()
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
            redit_article.column = ArticleColumn.objects.get(id=request.POST['column_id'])
            redit_article.algo_column = AlgoColumn.objects.get(id =request.POST['algo_column'])
            redit_article.algo_code = load_code(redit_article.algo_column.column) 
            redit_article.save()
            return HttpResponse("1")

        except :
            return HttpResponse("2")    

        





@login_required(login_url='/account/login')
@csrf_exempt
def redit_myalgoopt(request, article_id):
    if request.method == "GET":
        article_columns = ArticleColumn.objects.all()
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
            redit_article.column = ArticleColumn.objects.get(id=request.POST['column_id'])
            redit_article.algo_column = AlgoColumn.objects.get(id =request.POST['algo_column'])
            redit_article.algo_code = load_code(redit_article.algo_column.column) 
            redit_article.save()
            return HttpResponse("1")

        except :
            return HttpResponse("2") 








