from django.conf.urls import url

from . import views

# urlpatterns是被Django自动识别的路由列表变量

urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径，视图)
    url(r"^index/$",views.index),
    url(r"^detail/$",views.detail),
    url(r"^add/$",views.add),
]