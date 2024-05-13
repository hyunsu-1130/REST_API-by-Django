from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product
import json

'''
class ProductTests(APITestCase):
    def test_create_product(self):
      # 새로운 제품 생성 및 응답 검증
      url = reverse('api:product_list')   # product_list라는 주소로 data를 전송을 위함
      data = {'name' : 'Test Product', 'description' : 'good', 'price': 20, 'in_stock' : True}
      response = self.client.post(url, data, format='json')       # post를 사용하여 제품 생성
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(Product.objects.count(), 1)
      self.assertEqual(Product.objects.get().name, 'Test Product')

    def test_get_product(self):
        # 제품 목록을 가져오고 결과 검증
        response = self.client.get(reverse('api:product_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''

'''
# 'Products API'를 통해 특정 제품을 삭제하는 API 엔드포인트를 테스트하는 코드
class ProductTest(APITestCase):
  def test_delete_product(self):
    # 특정 제품 삭제 및 결과 검증
    # ㄱ. 임시 제품 생성
    product = Product.objects.create(name='Test Product2', description='bad', price=30, in_stock=True)
    # ㄴ. url 구성 : (reverse(주소, args=[삭제 대상 id])
    url = reverse('api:product_detail', args=[product.id])
    # ㄷ. 요청 보내기
    response = self.client.delete(url)
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Product.objects.count(), 0)
'''

# 'Products API'를 통해 특정 제품의 정보 조회
# 응답 코드 200인지(정상응답) 확인
# 응답받은 Product의 name 속성이 처음에 넣은 name 속성과 일치하는지 확인
class ProductRetrieveTests(APITestCase):
  def setUp(self):    # 제품 생성 및 URL 생성
    self.product = Product.objects.create(name='Test Product3', description='Not bad', price=50, in_stock=True)
    self.url = reverse('api:product_detail', args=[self.product.id])

  def test_retrieve_product(self):  
    response = self.client.get(self.url)    # 생성된 URL에 GET 요청을 보내서 제품 검색
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    response_data = json.loads(response.content.decode('utf-8'))     # 바이트 문자열을 디코딩하여 JSON으로 변환
    self.assertEqual(response_data['name'], 'Test Product3')
