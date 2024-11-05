from django.shortcuts import reverse, resolve
from django.http import HttpResponseRedirect
from .models import Cart, Booking

# class ClearCartMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
        
#         # Check if the user navigated back to the 'Book' page from the 'Checkout' page
#         if request.path == reverse('foodcateringapp:book') and request.GET.get('from') == 'checkout':
#             try:
#                 # Clear the cart for the user
#                 cart = Cart.objects.get(user=request.user)
#                 cart.delete()
#             except Cart.DoesNotExist:
#                 pass
            
#             try:
#                 # Delete the booking
#                 booking = Booking.objects.get(user=request.user)
#                 booking.delete()
#             except Booking.DoesNotExist:
#                 pass
        
#             # Redirect back to the 'CateringSets' page after clearing cart and deleting booking
#             return HttpResponseRedirect(reverse('foodcateringapp:cateringsets'))

#         return response
    

class ClearCartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if the current view matches the 'book' view
        resolved_view = resolve(request.path_info)
        if resolved_view.url_name == 'book':
            # Ensure the parameters are correctly extracted based on your URL configuration
            catering_set_id = resolved_view.kwargs.get('catering_set_id')

            # Perform cart clearing and booking deletion logic here
            # Retrieve the user's cart and delete it
            try:
                cart = Cart.objects.get(user=request.user)
                cart.delete()
            except Cart.DoesNotExist:
                pass  # Handle if the cart doesn't exist
            
            # Retrieve and delete the booking
            try:
                booking = Booking.objects.get(user=request.user, catering_set_id=catering_set_id)
                booking.delete()
            except Booking.DoesNotExist:
                pass  # Handle if the booking doesn't exist

            return HttpResponseRedirect(reverse('foodcateringapp:cateringsets'))

        
        return response
