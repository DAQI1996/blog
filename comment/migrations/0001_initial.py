# Generated by Django 2.1.10 on 2019-10-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('zhaiyao', models.CharField(max_length=50, null=True)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=20, null=True)),
                ('auth', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=10)),
                ('comment', models.TextField()),
                ('blog_id', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
