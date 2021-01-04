# Generated by Django 3.1.4 on 2021-01-04 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['post'], name='post_like_post_id_07b99b_idx'),
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['user'], name='post_like_user_id_4595a5_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post_id', 'user_id')},
        ),
    ]
