# Generated by Django 3.2.3 on 2021-05-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AJNIHA', '0005_alter_readeraccount_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(auto_created=True, blank=True, default='/book.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='readeraccount',
            name='prof_pic',
            field=models.ImageField(auto_created=True, blank=True, default='/default.png', null=True, upload_to=''),
        ),
    ]