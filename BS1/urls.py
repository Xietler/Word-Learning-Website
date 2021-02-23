"""BS1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^$', views.index, name='index'),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^wordunion/wordunion.html',views.wordunion,name='wordunion'),
    url(r'^wordunion/wordintro.html',views.wordintro,name='wordintro'),
    url(r'^wordbook/wordbook.html',views.wordbook,name='wordbook'),
    url(r'^memory/memory.html',views.memory,name='memory'),
    url(r'^plan/plan.html',views.plan,name='plan'),
    url(r'^exam/exam.html',views.exam,name='exam'),
    url(r'^exam/result.html',views.result,name = 'result'),
]
