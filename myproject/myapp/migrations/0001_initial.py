# Generated by Django 4.0.1 on 2022-01-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('family', models.CharField(blank=True, max_length=150)),
                ('age', models.SmallIntegerField()),
                ('cod', models.PositiveIntegerField(default='311111111', unique=True)),
            ],
        ),
    ]
