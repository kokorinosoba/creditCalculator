from django.conf import settings
from django.db import models


class Status(models.Model):
    class Meta:
        verbose_name = 'ステータス'
        verbose_name_plural = 'ステータス'
        unique_together = ('user', 'subject')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )
    doing = models.BooleanField(
        default=False,
    )
    done = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return str(self.user) + " " + str(self.subject)


class Subject(models.Model):
    class Meta:
        verbose_name = '授業科目'
        verbose_name_plural = '授業科目'

    subject_id = models.IntegerField(
        primary_key=True,
        default=None,
        unique=True,
    )
    subject_name = models.CharField(
        max_length=30,
        unique=True,
    )
    credits = models.IntegerField(
        default=2,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.subject_name


class Category(models.Model):
    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリー'

    category_name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.category_name


class Cource(models.Model):
    class Meta:
        verbose_name = 'コース'
        verbose_name_plural = 'コース'

    cource_abbreviation = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
    )
    cource_name = models.CharField(
        max_length=30,
        default=None,
        unique=True,
    )

    def __str__(self):
        return self.cource_abbreviation


class Cource_Subject(models.Model):
    class Meta:
        verbose_name = '科目のコース'
        verbose_name_plural = '科目のコース'
        unique_together = ('subject', 'cource')

    subject = models.ForeignKey(
        'Subject',
        on_delete=models.SET_NULL,
        null=True,
    )
    cource = models.ForeignKey(
        'Cource',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.subject) + " " + str(self.cource)


class User(models.Model):
    class Meta:
        verbose_name = 'ユーザ'
        verbose_name_plural = 'ユーザ'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    cource = models.ForeignKey(
        'Cource',
        on_delete=models.SET_NULL,
        null=True,
    )
    department = models.ForeignKey(
        'Department',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.user)


class Department(models.Model):
    class Meta:
        verbose_name = '学科'
        verbose_name_plural = '学科'

    department = models.CharField(
        max_length=30,
        default=None,
        unique=True,
    )

    def __str__(self):
        return self.department
