# Generated by Django 4.2.7 on 2023-12-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_nazwa_obrazka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='nazwa_obrazka',
        ),
        migrations.AddField(
            model_name='post',
            name='obrazek',
            field=models.ImageField(null=True, upload_to='posty'),
        ),
    ]
