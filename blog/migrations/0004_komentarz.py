# Generated by Django 4.2.7 on 2023-12-08 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_nazwa_obrazka_post_obrazek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentarz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_uzytkownika', models.CharField(max_length=120)),
                ('mail_uzytkownika', models.EmailField(max_length=254)),
                ('tekst', models.TextField(max_length=400)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentarze', to='blog.post')),
            ],
        ),
    ]
