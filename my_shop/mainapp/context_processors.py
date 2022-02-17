# MENU_LINKS = [
#     {"url": "main", "name": "домой"},
#     {"url": "contact", "name": "контакты"},
#     {"url": "products:all", "name": "продукты"},
# ]


def menu_links(request):
    return {
        'menu_links': [
            {"url": "main", "name": "домой"},
            {"url": "contact", "name": "контакты"},
            {"url": "products:all", "name": "продукты"},
        ]
    }