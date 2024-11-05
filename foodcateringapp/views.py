from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .forms import CardForm, FoodMenuEditForm, AddressForm, ChangeFirstNameForm, ChangeEmailForm, ChangePhoneForm, ChangeProfileImageForm, ShippingAddressForm, CheckoutForm, BookingForm
from .models import (
    FoodItem,
    FoodMenu,
    Cart,
    Order,
    OrderItem,
    Transaction,
    CartItem,
    UserProfile,
    ShippingAddress,
    Card,
    CateringSet,
    Booking,
    Event,
)
from django.http import JsonResponse
from django.utils import timezone
import json
from django.db.models.functions import TruncMonth, TruncWeek, TruncYear
import plotly.graph_objs as go
from django.db.models.functions import ExtractWeek, ExtractYear
from django.db.models import Sum, Count
from django.db.models import Min, Max
import calendar
from itertools import chain
from datetime import date
from django.utils.timezone import now
import datetime
from plotly.offline import plot
from django.utils.dateparse import parse_date
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.


@login_required
def mainIndex(request):
    events = Event.objects.all()
    return render(request, "foodcateringapp/index.html", {"events": events})


def foodmenu(request):
    menus = FoodMenu.objects.all()
    return render(request, "foodcateringapp/foodMenu.html", {"menus": menus})


def addFoodMenu(request):
    # render page for now
    return render(request, "foodcateringapp/addFoodMenu.html")


