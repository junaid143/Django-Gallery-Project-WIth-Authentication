# Generated by Django 4.1.7 on 2023-02-18 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GalleryApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='Images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.CharField(max_length=100)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GalleryApp.categorymodel')),
            ],
        ),
    ]
