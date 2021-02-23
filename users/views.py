from django.shortcuts import render, redirect
from .forms import RegisterForm
from users import models
import random

word_no = 0

def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form})

def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'exam/result.html')

def exam(request):
    words = models.words.objects.filter(cet6=1).values('word','translation')
    random.seed()
    wordno = random.randint(0,len(words)-1)
    question = {'word':words[wordno]['word']}
    random.seed()
    correct = random.randint(0,3)
    question[str(correct)] = words[wordno]['translation']
    question['correct'] = correct
    for i in range(4):
        if i != correct:
            random.seed()
            choice = random.randint(0,len(words)-1)
            question[str(i)] = words[choice]['translation']


    return render(request, 'exam/exam.html',{'question':question})

def memory(request):
    return render(request, 'memory/memory.html')

def plan(request):
    word_list = models.words.objects.filter(cet6=1).values('id', 'word', 'phonetic', 'definition', 'translation')
    return render(request, 'plan/plan.html', {'word_list': word_list})

def wordbook(request):
    books = models.books.objects.filter(user_id = 4).values('word_id','note','familiar')
    for book in books:
        query = models.words.objects.filter(id = book['word_id'] ).all()
        book['word'] = query[0].word
        book['phonetic'] = query[0].phonetic
        book['translation'] = query[0].translation
        book['definition'] = query[0].definition
    return  render(request, 'wordbook/wordbook.html',{'books':books})

def wordintro(request):
    return render(request,'wordunion/wordintro.html')

def wordunion(request):
    global word_no
    word_list = models.words.objects.filter( cet6 = 1).values('id','word','phonetic','definition','translation')
    item = word_list[word_no]
    word_no += 1
    return  render(request, 'wordunion/wordunion.html',{'item':item})