def checkout(request):
    user_cart = Cart.objects.get(user=request.user)
    # Retrieve the cart items associated with the user's cart
    cart_items = user_cart.cartitem_set.all()

    # Calculate the total price based on the items in the cart
    total_price = sum(item.food_item.price *
                      item.quantity for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            request.user.update_membership(total_price)
            redirect("foodcateringapp:profile")
        else:
            print(form.errors)
    else:
        form = CheckoutForm()
    context = {"cart_items": cart_items,
               "total_price": total_price, "form": form}

    return render(request, "foodcateringapp/CheckoutPage.html", context)


def get_updated_total_price(request):
    selected_option = request.GET.get("selected_option")
    user_cart = Cart.objects.get(user=request.user)
    cart_items = user_cart.cartitem_set.all()

    total_price = sum(item.food_item.price *
                      item.quantity for item in cart_items)

    if selected_option == "standard":
        total_price += 2.99
    elif selected_option == "express":
        total_price += 4.99
    elif selected_option == "saver":
        total_price += 0.99

    return JsonResponse({"updated_price": total_price})


def editcart(request):
    return render(request, "foodcateringapp/EditCartPage.html")


def editmenu(request):
    return render(request, "foodcateringapp/edit-menu.html")


def editmenuindex(request):
    return render(request, "foodcateringapp/edit_menu_index.html")


def adminIndex(request):
    return render(request, "foodcateringapp/admin_index.html")


def adminTest(request):
    return render(request, "foodcateringapp/admin_test.html")


def trackOrderIndex(request):
    orders = Order.objects.all()
    return render(request, "foodcateringapp/trackorder_index.html", {"orders": orders})


def get_orders(request):
    # Assuming you have a method to serialize orders to JSON
    orders = Order.objects.all().values()
    return JsonResponse({"orders": list(orders)}, safe=False)


def displayorder(request):
    orders = Order.objects.filter(
        Q(status="Preparing") | Q(status="Out of kitchen"))
    return render(request, "foodcateringapp/OrderDisplay.html", {"order": orders})


def food_menu_detail(request, menu_id):
    menu = get_object_or_404(FoodMenu, pk=menu_id)
    items = FoodItem.objects.filter(foodmenu=menu)
    return render(
        request, "foodcateringapp/food_menu_detail.html", {
            "menu": menu, "items": items}
    )


def checkoutcopy(request):
    """Add a new topic."""

    if request.method != "POST":
        # No data submitted; create a blank form.
        card_form = CardForm()
        address_form = AddressForm()

    # else:
    # no need to process form data as checkoutcopy is only rendering the form

    # Display a blank or invalid form.
    context = {"card_form": card_form, "address_form": address_form}
    return render(request, "foodcateringapp/checkoutpagecopy.html", context)


def savepaymentdetails(request):
    print("function was called")
    if request.method == 'POST':
        data = json.loads(request.body)
        number = data.get('number')
        cvv = data.get('cvv')
        user_id = request.user.id  # Assuming user is authenticated

        card = Card(
            card_number = number,
            expiry_date = "2000-12-11",
            cvc = cvv,
            user_id=user_id
        )
        card.save()

        return JsonResponse({'message': 'Card saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def saveshippingaddress(request):
    print("function was called")
    if request.method == 'POST':
        data = json.loads(request.body)
        address = data.get('address')
        postal = data.get('postal')
        city = data.get('city')
        user_id = request.user.id  # Assuming user is authenticated

        shipping_address = ShippingAddress(
            name="",  # Add your logic for name and address_line fields
            address_line1=address,
            address_line2="",  # Add your logic for address_line2 field
            postal=postal,
            city=city,
            user_id=user_id
        )
        shipping_address.save()

        return JsonResponse({'message': 'Address saved successfully'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def edit_menu(request, foodmenu_id):
    food_menu = FoodMenu.objects.get(id=foodmenu_id)
    if request.method == "POST":
        form = FoodMenuEditForm(
            request.POST, request.FILES, instance=food_menu)
        if form.is_valid():
            form.save()
            # Redirect after successful edit
            return redirect("foodcateringapp:editmenuindex")
    else:
        # Add an error message
        messages.error(request, "Order placement failed. Please log in.")
        # Redirect back to the checkout page
        return redirect('foodcateringapp:checkout')

        messages.error(
            request, "Order placement failed. Please log in."
        )  # Add an error message
        return redirect(
            "foodcateringapp:checkout"
        )  # Redirect back to the checkout page


def foodcart(request):
    cart_items = CartItem.objects.all()
    total_price = 0
    for item in cart_items:
        total_price = total_price + item.food_item.price * item.quantity

    total_price = round(total_price, 2)

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "editable": True,
        "renderedFrom": "foodcart"
    }

    return render(request, "foodcateringapp/foodcart.html", context)


# add to cart new


def add_to_cart(request, item_id):
    menu_id = request.POST.get("menu_id")
    print(f"Item ID: {item_id}")

    # Get the food item to add to the cart
    food_item = get_object_or_404(FoodItem, pk=item_id)
    print(f"Food Item: {food_item}")

    # Check if the user is authenticated (logged in)
    if request.user.is_authenticated:
        user = request.user
        # Try to get the user's cart; create one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=user)
        print(f"Cart: {cart}, Created: {created}")

        if request.method == "POST":
            # Get the quantity from the form
            quantity = int(request.POST.get("quantity", 1))
            print(f"Quantity: {quantity}")

            if quantity > 0:
                # Check if the item is already in the user's cart
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart, food_item=food_item
                )
                print(f"Cart Item: {cart_item}, Created: {created}")

                if not created:
                    cart_item.quantity += quantity
                    cart_item.save()
                    print(f"Cart Item Quantity Updated: {cart_item.quantity}")

                # Update the total of the cart
                # there is no total field for cart
                cart.total = sum(
                    cart_item.food_item.price * cart_item.quantity
                    for cart_item in cart.cartitem_set.all()
                )
                cart.save()

    return redirect("foodcateringapp:food_menu_detail", menu_id=menu_id)


def increase_cart_item(request, product_id):
    cart_item = get_object_or_404(CartItem, pk=product_id)
    if request.method == "POST":
        cart_item.quantity += 1  # Decrease the quantity

        cart_item.save()  # Save the updated quantity

    return redirect("foodcateringapp:foodcart")


def decrease_cart_item(request, product_id):
    cart_item = get_object_or_404(CartItem, pk=product_id)
    if request.method == "POST":
        cart_item.quantity -= 1  # Decrease the quantity
        if cart_item.quantity <= 0:
            cart_item.delete()  # Remove the item if quantity is zero or less
        else:
            cart_item.save()  # Save the updated quantity

    return redirect("foodcateringapp:foodcart")


def food_item_sold(request):
    order_items = OrderItem.objects.all()
    food_item_quantity = {}

    for order_item2 in order_items:
        order_item2.total_price = order_item2.fooditem.price * \
            order_item2.quantity  # Calculate total price for the order item
        order_item2.save()

    for order_item in order_items:
        food_name = order_item.fooditem.name
        if food_name in food_item_quantity:
            # Add the quantity sold for existing food item
            food_item_quantity[food_name]['quantity'] += order_item.quantity
            # Update the total price for the existing food item
            food_item_quantity[food_name]['total_price'] += order_item.quantity * \
                order_item.fooditem.price
        else:
            # Create a new entry in the dictionary
            food_item_quantity[food_name] = {
                'quantity': order_item.quantity,
                'total_price': order_item.quantity * order_item.fooditem.price
            }

    food_item_data = [{'food_item': name, 'quantity_sold': data['quantity'], 'total_price': data['total_price']}
                      for name, data in food_item_quantity.items()]

    context = {
        "food_item_data": food_item_data,
        "order_items": order_items,
    }

    return render(request, 'foodcateringapp/FoodItemSold.html', context)

# def food_item_sold(request):
#     order_items = OrderItem.objects.all()
#     for order_item2 in order_items:
#         order_item2.total_price = order_item2.fooditem.price * order_item2.quantity  # Calculate total price for the order item
#         order_item2.save()

#     context = {
#         "order_items": order_items,
#     }

#     return render(request, 'foodcateringapp/FoodItemSold.html',context)

# new place order


def place_order(request):
    if request.method == "POST" and request.user.is_authenticated:
        user = request.user

        delivery_option = request.POST.get("delivery-option")

        # Calculate the delivery fee based on the selected option
        delivery_fee = 0.0  # Default value for 'saver' option
        if delivery_option == "standard":
            delivery_fee = 2.99
        elif delivery_option == "express":
            delivery_fee = 4.99
        elif delivery_option == "saver":
            delivery_fee += 0.99

        # Calculate the total price based on the items in the cart and the delivery fee
        total_price_response = get_updated_total_price(request)
        totalprice = json.loads(total_price_response.content.decode("utf-8")).get(
            "updated_price"
        )
        totalprice += delivery_fee
        # update membership based on spending
        user.update_membership(totalprice)

        payment_method = request.POST["payment-method"]

        # Create a new order instance
        order = Order(user=user, status="Preparing",
                      total_price=round(totalprice, 2))
        order.save()

        user_cart = Cart.objects.get(user=user)
        cart_items = user_cart.cartitem_set.all()

        # Loop through the cart items and create an OrderItem for each item linked to the order
        for cart_item in cart_items:
            order_item = OrderItem(fooditem=cart_item.food_item, orderID=order)
            order_item.quantity = cart_item.quantity
            order_item.save()

        # Clear the old cart by removing the association with the user's cart
        user_cart.completed = True
        user_cart.cartitem_set.all().delete()
        user_cart.save()

    transaction = Transaction(
        payment_method=payment_method,
        date=timezone.now(),
        user=user,
        total=round(totalprice, 2),
    )
    transaction.save()

    # context = {'order': order, 'totalprice':totalprice}
    return redirect("foodcateringapp:trackorderindex")


def chart_view(request):
    filter_type = request.GET.get('filter', 'day')
    year = request.GET.get('year')
    month = request.GET.get('month')
    day = request.GET.get('day')

    transactions = Transaction.objects.all()
    labels = []
    data = []
    chart = None
    error_message = None

    if filter_type == 'all_time':
        start_year = transactions.aggregate(start_year=Min('date'))[
            'start_year'].year
        end_year = transactions.aggregate(end_year=Max('date'))[
            'end_year'].year
        years = range(start_year, end_year + 1)
        transactions_by_year = transactions.annotate(year=ExtractYear(
            'date')).values('year').annotate(total=Sum('total'))
        transactions_by_year = {t['year']: t['total']
                                for t in transactions_by_year}
        for year in years:
            labels.append(year)
            data.append(transactions_by_year.get(year, 0))

    elif filter_type == 'year' and year:
        monthly_transactions = transactions.filter(date__year=year).annotate(
            month=TruncMonth('date')).values('month').annotate(total=Sum('total')).order_by('month')
        for month in range(1, 13):
            month_label = datetime.date(1900, month, 1).strftime('%B')
            transaction = next(
                (t for t in monthly_transactions if t['month'].month == month), None)
            labels.append(month_label)
            data.append(transaction['total'] if transaction else 0)

    elif filter_type == 'month' and year and month:
        # Find the first and last day of the month
        first_day = datetime.date(int(year), int(month), 1)
        last_day = datetime.date(int(year), int(
            month), calendar.monthrange(int(year), int(month))[1])
        # Generate a list of week numbers
        weeks = [first_day.isocalendar()[1]]
        while first_day < last_day:
            first_day += datetime.timedelta(days=7)
            weeks.append(first_day.isocalendar()[1])
        transactions_by_week = transactions.filter(date__year=year, date__month=month).annotate(
            week=ExtractWeek('date')).values('week').annotate(total=Sum('total'))
        transactions_by_week = {t['week']: t['total']
                                for t in transactions_by_week}
        for week in weeks:
            labels.append(f"Week {week}")
            data.append(transactions_by_week.get(week, 0))

    else:
        error_message = "Please provide the required parameters for the selected filter."

    if not transactions.exists():  # Check if the queryset is empty
        error_message = "This date has no transactions, please try again with a new date."
    else:
        # Plot if we have data
        if labels and data:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=labels, y=data, mode='lines+markers'))
            chart = plot(fig, output_type='div')

            # line_color = '#967e76'  # A color for the line
            # marker_color = '#d7c0ae'  # A color for the markers

            fig.add_trace(go.Scatter(
                x=labels,
                y=data,
                mode='lines+markers',
                # Darker color for the line, increased width
                line=dict(color='#334D66', width=3),
                # Brighter color and larger size for markers
                marker=dict(color='#967e76', size=10)
            ))

            # Customize chart layout with colors
            fig.update_layout(
                title='Transaction Data Line Chart',
                title_font_color='#334D66',
                paper_bgcolor='#fbf0df',  # Background color outside the plotting area
                plot_bgcolor='#FFDBCC',  # Background color of the plotting area
                font_color='#334D66',
                xaxis=dict(
                    title='Date' if filter_type == 'date' else 'Month' if filter_type == 'month' else 'Year',
                    gridcolor='#d7c0ae'  # Color for the gridlines
                ),
                yaxis=dict(
                    title='Total',
                    gridcolor='#d7c0ae'  # Color for the gridlines
                )
            )

            # Convert the figure to HTML
            chart = fig.to_html(
                full_html=False, default_height=500, default_width=800)

    context = {
        'graph': chart,
        'error_message': error_message,
        'filter_type': filter_type,
        'year': year,
        'month': month,
        'day': day
    }
    return render(request, 'admin/chartgraph.html', context)


def graph_view(request):
    selected_date_str = request.GET.get(
        'date', timezone.now().strftime('%Y-%m-%d'))
    selected_date = parse_date(selected_date_str)

    start_of_selected_day = timezone.make_aware(
        timezone.datetime.combine(selected_date, timezone.datetime.min.time()))
    end_of_selected_day = start_of_selected_day + timezone.timedelta(days=1)

    category_totals = Transaction.objects.filter(
        date__gte=start_of_selected_day, date__lt=end_of_selected_day
    ).values('user__order__orderitem__fooditem__foodmenu__categories').annotate(
        total_amount=Sum('total')
    ).order_by()

    labels = [item['user__order__orderitem__fooditem__foodmenu__categories']
              for item in category_totals]
    values = [item['total_amount'] for item in category_totals]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        # Bright, contrasting colors
        marker=dict(colors=['#007acc', '#ffd700', '#dc143c']),
    )])

    # Update layout settings
    fig.update_layout(
        title='Transactions by Food Menu Category',
        title_font_color='#334D66',  # Dark color for title text
        paper_bgcolor='#fbf0df',  # Background color outside the plotting area
        plot_bgcolor='#FFDBCC',  # Light background of the plotting area
        font_color='#334D66',  # Dark font for better contrast and readability
        margin=dict(l=0, r=0, t=50, b=20)
    )

    chart = plot(fig, output_type='div')

    context = {
        'chart': chart,
        'today': selected_date_str,
    }

    return render(request, 'admin/chartgraph.html', context)


