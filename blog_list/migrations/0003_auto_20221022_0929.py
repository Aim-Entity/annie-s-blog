# Generated by Django 2.2.7 on 2022-10-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_list', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='blog',
            name='enable_comment',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
    ]