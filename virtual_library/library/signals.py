from django.db.models.signals import post_delete
from django.dispatch import receiver
from library.models import Book


@receiver(post_delete, sender=Book)
def del_book_authors_connect(sender, instance, **kwargs):
    """Отслеживает сигнал удаления Book и удаляет связи с авторами"""
    instance.authors.clear()
