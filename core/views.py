from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse
import math

# Create your views here.

# I pray this works please abeg 
def is_armstrong(n):
    if n < 0:  
        return False
    num_str = str(abs(n))
    r_power = len(num_str)
    total_n = sum(int(digit) ** r_power for digit in num_str)
    return total_n == n

def is_prime(n):
    if n < 2:  
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:  # Perfect numbers are positive integers
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def get_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

@api_view(['GET'])
def my_data(request):
    try:
        number = request.GET.get('number', '')
        
        try:
            number = int(number)
        except ValueError:
            return JsonResponse({
                "number": number,
                "error": True
            }, status=400)
        
        # Get fun fact from numbersapi.com
        response = requests.get(f'http://numbersapi.com/{number}/math')
        fun_fact = response.text if response.status_code == 200 else number
        
        result = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": get_properties(number),
            "digit_sum": get_digit_sum(number),
            "fun_fact": fun_fact
        }
        
        return JsonResponse(result, status=200)
        
    except Exception as e:
        return JsonResponse({
            "number": str(e),
            "error": True
        }, status=400)
    



