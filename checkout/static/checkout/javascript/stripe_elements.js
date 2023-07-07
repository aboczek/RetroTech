const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#212529',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {
    style: style
});
card.mount('#card-element');

// Handle for realtime validation errors on the card element.
card.addEventListener('change', function (e) {
    const errorDiv = document.querySelector('#card-errors');
    if (e.error) {
        const html = `*<span class="mt-2">${e.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit button

const form = document.querySelector('#payment-form');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.querySelector('#card-errors');
            var html = `
                *<span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});