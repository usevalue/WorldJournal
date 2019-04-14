# Generated by Django 2.1.7 on 2019-04-13 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wjlibrary', '0005_auto_20190403_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=12)),
                ('magnitude', models.DecimalField(decimal_places=8, max_digits=20)),
                ('content', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='world',
            name='description',
            field=models.TextField(default='There is no description for this world.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='world',
            name='purpose',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='environmentvariable',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wjlibrary.World'),
        ),
    ]