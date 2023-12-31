from django import template


register = template.Library()

@register.filter
def adding_authors(authors_list):
    """Вернёт строку с именами авторов книг"""
    authors_str = str()
    authors_name_list = [
        author.name for author in authors_list if ''.join(author.name.split(' ')).isalpha()
    ]

    for name in authors_name_list:
        authors_str += name
        if authors_name_list[-1] != name:
            authors_str += ', '

    return authors_str