@csrf_exempt
def update_order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        new_status = request.POST.get("new_status")
        order.status = new_status
        order.save()
        return JsonResponse({"success": True})
    except Order.DoesNotExist:
        return JsonResponse({"success": False, "error": "Order not found"})


@csrf_exempt
def update_name(request):
    user = request.user

    if request.method == 'POST':
        form = ChangeFirstNameForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['new_first_name']
            user.first_name = new_first_name
            user.save()
            return redirect('foodcateringapp:profile')

    # If the form is not valid or it's a GET request, render the profile page.
    return redirect('foodcateringapp:profile')


@csrf_exempt
def update_email(request):
    user = request.user

    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['new_email']
            user.email = new_first_name
            user.save()
            return redirect('foodcateringapp:profile')

    # If the form is not valid or it's a GET request, render the profile page.
    return redirect('foodcateringapp:profile')


@csrf_exempt
def update_phone(request):
    user = request.user

    if request.method == 'POST':
        profile = UserProfile.objects.get(user=user)

        form = ChangePhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['new_phone']
            profile.phone_number = phone
            user.save()
            profile.save()
            return redirect('foodcateringapp:profile')

    # If the form is not valid or it's a GET request, render the profile page.
    return redirect('foodcateringapp:profile')


@csrf_exempt
def update_profile_image(request):
    if request.method == 'POST':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = ChangeProfileImageForm(
            request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('foodcateringapp:profile')

    return redirect('foodcateringapp:profile')


@login_required
def profilePage(request):
    user = request.user
    first_name = user.first_name
    last_name = user.last_name
    membership_tier = user.tier
    shipping_addresses = ShippingAddress.objects.filter(user=user.id)
    payment_method = Card.objects.filter(user=user.id)

    try:
        profile = UserProfile.objects.get(user=user)
        # Existing code for user profile
    except UserProfile.DoesNotExist:
        # Handle the case where UserProfile does not exist
        # For example, you can create a UserProfile on the fly
        profile = UserProfile.objects.create(
            user=user, phone_number='N\A', profile_image="Image/FEGCWHITE.png")

    phone_number = profile.phone_number
    picture = profile.profile_image
    # Create a context dictionary with user data
    context = {
        'user': user,
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'shipping_addresses': shipping_addresses,
        'payment_method': payment_method,
        'profile_image':  picture,
        'form': ChangeFirstNameForm(),
        'form_email': ChangeEmailForm(),
        'form_phone': ChangePhoneForm(),
        'form_profile_image': ChangeProfileImageForm(),
        'membership_tier': membership_tier,
    }
    return render(request, "foodcateringapp/profilePage.html", context)


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Important to maintain the user's session
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('foodcateringapp:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'foodcateringapp/change_password.html', {'form': form})


def edit_shipping_address(request, address_id):
    # Retrieve the address object
    address = get_object_or_404(ShippingAddress, id=address_id)

    # Check if the request method is POST
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            # Redirect to the profile page or any other appropriate page
            return redirect('foodcateringapp:profile')
    else:
        # If the request method is not POST, create a form with the address instance
        form = ShippingAddressForm(instance=address)

    # Pass the address and form to the template context
    context = {
        'address': address,
        'form': form,
    }

    # Render the template
    return render(request, 'foodcateringapp/edit_shipping_address.html', context)


def edit_payment(request, card_id):
    # Retrieve the address object
    card = get_object_or_404(Card, id=card_id)

    # Check if the request method is POST
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            # Redirect to the profile page or any other appropriate page
            return redirect('foodcateringapp:profile')
    else:
        # If the request method is not POST, create a form with the address instance
        form = CardForm(instance=card)

    # Pass the address and form to the template context
    context = {
        'card': card,
        'form': form,
    }

    # Render the template
    return render(request, 'foodcateringapp/edit_payment.html', context)


def display_catering_sets(request):
    # Retrieve all catering sets from the database and prefetch related CateringSetItem instances
    catering_sets = CateringSet.objects.prefetch_related("set_items").all()

    context = {
        "catering_sets": catering_sets,
    }
    return render(request, "foodcateringapp/catering_sets.html", context)


def booking(request):
    bookings = Booking.objects.filter(user=request.user)
    context = {
        "bookings": bookings,
    }
    return render(request, "foodcateringapp/booking.html", context)


def membership_page(request):
    # Replace 'membership_tier_value' with the actual value for the client's membership tier
    # Replace with your logic to fetch the membership tier

    tiers = {
        "Entry": 0,
        "Silver": 500,
        "Gold": 1000,
        "Diamond": 2000,
    }
    current_user = request.user
    points = current_user.membership_points
    next_tier_index = next((i for i, (tier, points_required) in enumerate(
        tiers.items()) if points_required > points), len(tiers))

    if next_tier_index < len(tiers):
        next_tier_name = list(tiers.keys())[next_tier_index]
        next_tier_points = list(tiers.values())[next_tier_index]
        # print(f"Next tier: {next_tier_name}, Points required: {next_tier_points - points}")
        points_until_next_tier = next_tier_points-points
    else:
        points_until_next_tier = 0

    membership_tier_value = current_user.tier

    context = {
        "points": points,
        "membership_tier": membership_tier_value,
        "points_until_next_tier": points_until_next_tier,
        "next_tier_name": next_tier_name,
        "next_tier_points": next_tier_points,
    }

    return render(request, 'foodcateringapp/membership_page.html', context)

# def book(request):
#     booking_id = 0
#     if request.method == 'POST':
#         form = BookingForm(request.POST)

#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.user = request.user  # Set the booking user to the current user
#             booking.save()
#             messages.success(request, 'Booking successful!')
#             booking_id = booking.id
#             # next_url = request.POST.get('next', '')
#             return redirect('foodcateringapp:confirmbooking', booking_id = booking_id)  # Redirect to a confirmation page
#     else:
#         form = BookingForm()

#     catering_sets = CateringSet.objects.all()

#     context = {
#         'form': form,
#         'catering_sets': catering_sets,
#         'bookingID' : booking_id,
#     }
#     return render(request, 'foodcateringapp/book.html', context)


def book(request, catering_set_id=None):
    booking_id = 0

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful!')
            booking_id = booking.id
            return redirect('foodcateringapp:makebooking', booking_id=booking_id)
    else:
        # If catering_set_id is provided in the URL, pre-select the corresponding catering set
        catering_set = None
        if catering_set_id:
            try:
                catering_set = CateringSet.objects.get(pk=catering_set_id)
            except CateringSet.DoesNotExist:
                pass

        form = BookingForm(initial={'catering_set': catering_set})

    catering_sets = CateringSet.objects.all()

    context = {
        'form': form,
        'catering_sets': catering_sets,
        'bookingID': booking_id,
    }
    return render(request, 'foodcateringapp/book.html', context)


def make_booking(request, booking_id):
    try:
        # Get the booking associated with the booking_id
        booking = Booking.objects.get(pk=booking_id)

        # Get the CateringSet and its FoodItems
        catering_set = booking.catering_set
        food_items = catering_set.set_items.all()

        # Add FoodItems to the user's cart
        # user_cart = request.user.cart
        # Try to get the user's cart; create one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=request.user)
        for catering_set_item in food_items:
            food_item = catering_set_item.food_item
            quantity = catering_set_item.quantity

            # Check if the item is already in the user's cart
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, food_item=food_item)

            if created:
                cart_item.quantity = quantity
                cart_item.save()

        cart_items = CartItem.objects.all()
        total_price = 0
        for item in cart_items:
            total_price = total_price + item.food_item.price * item.quantity

        total_price = round(total_price, 2)

        context = {
            "cart_items": cart_items,
            "total_price": total_price,
            "editable": False,
            "renderedFrom": "make_booking"
        }

        return render(request, "foodcateringapp/foodcart.html", context)

    except Booking.DoesNotExist:
        # Handle the case where the booking is not found
        return render(request, 'foodcateringapp/booking_not_found.html')

# def foodcart(request):
