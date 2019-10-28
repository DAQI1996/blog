from django.db import models


class Blog(models.Model):
    """博客"""
    title = models.CharField(max_length = 20, null=False)  # 博客标题
    zhaiyao = models.CharField(max_length = 50,null=True)  # 博客摘要
    content = models.TextField(null = False)  # 博客内容
    category = models.CharField(max_length = 20, null=True)  # 博客分类
    auth = models.CharField(max_length = 20, null=False)  # 博客标题
    time = models.DateTimeField(auto_now_add=False, null=False) # 博客创建时间


class Comment(models.Model):
    """评论"""
    user = models.CharField(max_length=10, null=False)  # 评论的用户名
    comment = models.TextField(null=False)   # 评论的内容
    blog_id = models.IntegerField(null=False)   # 所属博客的ID
    time = models.DateTimeField(auto_now_add=False, null=False)  # 评论创建时间
