import requests
from django.shortcuts import render
from django.http import HttpResponse

TARGET_URL = 'https://www.youtube.com/'  # Сайт, который будет транслироваться

def show_site(request):
    try:
        # Делаем запрос к целевому сайту
        response = requests.get(TARGET_URL)
        response.raise_for_status()  # Проверяем успешность запроса
        # Возвращаем содержимое сайта
        return HttpResponse(response.content)
    except requests.RequestException as e:
        return HttpResponse(f"Error fetching the site: {e}", status=500)