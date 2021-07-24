import uuid
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.db import models


class BaseModel(models.Model):
    user_model = get_user_model()

    uid = models.UUIDField(verbose_name=_('UUID'), unique=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(to=user_model, verbose_name=_('created by'), null=True, blank=True,
                                   related_name='%(class)s_created', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(to=user_model, verbose_name=_('updated by'), null=True, blank=True,
                                   related_name='%(class)s_updated', on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), null=True, blank=True)

    class Meta:
        abstract = True