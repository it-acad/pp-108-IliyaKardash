# Generated by Django 5.1.4 on 2025-01-14 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_alter_author_surname'),
        ('book', '0004_book_date_of_issue_book_year_of_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='works', to='book.book'),
        ),
    ]
