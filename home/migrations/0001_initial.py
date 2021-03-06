# Generated by Django 3.2.7 on 2022-01-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('is_completed', models.BinaryField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
