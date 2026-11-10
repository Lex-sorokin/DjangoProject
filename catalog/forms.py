from django import forms
from django.core.exceptions import ValidationError
from catalog.models import Product


class ProductForm(forms.ModelForm):
    # Список запрещенных слов в нижнем регистре
    FORBIDDEN_WORDS = {
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    }

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


    def clean_price(self):
        price = self.cleaned_data.get('price')

        # Проверяем, что цена не None и меньше 0
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")

        return price


    def _validate_text(self, text):
        """Вспомогательный метод для проверки текста на запрещенные слова."""
        if not text:
            return text

        # Переводим текст в нижний регистр для проверки без учета регистра
        lowered_text = text.lower()

        # Проверяем наличие каждого запрещенного слова в тексте
        for word in self.FORBIDDEN_WORDS:
            if word in lowered_text:
                raise ValidationError(f"Использование слова '{word}' запрещено в целях безопасности.")
        return text

    def clean_name(self):
        name = self.cleaned_data.get('name')
        return self._validate_text(name)

    def clean_description(self):
        description = self.cleaned_data.get('description')
        return self._validate_text(description)
