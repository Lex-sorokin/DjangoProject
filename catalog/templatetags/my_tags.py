from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def media_filter(path):
    # if path:
    #     return f"/media/{path}"
    # return "#"
    if not path:
        return "#"  # Или путь к дефолтной заглушке, например: '/static/images/no-photo.png'

        # Если передали объект поля Django (ImageField), у него есть встроенный .url
    if hasattr(path, 'url'):
        try:
            return path.url
        except ValueError:
            return "##"  # Обработка случая, когда в БД запись есть, а файл физически удален

    # Если передали обычную строку-путь (например, "products/img.jpg")
    path_str = str(data)

    # Проверяем, не начинается ли путь уже с MEDIA_URL, чтобы избежать дублирования
    media_url = getattr(settings, 'MEDIA_URL', '/media/')
    if path_str.startswith('/') or path_str.startswith('http'):
        return path_str

    return f"{media_url}{path_str}"