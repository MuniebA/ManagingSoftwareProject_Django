
from django import forms
from .models import Card, FoodMenu, ShippingAddress, UserProfile, Booking


class FoodMenuEditForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        fields = ['name', 'description', 'categories', 'foodmenuImage']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'expiry_date', 'cvc']


class AddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            'address_line1',
            'address_line2',
            'postal',
            'city'
        ]


class ChangeFirstNameForm(forms.Form):
    new_first_name = forms.CharField(max_length=30)


class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(label="New Email")


class ChangePhoneForm(forms.Form):
    new_phone = forms.CharField(max_length=30)


class ChangeProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'address_line1', 'address_line2']


class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    ship_address = forms.CharField(label='Shipping Address', max_length=255)
    ship_city = forms.CharField(label='Shipping City', max_length=100)
    ship_postal_code = forms.CharField(
        label='Shipping Postal Code', max_length=20)
    phone = forms.CharField(label='Phone', max_length=20)
    DELIVERY_OPTIONS = [
        ('standard', 'Standard (RM2.99)'),
        ('express', 'Express (RM4.99)'),
        ('saver', 'Saver (RM0.99)'),
    ]
    delivery_option = forms.ChoiceField(
        label='Delivery Option', choices=DELIVERY_OPTIONS, widget=forms.RadioSelect(attrs={'id': 'id_delivery_option'})
    )

    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('cards', 'Cards'),
        ('ewallet', 'E-Wallet'),
    ]

    payment_method = forms.ChoiceField(
        label='Payment Method', choices=PAYMENT_CHOICES, widget=forms.RadioSelect(attrs={'id': 'id_payment_method'}))

    card_type = forms.ChoiceField(label='Card Type', choices=[
        ('credit-card', 'Credit Card'),
        ('debit-card', 'Debit Card'),
    ], required=False)

    card_number = forms.CharField(
        label='Card Number', max_length=16, required=False)
    cvv = forms.CharField(label='CVV', max_length=4, required=False)

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if self.cleaned_data.get('payment_method') == 'cards' and not card_number:
            raise forms.ValidationError(
                'Card number is required for card payment.')
        return card_number

    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        if self.cleaned_data.get('payment_method') == 'cards' and not cvv:
            raise forms.ValidationError('CVV is required for card payment.')
        return cvv

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['catering_set', 'date', 'time', 'additional_info']