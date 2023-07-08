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
            content=f'Webhook received: {event["type"]}',
            status=200
        )
