# Generated by Django 4.0.2 on 2022-03-12 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bloggers', '0001_initial'),
        ('blog', '0003_alter_blog_author_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bloggers.author'),
        ),
    ]
