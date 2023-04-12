# Import the required modules
from django import template
from .models import MenuItem

# Register a new template library
register = template.Library()  # creates a new instance of Django's template library.


# decorator that registers the function that follows as a simple template tag.
# Simple tags are tags that accept arguments and return a string that will be inserted into the template.
@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Get the current URL
    current_url = context['request'].path

    # Get the menu items from the database
    menu_items = MenuItem.objects.filter(name=menu_name)

    # Create a dictionary to store the items and their children
    menu_dict = {}
    for item in menu_items:
        if item.parent_id is None:
            menu_dict[item.id] = {'item': item, 'children': []}
        else:
            parent_id = item.parent_id
            if parent_id in menu_dict:
                menu_dict[parent_id]['children'].append({'item': item, 'children': []})
            else:
                menu_dict[parent_id] = {'item': None, 'children': [{'item': item, 'children': []}]}

    # Recursively expand the menu to include the active item and its children
    def expand_menu(menu_dict, active_item):
        for key in menu_dict:
            if menu_dict[key]['item'] == active_item:
                menu_dict[key]['expanded'] = True
                expand_menu(menu_dict, None)
            elif active_item is not None and menu_dict[key]['item'] is not None and active_item.id == menu_dict[key][
                'item'].id:
                menu_dict[key]['expanded'] = True
                expand_menu(menu_dict[key]['children'], None)
            else:
                expand_menu(menu_dict[key]['children'], active_item)

    # Find the active item and expand the menu
    active_item = None
    for item in menu_items:
        if item.url == current_url or item.named_url == current_url:
            active_item = item
            break
    expand_menu(menu_dict, active_item)

    # Render the menu using the template
    return template.loader.render_to_string('menu.html', {'menu_dict': menu_dict})
