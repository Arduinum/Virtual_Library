from django import template


register = template.Library()

@register.filter
def adding_authors(authors_list):
    """Вернёт строку с именами авторов книг"""
    
    authors_str = str()
    authors_name_list = [author.name for author in authors_list if author.name.isalpha()]

    for name in authors_name_list:
        authors_str += name
        if authors_name_list[-1] != name:
            authors_str += ', '

    return authors_str

@register.filter
def is_book_detail(request_path):
    if 'books' in request_path:
        if request_path.split('/')[-2].isdigit():
            return True
    return False
