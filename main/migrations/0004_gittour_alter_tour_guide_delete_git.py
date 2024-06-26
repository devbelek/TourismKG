# Generated by Django 4.2.8 on 2024-06-23 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_git_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='tour',
            name='guide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tours', to='main.profileuser'),
        ),
        migrations.DeleteModel(
            name='Git',
        ),
    ]