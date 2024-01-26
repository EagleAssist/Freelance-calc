from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rate
from .serializers import RateSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
class CalculateView(APIView):
    def get(self, request):
        return render(request, 'calculate_price.html')

    def post(self, request):
        rate_type = request.data.get('rate_type')
        complexity = request.data.get('complexity')
        num_pages = request.data.get('num_pages')

        try:
            rate = Rate.objects.get(rate_type=rate_type, complexity=complexity)
            total_cost = rate.rate * int(num_pages)
            return Response({'total_cost': total_cost})
        except Rate.DoesNotExist:
            return Response({'error': 'Rate not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception for debugging
            print(e)
            return Response({'error': 'Internal server error'}, status=500)
        
        