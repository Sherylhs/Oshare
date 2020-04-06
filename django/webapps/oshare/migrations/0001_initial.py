<<<<<<< HEAD
# Generated by Django 3.0.2 on 2020-04-06 03:18

from django.conf import settings
=======
# Generated by Django 3.0.5 on 2020-04-05 17:01

>>>>>>> yinuod
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> yinuod
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=1500)),
<<<<<<< HEAD
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(max_length=400)),
                ('image', models.ImageField(blank=True, null=True, upload_to='oshare/product_img')),
                ('rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.IntegerField(max_length=15)),
                ('address', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(default='images/profile.png', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oshare.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='oshare/post_img')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='oshare.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='products',
            field=models.ManyToManyField(to='oshare.Product'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshare.UserModel'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('ship_addr', models.CharField(max_length=100)),
                ('order_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshare.UserModel')),
            ],
        ),
        migrations.CreateModel(
            name='FollowModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.DateTimeField(auto_now=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_followed', to='oshare.UserModel')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_follows', to='oshare.UserModel')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=300)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshare.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshare.UserModel')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oshare.UserModel')),
>>>>>>> yinuod
            ],
        ),
    ]
