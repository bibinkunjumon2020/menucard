from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    level = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    lft = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    rght = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    tree_id = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
