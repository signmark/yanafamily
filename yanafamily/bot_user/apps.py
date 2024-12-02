from django.apps import AppConfig

class BotUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot_user'
    verbose_name = 'Пользователи бота'  # Название приложения в админке
