# Generated by Django 4.2 on 2023-04-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20230414_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
