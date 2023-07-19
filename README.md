# RetroTech shop

Welcome to my project about shop called **RetroTech**. This shop is about handheld consoles mainly but will have other ones as well like PlayStation or Xbox and ability to sell them to me.

<img src="docs/website-image.png" alt="home page" width="900">

## Table of content:

- [Motivation](#motivation)
- [User Experience](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Website Goals](#website-goals)
    - [Requirements](#requirements)
    - [Expectations](#expectations)
    - [Design](#design)
    - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Tablet](#tablet)
        - [Mobile](#mobile)
- [Authentication](#authentication)
- [Data Structure](#data-structure)
- [Website Structure](#website-structure)
- [Technology, Frameworks and Programs used](#technology-frameworks-and-programs-used)
    - [Languages](#languages)
    - [Frameworks and programs used](#frameworks-and-programs-used)
- [Features](#features)
    - [Navigation bar](#navigation)
- [Testing](#testing)
- [Testing user stories](#testing-user-stories)
- [Deployment](#deployment)
- [Credits](#credits)

# Motivation

Motivation for this project is to sell and buy consoles on this website.

# User Experience (UX)

## User Stories
- User Story
    - As a user, I want to land on main page.
    - As a user, I want to be able to navigate through main page.
    - As a user, I want to be able to navigate through categories.
    - As a user, I want to be able to contact owner to sell my console or handheld device.
    - As a user, I want to be able to navigate through sales page.
    - As a user, I want to be able to buy device of the website.
    - As a user, I want to be able to see what kind of device website has to offer.
    - As a user, I want to be able to create account.
    - As a user, I want to be able to store my details on my account.
    - As a user, I want to be able to add item to shopping bag.
    - As a user, I want to be able to continue shopping after adding one or more items in the bag.
    - As a user, I want to be able to pay for my shopping with Stripe.
    - As a user, I want to be able to sign up for newsletter.

[Back to top](#)

## Website Goals

Websites goal is to promote my RetroTech shop and gain new customers.

## Agile Methodology

- This project uses Agile methodology with kanban board, each user story represents as **EPIC** and its smaller issues are **TASKS**
- I have implemented **iterations** every week every thursday was iteration last week before deadline will be last iteration till deadline date.

    <details><summary>Kanban board screenshot</summary>
    <img src="docs/kanban-board.png" alt="kanban board"/>
    </details>
    <br>

## Requirements

- Home page.
- Categories with products.
- Checkout.
- Sales.
- Newsletter.
- Sell to us.
- Login system.
- Storing cusomter details if logged in.

## Expectations

- I expect my website will attract new customers.
- I expect my website will have home page.
- I expect my website will have categories and products.
- I expect my website will let customers buy devices from my website.
- I expect my website will let customers sell their devices to me if they are in good condition.
- I expect my website will let customers add more than one item into bag.
- I expect my website will let users create profile account and store their details.

## Design

- Colors
    - Colors used on website are:

    - Gold: #ffc107;

        <img src="docs/gold.png" alt="gold color" width="15%"/>

    - Purple: #6A02F2;

        <img src="docs/purple.png" alt="purple color" width="15%"/>
    
    - Grey: ##4d4e4f;

        <img src="docs/d-grey.png" alt="grey color" width="15%"/>

    - light grey: #eeebeb;

        <img src="docs/light-grey.png" alt="light grey color" width="15%"/>

    - white: #fff;

        <img src="docs/white.png" alt="white color" width="15%"/>

- Fonts:

    Font was used default from Boostrap 5, [Helvetica Neue](https://fontsgeek.com/helvetica-neue-font), [Helvetica](https://fontsgeek.com/helvetica-font), [Arial](https://fontsgeek.com/arial-font), and [sans-serif](https://fontsgeek.com/sans-serif-font) in its default font stack.

- Images: 

    - [Freepik](https://www.freepik.com/free-vector/reviews-concept-landing-page_5156335.htm#query=reviews&position=27&from_view=search&track=locales")

    - [Currys.ie](https://www.currys.ie/)

    - [Smyths](https://www.smythstoys.com/ie/en-ie/)

    - [Retroid](https://www.goretroid.com/)

    - [Anbernic](https://anbernic.com/)

[Back to top](#)

## Wireframes

- Home page.

	**placeholder**

- Products/Categories.

	**placeholder**

- Checkout.

	**placeholder**

- Sales.

	**placeholder**

- Front end admin panel

	**placeholder**

- Profile account

	**placeholder**

- Newsletter

    **placeholder**


# Authentication and Security

### Authentication

- Project uses [Allauth](https://django-allauth.readthedocs.io/en/latest/) as login system, pages were adjusted and styled. Emailing system to login, email confirmation, password recovery and so on works and is being sent.

- Unwanted visitors trying to access restricted pages in project will be redirected to home with message that they are allowed on this site. ``@Login_required`` and 

    ```
    if not request.user.is_superuser:
        messages.error(request, 'You arent allowed there! \
                        redirecting to home page.')
        return redirect(reverse('home'))
        ```

### Security

- All secret keys are stored in **env.py** or stored in variables in [Heroku](https://www.heroku.com/).

# Data Structure

## Database

Category:
| Object | Field |
|---|---|
| ID | is automatically generated |
| name | CharField |
| frontend_name | CharField |

name is given category_choices of handheld, console, games, accessories.
<hr>

Item:
| Object | Field |
|---|---|
| ID | is automatically generated |
| category | ForeignKey to Category model |
| sku_number | CharField |
| product_name | CharField |
| product_model | CharField |
| product_description | TextField |
| price | DecimalField |
| original_price | DecimalField |
| sale | Boolean |
| featured | Boolean |
| image_one | CloudinaryField |
| image_two | CloudinaryField |
| image_three | CloudinaryField |

<hr>

SellToUS:
| Object | Field |
|---|---|
| ID | is automatically generated |
| full_name | CharField |
| email | EmailField |
| brand | CharField |
| model | CharField |
| grade | CharField |
| description | TextField |
| sell_image_one | CloudinaryField |
| sell_image_two | CloudinaryField |
| sell_image_three | CloudinaryField |

<hr>

UserProfile:
| Object | Field |
|---|---|
| ID | is automatically generated |
| user | OnetoOneField with User |
| default_phone_number | CharField |
| default_town_or_city | CharField |
| default_street_address1 | CharField |
| default_street_address2 | CharField |
| default_postcode | CharField |
| default_county_state | CharField |
| default_country | CountryField |

User is imported from django.contrib.auth.models
<hr>

Newsletter:
| Object | Field |
|---|---|
| ID | is automatically generated |
| news_email | EmailField |

newsletter email is called news_email because I made my own context_processors that would pull all email id's from websie when they were provided. This way it prevents unwanted newsletter signups.

<hr>

Order:
| Object | Field |
|---|---|
| ID | is automatically generated |
| order_number | CharField |
| user_profile | ForeignKey to UserProfile |
| full_name | CharField |
| email | EmailField |
| phone_number | CharField |
| country | CountryField |
| postcode | CharField |
| town_or_city | CharField |
| street_address1 | CharField |
| street_address2 | CharField |
| county_state | CharField |
| date | DateTimeField |
| order_total | DecimalField |
| grand_total | DecimalField |
| original_basket | TextField |
| stripe_pid | CharField |

order_total adds up all lineitems,
grand_total is order_total.
order_number is generated by uuid4 with hex and Upper letters.

<hr>

OrderLineItem:
| Object | Field |
|---|---|
| ID | is automatically generated |
| order | ForeignKey to Order |
| item | ForeignKey to Item |
| quantity | IntegerField |
| lineitem_total | DecimalField |

lineitem_total is calculated items price * quantity.

<hr>

<img src="docs/db.png" alt="Item model">

## Logic

<img src="docs/logic.png" alt="website logic" width="1000">

# Website Structure

- Most of website structure comes from Bootstrap itself, and rest is just overrides to make it look nicer.

|  Screen size |  Breakpoint |
|---|---|
| extra small | >= 320px |
| small | >= 576px |
| medium | >= 768px |
| Custom | 768 >= 900 |
| Custom | >= 990 | 

# Technology, Frameworks and Libraries used.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

- [Jquery](https://en.wikipedia.org/wiki/JQuery)

## Frameworks and Libraries used.

- [Django](https://www.djangoproject.com/) Python-based web framework that follows the model–template–views architectural pattern.

- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) HTTP server interface.

- [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.

- [Stripe](https://stripe.com/) Payments.

- [Bootstrap](https://getbootstrap.com/) Bootstrap 5 was used in this project.

- [FontAwesome](https://fontawesome.com/) Icons used in this project.

## Tools

- [Heroku](https://www.heroku.com) Deployment of website.

- [ElephantSQL](https://www.elephantsql.com/) Database storing all schemas and data.

- [Cloudinary](https://cloudinary.com/) Storing static files and images.

- [Balsamiq](https://balsamiq.com/) Wireframes.

- [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/) used to generate new key.

- [Favicon](https://favicon.io/favicon-generator/) Favicon generator.

- [Freepik](https://www.freepik.com/) Freepik images

# Features

- Responsive on all devices.
- Custom Front end admin panel.
- Profile accounts.
- Checkout with Stripe payments.
- Products and Categories.
- Newsletter
- Emails on newsletter signup, sell to us and if checkout is successful.

## Navigation
	
	
**placeholder**

# Testing

1. W3C HTML Validator, CSS Validator, CI Pylinter and JShint.

    - HTML All files have been tested no errors and no warnings on my own code.

	    <img src="docs/indexhtml.png" alt="html validator" width="700">

    - CSS all files te sted.
        
        - style.css(main css)
        <img src="docs/main-css.png" alt="css validator" width="700">

        - home.css
        <img src="docs/home.png" alt="css validator" width="700">

        - items.css
        <img src="docs/items.png" alt="css validator" width="700">

        - checkout.css
        <img src="docs/checkout.png" alt="css validator" width="700">

    - Python using CI Pylinter.

        - Home app.

            <img src="docs/home-forms.png" alt="python validator" width="700">

            <img src="docs/home-models.png" alt="python validator" width="700">

            <img src="docs/home-views.png" alt="python validator" width="700">

        - Items app.

            <img src="docs/items-forms.png" alt="python validator" width="700">

            <img src="docs/items-models.png" alt="python validator" width="700">

            <img src="docs/items-sale-signals.png" alt="python validator" width="700">

            <img src="docs/items-views.png" alt="python validator" width="700">

        - Basket app.

            <img src="docs/views-basket.png" alt="python validator" width="700">

            <img src="docs/price-quantity.png" alt="python validator" width="700">

            <img src="docs/context.png" alt="python validator" width="700">

        - Checkout app.

            <img src="docs/forms-checkout.png" alt="python validator" width="700">

            <img src="docs/models-checkout.png" alt="python validator" width="700">

            <img src="docs/signals-checkout.png" alt="python validator" width="700">

            <img src="docs/views-checkout.png" alt="python validator" width="700">

        - Retrotech project.

            <img src="docs/context-processors.png" alt="python validator">


    - Javascript.

        - Autoclosing script for messages.

            <img src="docs/autoclose.png" alt="javascript">


2. Testing on website.

	- Lighthouse:

        - Desktop

            <img src="docs/lighthouse-desktop.png" alt="lighthouse score desktop">

        - Mobile

            <img src="docs/lighthouse-mobile.png" alt="lighthouse score mobile">

3. Testing on portable devices.

	I have tested project on my OnePLus phone and in Developer tools. Everything seems to be fine.

    Two screenshots as an example.

    - Mobile phone.
        <img src="docs/testing-phone.png" alt="testing phone">

    - Tablet.
        <img src="docs/testing-tablet.png" alt="testing tablet">

4. Automated and Manual testing.

	**placeholder**

5. Known bugs.

	**placeholder**

6. Bugs fixed.

	**placeholder**

# Testing user stories

| **Feature**                     | **Action**                          | **Expected Result**                                                                  | **Result** |
|---------------------------------|-------------------------------------|--------------------------------------------------------------------------------------|-------------------|
| **placeholder** | **placeholder** | **placeholder** | PASS |
<details><summary>Picture</summary>
<img src="" alt=""/>
</details>
<br>

# Deployment

## Programs needed:

### Heroku

**placeholder**

### GitHub

**placeholder**

### ElephantSQL

**placeholder**

## Local Development

**placeholder**

**loads of placeholders**

**loads of placeholders**

**loads of placeholders**

**loads of placeholders**

**loads of placeholders**

# Credits 

- [Simen Daehlin](https://github.com/Eventyret) My Mentor.
- [Freepik](https://www.freepik.com/free-vector/reviews-concept-landing-page_5156335.htm#query=reviews&position=27&from_view=search&track=locales") Freepiks website linked to person that created image.
- [Currys.ie](https://www.currys.ie/) Used for images for products.
- [Smyths](https://www.smythstoys.com/ie/en-ie/) Used for images for products.
- [Retroid](https://www.goretroid.com/) Used for images for products.
- [Anbernic](https://anbernic.com/) Used for images for products.
- [The W3C Markup Validation Service](https://validator.w3.org/) Validation of HTML.
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Validation of CSS.
- [Python linter](https://pep8ci.herokuapp.com/#) used to lint python code.
- [JShint](https://jshint.com/) used to lint javascript.
- [Autoprefixer](https://autoprefixer.github.io/) used to prefix CSS.