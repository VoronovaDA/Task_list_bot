from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler
from django.conf import settings

from task_entry.models import Tasks


def log_err(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            err_message = f"Произошла ошибка: {e}"
            print(err_message)
            raise e

    return inner


class Command(BaseCommand):
    help = "Start Telegram bot"

    def handle(self, *args, **options):
        def start(update, context):
            context.bot.send_message(
                chat_id=update.message.chat_id,
                text="Привет! Я бот для работы с задачами. Используйте /add для добавления задачи и /tsk для просмотра списка задач.",
            )

        @log_err
        def add_task(update, context):
            task_text = " ".join(context.args)
            Tasks.objects.create(task_text=task_text)
            context.bot.send_message(
                chat_id=update.message.chat_id, text="Задача успешно добавлена!"
            )

        @log_err
        def list_tasks(update, context):
            tasks = Tasks.objects.all()
            tasks_text = (
                "\n".join([task.task_text for task in tasks])
                if tasks
                else "Список задач пуст"
            )
            context.bot.send_message(chat_id=update.message.chat_id, text=tasks_text)

        updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("add", add_task))
        dispatcher.add_handler(CommandHandler("tsk", list_tasks))

        updater.start_polling()
