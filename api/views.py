from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Product
from .serializers import serialize_product
from django.views.decorators.csrf import csrf_exempt
import json

'''
- GET: 리소스 조회
- POST: 새 리소스를 생성
- PUT: 기존 리소스 수정
- DELETE: 리소스 삭제
'''



@csrf_exempt
def product_list(request):
  if request.method == 'GET':   # 정보 조회
    products = Product.objects.all()
    # 가져온 Product 객체들을 JSON 형식으로 직렬화(serialize) 및 반환
    return JsonResponse({'products' : [serialize_product(p) for p in products]}, safe=False)
  elif request.method == 'POST' :     # 새로운 정보 생성
    data = json.loads(request.body)   # 요청의 본문(body)에서 데이터를 추출
    product = Product.objects.create(**data)    # 추출된 데이터를 사용하여 새로운 Product 객체를 생성
    return JsonResponse(serialize_product(product), status=201)   # 상태 코드 201(Created)과 함께 직렬화된 데이터를 JsonResponse를 통해 반환
  

@csrf_exempt
def product_detail(request,pk):
  try:
    product = Product.objects.get(pk=pk)    # 해당 제품(Product) 가져오기
  except Product.DoesNotExist:
    return HttpResponse(status=404)
  
  if request.method == 'GET' :     # 정보 조회 
    return JsonResponse(serialize_product(product))   # JSON 형식으로 직렬화하여 반환
  elif request.method == 'PUT' :      # 기존 리소스 수정
    data = json.loads(request.body)     # 요청 본문(body)에서 데이터 추출
    for field, value in data.items():       # POST 요청에서 받은 데이터를 딕셔너리 형태로 반환 (딕셔너리의 각 항목은 필드 이름(field name)과 해당 값(value)으로 구성)
      setattr(product, field, value)      # 추출된 데이터를 사용하여 제품 객체의 필드 업데이트
    product.save()                        # 저장
    return JsonResponse(serialize_product(product))   # 업데이트된 제품을 JSON 형식으로 직렬화하여 반환
  elif request.method == 'DELETE' : 
    product.delete()
    return HttpResponse(status=204)