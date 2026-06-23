from django.http import JsonResponse,HttpResponse


def greet_user(request):
    return HttpResponse('Welcome to Ecommerce!')


# Create your views here.
# @api_view(['GET'])
# def get_products(request, id):
#     if not id:
#         products = Product.objects.all()
#     else:
#         products = Product.objects.get(id=id)
#     return Response({'products': products})
git commit -m "added .gitignore and readme.MD. untracked .venv,.idea"