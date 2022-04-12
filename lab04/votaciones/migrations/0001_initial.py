# Generated by Django 4.0.3 on 2022-04-05 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_reg', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cand', models.CharField(max_length=20)),
                ('apellido_cand', models.CharField(max_length=20)),
                ('edad_cand', models.IntegerField(max_length=2)),
                ('origen_cand', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='date of birth')),
                ('partido', models.CharField(max_length=15)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votaciones.region')),
            ],
        ),
    ]
