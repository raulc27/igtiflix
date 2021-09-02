# Generated by Django 3.2.4 on 2021-09-02 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('idGenero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='genero.genero')),
            ],
        ),
    ]
