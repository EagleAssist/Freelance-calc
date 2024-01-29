from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rate,History
from .serializers import RateSerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.db.models import Case, When
from django.views import View
from django.core.serializers import serialize


# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login')
class CalculateView(APIView):
    def get(self, request):
        return render(request, 'calculate_price.html')

    def post(self, request):
        print(request.__dict__)
        user=request.user
        rate_type = request.data.get('rate_type')
        complexity = request.data.get('complexity')
        num_pages = request.data.get('num_pages')

        try:
            rate = Rate.objects.get(rate_type=rate_type, complexity=complexity)
            total_cost = rate.rate * int(num_pages)
            
            history=History(user_his=user,hist_rate_type=rate_type,hist_complexity=complexity,hist_num_pages=num_pages,hist_rate=total_cost)
            history.save()
            print(f"User: {user}")
            return Response({'total_cost': total_cost})
       
        except Rate.DoesNotExist:
            return Response({'error': 'Rate not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception for debugging
            print(e)
            # return Response({'error': 'Internal server error'}, status=500)
            return Response({'error'+str(e)}, status=500)
# class history(APIView):
#     def get(self, request,*args, **kwargs):
#         user = request.user
#         history_of_user = History.objects.filter(user_his=user)
#         # history_of_user=list(history_of_user)
#         print(history_of_user)
#         return render(request, "history.html", {'history_data':history_of_user})
        
class history(View):
    template_name = 'history.html'

    def get(self, request, *args, **kwargs):
        # Fetch the current user's history data
        user_history = History.objects.filter(user_his=request.user)
        
        serialized_history = serialize('json', user_history)
        # Pass the data to the template
        context = {'history_data': serialized_history}
        print(context)
        return render(request, self.template_name, context)
def logout_view(request):
    logout(request)
    
    return redirect('/login')