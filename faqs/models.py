from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))

    # Language-specific translations
    question_hi = models.TextField(_("Question in Hindi"), blank=True, null=True)
    question_bn = models.TextField(_("Question in Bengali"), blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_translated_question(self, lang):
        """ Returns the translated question based on language """
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        return self.question  # Default to English

    def __str__(self):
        return self.question[:50]  # Show first 50 chars
