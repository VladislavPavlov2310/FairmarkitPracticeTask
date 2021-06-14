# Generated by Django 3.2 on 2021-06-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='authors', to='api.Book'),
        ),
    ]