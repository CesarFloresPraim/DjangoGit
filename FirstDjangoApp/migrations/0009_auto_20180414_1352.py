# Generated by Django 2.0.2 on 2018-04-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstDjangoApp', '0008_auto_20180410_2028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.AddField(
            model_name='administrador',
            name='hora_entrada',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='administrador',
            name='salario',
            field=models.IntegerField(default=0),
        ),
    ]
