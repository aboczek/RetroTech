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
    $('#load-spinner').fadeToggle(100);
    $('#load-spinner').css('display', 'flex');

    const saveDetails = Boolean($('#save-details').attr('checked'));
    // Form using csrf token in the form
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_details': saveDetails,
    };
    const url = '/cache-checkout-data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county_state.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county_state.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                let errorDiv = document.querySelector('#card-errors');
                let html = `
                *<span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#load-spinner').fadeToggle(100);
                $('#load-spinner').css('display', 'flex');
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
    }).fail(function () {
        // reloading page, error will be in django messages
        location.reload();
    })
});