const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);
const stripe = Stripe(stripe_public_key);
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