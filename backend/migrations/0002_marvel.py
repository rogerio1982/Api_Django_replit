# Generated by Django 3.1.5 on 2021-08-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marvel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('technology', models.CharField(max_length=20)),
                ('image', models.FileField(blank=True, upload_to='static/')),
            ],
        ),
    ]
