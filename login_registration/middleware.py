# from django.http import JsonResponse
# from django.utils.deprecation import MiddlewareMixin

# class LoginRequiredMiddleware(MiddlewareMixin):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if not request.user.is_authenticated:
#             if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#                 return JsonResponse({'error': 'You must be logged in to access this page.'}, status=401)
#             else:
#                 return JsonResponse({'error': 'You must be logged in to access this page.'}, status=401)
#         return None
    