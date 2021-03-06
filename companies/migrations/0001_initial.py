# Generated by Django 4.0.5 on 2022-06-18 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'job_categories',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=2000, null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.category')),
            ],
            options={
                'db_table': 'job_subcategories',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('position', models.CharField(max_length=200)),
                ('technology', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('under_recruitment', 'Under Recruitment'), ('recruitment_ended', 'Recruitment Ended'), ('deleted', 'Deleted')], default='recruitment_ended', max_length=200)),
                ('compensation', models.PositiveIntegerField()),
                ('due_date', models.DateField()),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.subcategory')),
            ],
            options={
                'db_table': 'job_positions',
            },
        ),
    ]
