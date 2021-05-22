# Generated by Django 3.2.3 on 2021-05-22 06:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('pageNo', models.IntegerField()),
                ('bookTitle', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('rate', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReaderAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=40)),
                ('sName', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('country', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(max_length=40)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelfName', models.CharField(max_length=40)),
                ('shelfType', models.CharField(max_length=1)),
                ('Reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.readeraccount')),
            ],
            options={
                'unique_together': {('shelfName', 'Reader', 'shelfType')},
            },
        ),
        migrations.CreateModel(
            name='shelves_Readers_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.readeraccount')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.shelves')),
            ],
            options={
                'unique_together': {('reader', 'book', 'shelf')},
            },
        ),
        migrations.CreateModel(
            name='ReadingRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('fromPage', models.IntegerField()),
                ('toPage', models.IntegerField()),
                ('note', models.TextField()),
                ('private', models.BooleanField(default=False)),
                ('bookcompleted', models.BooleanField(default=False)),
                ('book_shelf_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.shelves_readers_books')),
            ],
        ),
        migrations.CreateModel(
            name='liked_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.readeraccount')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.readingrecords')),
            ],
        ),
        migrations.CreateModel(
            name='booksuggest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_Title', models.CharField(max_length=40)),
                ('book_description', models.TextField()),
                ('accountUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AJNIHA.readeraccount')),
            ],
        ),
        migrations.CreateModel(
            name='follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='AJNIHA.readeraccount')),
                ('follower_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='AJNIHA.readeraccount')),
            ],
            options={
                'unique_together': {('follower_account', 'followed_account')},
            },
        ),
    ]
