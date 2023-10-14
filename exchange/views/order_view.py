from rest_framework.views import APIView, status
from rest_framework.response import Response
from ..requests_validations.order_request_validation import OrderRequestValidation
from ..services.order_services.order_price_calculator import OrderPriceCalculator
from ..services.order_services.checkout_services.checkout_service_factory import CheckoutServiceFactory


class OrderView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.order_price_calculator = OrderPriceCalculator()
        self.checkout_service_factory = CheckoutServiceFactory()

    def post(self, request):

        request_validation = OrderRequestValidation(data=request.data)

        if request_validation.is_valid():
            validated_data = request_validation.validated_data
            amount = validated_data['amount']
            currency_symbol = validated_data['currency_symbol']
            order_price_in_usd = self.order_price_calculator.calculate_price(currency_symbol, amount)
            checkout_service = self.checkout_service_factory.create_checkout_service(order_price_in_usd, currency_symbol)
            order_request_result = checkout_service.process_order()

            return Response({order_request_result}, status=200)
        else:
            return Response(request_validation.errors, status=status.HTTP_400_BAD_REQUEST)
