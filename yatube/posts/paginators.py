from django.core.paginator import Paginator

NUMBER_OF_ROWS = 10


def post_paginator(posts, request):
    paginator = Paginator(posts, NUMBER_OF_ROWS)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
