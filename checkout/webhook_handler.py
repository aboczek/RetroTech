from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handler for stripe webhooks.
    """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handling generic, unknown and unexpected webhook events.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handling payment intent succeeded.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handling payment intent failed.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
