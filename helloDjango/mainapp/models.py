import uuid

from django.db import models


# Create your models here.
class UserEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='账号')
    age = models.IntegerField(default=0, verbose_name='年龄')
    phone = models.CharField(max_length=11, verbose_name='手机号')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_user'
        verbose_name = '客户管理'
        verbose_name_plural = verbose_name


class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')
    order_num = models.IntegerField(verbose_name='排序')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        verbose_name = '水果分类'
        verbose_name_plural = verbose_name
        ordering = ['-order_num']


class FruitEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='水果名')
    price = models.FloatField(verbose_name='价格')
    source = models.CharField(max_length=30, verbose_name='原产地')
    category = models.ForeignKey(CateTypeEntity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name


class StoreEntity(models.Model):
    class Meta:
        db_table = 't_store'
        unique_together = (('name', 'city'),)
        verbose_name = '水果店'
        verbose_name_plural = verbose_name

    id = models.UUIDField(primary_key=True, verbose_name='店号')
    name = models.CharField(max_length=50, verbose_name='店名', unique=True)
    store_type = models.IntegerField(choices=((0, '自营'), (1, '第三方')), verbose_name='类型', db_column='type_')
    address = models.CharField(max_length=100, verbose_name='地址')
    city = models.CharField(max_length=50, verbose_name='城市', db_index=True)
    logo = models.ImageField(verbose_name='LOGO', upload_to='store', width_field='logo_width',height_field='logo_heigth',blank=True,null=True)
    logo_width = models.IntegerField(verbose_name='LOGO宽', null=True)
    logo_heigth = models.IntegerField(verbose_name='LOGO高', null=True)
    summary = models.TextField(verbose_name='介绍',blank=True,null=True)
    create_time = models.DateField(verbose_name='成立时间', auto_now_add=True)
    last_time = models.DateField(verbose_name='最后变更时间', auto_now=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()

    @property
    def id_(self):
        return self.id.hex
