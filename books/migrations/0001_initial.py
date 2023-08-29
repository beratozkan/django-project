# Generated by Django 4.2.4 on 2023-08-29 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True, default='')),
                ('birht_date', models.DateField(blank=True, default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abstract', models.TextField(blank=True, default='')),
                ('pageSize', models.IntegerField(blank=True, default='', max_length=100)),
                ('price', models.IntegerField(blank=True, default='', max_length=100)),
                ('ISBN', models.IntegerField(blank=True, default='', max_length=100)),
                ('author_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
    ]
