from django.db import models

class BotUser(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    male = models.CharField(max_length=10)
    description = models.CharField(max_length=4096)
    usage = models.IntegerField()
    if_tarif = models.IntegerField()
    order_id = models.IntegerField()

    class Meta:
        db_table = "users"  # Имя существующей таблицы
        managed = False  # Django не будет пытаться управлять таблицей
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"

    def __str__(self):
        return self.name
