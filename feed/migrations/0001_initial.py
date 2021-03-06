# Generated by Django 2.0.4 on 2018-05-06 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, max_length=2000, null=True)),
                ('feed_url', models.URLField()),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('last_polled_time', models.DateTimeField(blank=True, null=True)),
                ('cover_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('width_field', models.IntegerField(default=400)),
                ('height_field', models.IntegerField(default=400)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.URLField(blank=True, max_length=2000, null=True)),
                ('audio_url', models.URLField(max_length=2000)),
                ('description', models.TextField(blank=True, null=True)),
                ('published_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('duration', models.CharField(blank=True, max_length=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feed.Channel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Episode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MstCollection',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MstPlaylist',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('is_public', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MstTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('play_order', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Episode')),
                ('mst_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.MstPlaylist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feed.Channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Episode')),
                ('mst_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.MstTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.Episode'),
        ),
        migrations.AddField(
            model_name='collection',
            name='mst_collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.MstCollection'),
        ),
    ]
