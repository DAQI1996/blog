from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
import json
from .models import Comment,Blog

# 博客列表页
def index(request):
    # user = request.session.get("user")
    # if not user:
    #     pass
    #  简单测试，未考略数据过多分页的情况，
    try:
        datas = Blog.objects.all()
    except Exception as e:
        print(e)
    return render(request,"index.html",locals())


# 博客详情页
def detail(request):
    id = int(request.GET.get("id"))
    if not id:
        print("请求错误")
    try:
        data = Blog.objects.get(id=id)
        comments = Comment.objects.filter(blog_id=id)
    except Exception as e:
        print(e)
    return render(request,"detail.html",locals())


# 博客评论添加
def add(request):
    # 这里没有实现登录功能，所以取不出东西，直接写死了user
    # user = request.session.get("user")
    user = "大琦"
    id = int(request.POST.get("id"))
    comment = request.POST.get("comment")
    if not all([id, comment]):
        return HttpResponse(json.dumps({"state": 0, "msg": "数据添加参数错误"}), content_type="application/json")
    comm = Comment(
        user=user,
        comment=comment,
        time=timezone.now(),
        blog_id=id
    )
    try:
        comm.save()
    except Exception as e:
        return HttpResponse(json.dumps({ "state": 0,"msg": "".format(e)}), content_type="application/json")
    return HttpResponse(json.dumps({ "state": 1,"msg": "添加成功"}), content_type="application/json")