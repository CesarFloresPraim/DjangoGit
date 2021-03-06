# Generated by Django 2.0.2 on 2018-04-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstDjangoApp', '0007_auto_20180409_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('contrasenia', models.CharField(max_length=100)),
                ('salario', models.IntegerField(default=0)),
                ('hora_entrada', models.TimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='articulos',
            name='comision_empleado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ventas',
            name='notas',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='ventas',
            name='realizada_por',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
