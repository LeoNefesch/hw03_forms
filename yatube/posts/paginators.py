from django.core.paginator import Paginator

NUMBER_OF_ROWS: int = 10


def post_paginator(posts, request):
    paginator = Paginator(posts, NUMBER_OF_ROWS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
