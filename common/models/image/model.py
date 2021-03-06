from app.base.model import Model as _Model


class Image(_Model):
    from django.contrib.contenttypes.fields import GenericForeignKey as _GenericForeign
    from django.contrib.contenttypes.models import ContentType as _Type
    from django.db.models.fields.files import ImageField as _image
    from django.db.models.fields import related as _related
    from django.db.models import deletion as _deletion
    from django.db.models import fields as _field

    content_type = _related.ForeignKey(_Type, on_delete=_deletion.CASCADE, verbose_name="Модель")
    object_id = _field.PositiveIntegerField(verbose_name="Ключ")
    content_object = _GenericForeign()

    def computed_folder(self, file_name):
        import uuid
        from app.base.helpers import snake
        extension = file_name.split('.')[-1]

        return "%s/%d/%s" % (snake(self.content_type.model_class().__name__), self.object_id, "%s.%s" % (uuid.uuid4(), extension))

    image = _image("Изображение", null=True, upload_to=computed_folder)

    # Can be empty...
    description = _field.CharField(verbose_name="Описание", null=True, blank=True, max_length=512)

    def __str__(self):
        return "Изображение для %s [№ %d]" % (self.content_type, self.object_id)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
