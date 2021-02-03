# Generated by Django 3.1.5 on 2021-02-03 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CactusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cactus_name', models.CharField(max_length=50)),
                ('cactus_scientific_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cactus_description', models.TextField(blank=True, max_length=200, null=True)),
                ('cactus_size', models.CharField(choices=[('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande')], max_length=1)),
            ],
            options={
                'db_table': 'cactus',
            },
        ),
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_file', models.ImageField(unique=True, upload_to='pictures')),
                ('picture_date', models.DateField(auto_now_add=True)),
                ('picture_cactus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cactus.cactusmodel')),
            ],
        ),
    ]