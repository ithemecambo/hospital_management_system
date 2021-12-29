# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
#
# DEFAULT_PAGE = 1
#
#
# class CustomPagination(PageNumberPagination):
#     page = DEFAULT_PAGE
#     limit = 10
#     page_size_query_param = 'limit'
#
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'total': self.page.paginator.count,
#             'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
#             'limit': int(self.request.GET.get('limit', self.limit)),
#             'results': data
#         })
#
