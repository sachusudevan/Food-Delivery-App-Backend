# Generated by Django 3.1.7 on 2021-05-16 14:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.SlugField(allow_unicode=True, default=uuid.uuid4, editable=False, max_length=255, unique=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('is_publish', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category-backgrounds/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
