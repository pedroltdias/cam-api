# Generated by Django 4.2 on 2023-04-18 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_funcionario_telefone_alter_departamento_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='carga_horaria_semanal',
            field=models.PositiveIntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=550, max_digits=10),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='horas_necessarias',
            field=models.IntegerField(default=120),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='horas_realizadas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='prazo_estimado',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ultima_atualizacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
