# Generated by Django 4.1.2 on 2023-03-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0005_department_priority_alter_task_name_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='priority',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='address',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='task',
            name='materials',
            field=models.TextField(max_length=200),
        ),
    ]
