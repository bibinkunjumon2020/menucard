from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Define a model called MenuItem that extends MPTTModel, which provides the functionality
# for creating a tree-like structure of menu items.
class MenuItem(MPTTModel):
    # Define a field to store the name of the menu item.
    name = models.CharField(max_length=100)
    # Define a field to store the URL of the menu item.
    url = models.CharField(max_length=255, blank=True)
    # Define a field to store the named URL of the menu item.
    named_url = models.CharField(max_length=100, blank=True)
    # Define a foreign key to store the parent of the menu item.
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    # Define fields to store the level, left value, right value, and tree ID of the menu item.
    level = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    lft = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    rght = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    tree_id = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class MPTTMeta:
        # Define the order of insertion for the menu items based on their name.
        order_insertion_by = ['name']

    def __str__(self):
        # Return the name of the menu item as a string.
        return self.name
