# Generated by Django 4.2.3 on 2023-07-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.CharField(default='https://clipartix.com/wp-content/uploads/2019/03/stack-of-books-clipart-18-2019-22.jpg', max_length=500),
        ),
    ]