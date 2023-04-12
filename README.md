
# Job Tasks

You need to make a django app that will implement a tree menu, observing the following conditions:
1) The menu is implemented through the template tag
2) Everything above the selected item is expanded. The first level of nesting under the selected item is also expanded.
3) Stored in the database.
4) Edited in the standard Django admin
5) The active menu item is determined based on the URL of the current page
6) There can be several menus on one page. They are identified by name.
7) When you click on the menu, you go to the URL specified in it. The URL can be specified either explicitly or via named url.
8) To draw each menu, exactly 1 query to the database is required
  We need django-app, which allows you to add menus (one or more) to the database through the admin panel, and draw menus by name on any desired page.
  {% draw_menu 'main_menu' %}


## Work status:

1. The menu is implemented through the template tag:

        The code uses the custom template tag {% draw_menu 'main_menu' %} to draw the menu on the page. 
        This means that the menu's content is defined in a separate template file, which is included in the main template using this tag.

2. Everything above the selected item is expanded. The first level of nesting under the selected item is also expanded:

        This requirement means that when a menu item is selected, all the menu items above it should be expanded, and the first level of items below it should also be expanded. 
        The code achieves this using the expanded is_ancestor_selected, and is_selected attributes of the menu items, which are set based on the current page URL.


3. Stored in the database:

        The menu items are stored in the database, which allows them to be edited through Django's admin panel. 
        This means that the menu content can be easily updated without needing to modify the code.

4. Edited in the standard Django admin:
    
        admin.site.register(MenuItem, MPTTModelAdmin)
5. The active menu item is determined based on the URL of the current page:

        The code uses the request.path attribute to determine the current page URL and sets the is_ancestor_selected and is_selected attributes accordingly.

        current_url = context['request'].path

6. There can be several menus on one page. They are identified by name:

        {% draw_menu 'main_menu' %}

This means that multiple menus can be defined and included on the same page.

7. When you click on the menu, you go to the URL specified in it. The URL can be specified either explicitly or via named url:

        This requirement means that the menu items should be clickable links that take the user to the specified URL. 
        The code achieves this using the url and named_url attributes of the menu items, which are used to generate the link URL.

8. To draw each menu, exactly 1 query to the database is required:

        In my code, I fetch all the menu items from the database using

        MenuItem.objects.filter(name=menu_name), 

    and since MenuItem has a foreign key relationship with its child items, select_related is used to fetch all the child items in a single query. 

## Screenshots:

<img width="1425" alt="image" src="https://user-images.githubusercontent.com/104210649/231416220-4542ef23-779f-4827-bc02-8cac419f9731.png">
<img width="1392" alt="image" src="https://user-images.githubusercontent.com/104210649/231416364-4d70df20-f6f3-4566-8de0-7639a9aa0b14.png">
<img width="849" alt="image" src="https://user-images.githubusercontent.com/104210649/231416525-16775f7d-d5b7-49fc-adfa-cb3f3bce3c74.png">
<img width="572" alt="image" src="https://user-images.githubusercontent.com/104210649/231416841-ee40f758-68a7-455c-bccf-564448b88610.png">
<img width="627" alt="image" src="https://user-images.githubusercontent.com/104210649/231416962-e8da0b39-061c-4a10-a192-6560bb20227a.png">


## 🚀 About Me

I am a skilled software developer with over three years of experience in delivering secure and reliable applications. My expertise lies in back-end user development and AI-related work. 

Still learning Golang,AWS..etc.

Check my Portfolio : https://bibinkunjumon.me.uk/



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://bibinkunjumon.me.uk/)


