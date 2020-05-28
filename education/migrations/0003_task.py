# Generated by Django 3.0.6 on 2020-05-28 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.Course')),
                ('lecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Lecture')),
            ],
        ),
    ]
