# Music City
<hr>

Music City - is a web platform for guitar players. 
It provides not only music instruments for sale, but the lessons of 
how to play the guitar as well. Each lesson may include picture, text
and video. And the lessons are grouped in playlists for easier navigation.
To get access to this functionality the user should purchase one
of the available subscriptions or try demo subscription for free.
The lessons may be used to promote the instruments and accessories and
enhance the company sells.

The purpose of the application is to create handy platform for musicians, where 
they can buy musical instruments, equipment and accessories, and also to learn 
how to play the guitar. 

What sets this platform apart is its unique combination of offering both musical
instruments and music lessons in one place. Users have access to everything they 
need, from purchasing instruments to learning how to play them, all within a single, 
integrated platform.

## E-commerce business model
<hr>
Being the comprehensive web-application for selling physical and 
intellectual products - music instruments, equipment and lessons 
it requires however marketing techniques and strategies to be implemented
to create a recognisable and successful brand.

### Search Engine Optimization
The website content is optimized for better ranking in search engines, however
the site owner should provide each product with the full and easy to read description
paying attention to using the key-words naturally inserted to the text.

### Content marketing
The main website content is lessons, so the site admin should keep them updated and make
sure that new lessons adding. The best practise will be to have the playlists for guitar
players of all levels and music of various styles. To make sure that the users will be
interested in returning and keep their subscriptions active a good idea will be to create 
a playlist with the site news, special offers for the subscribed users, catching videos
with hints, advices and challenges. This playlist should be updated frequently, meaning
that old videos are deleted and new ones uploaded.

### Social media marketing
It's important to post content to the social media on regular basis. Our customers are 
creative people, not only professional musicians, but amateurs and beginners as well,
so it's important to keep their interest to the platform by posting videos of tutorials
how to play popular and viral songs, posts about famous musicians and bands etc. It's a 
good way to communicate with the potential customers and create positive, diverse, and
friendly community.

### Email marketing
The web application provides site owner with the newsletter functionality for building 
email sale strategy.

Newsletter emails should be informative and catching, bringing the users attention to
the targeted products. It's important to avoid frequent emails, which may be considered 
spam and make users to unsubscribe from the newsletter. A good practise will be to provide
the subscribed users with the special offers, not available for the rest. For example, free
branded merch when buying something, unique posts etc.

### Influencer marketing
Another way to enhance interest to the brand is collaboration with bloggers and YouTube,
Instagram advertise. Being mentioned in music blogger video may bring the most relevant
users to the platform.


## UX
<hr>

### Colour scheme

- `#000` used for primary text
- `#e67300` used for higlights
- `#fff` used for secondary text
- `#444`, `#555`, `#888`,`#999`, `#ddd` were used for background colours

### Design mockups for desktop and mobile views
![image of draft mockups](https://i.ibb.co/JKNsYYR/IMG-6864.jpg)

## Features
<hr>

- ### Responsive design
![responsive design image](https://i.ibb.co/H2LGvmb/resp.png)

Using Bootstrap and custom CSS make the web application look good
both on mobile devices and desktop screens.


 - ### Homepage

![imgage of the home page](https://i.ibb.co/Jrbb0cj/2024-05-16-08-45-55.png)

On the homepage of the website user can see the special offers section. 
It is automatically and randomly generated from the products which have
two prices, where old price is the higher, it is crossed out, while the
other price is marked red to show the user that the product has better 
price now.

- ### Lessons
![image of lessons section](https://i.ibb.co/yFBwK2h/2024-05-16-09-05-13.png)
The website contains lessons section for those who would like to learn how
to play the guitar. These lessons are available on subscription. For consistency
the lessons of the one topic gathered in groups (or playlists) which allows user 
to pick the topic he would like to learn and see the lessons related to it.
Playlists which don't contain any lessons never shows up in the page. Initially,
the lessons collapsed in playlist and user can reveal them by clicking on the arrow 
button. 
![image of the lesson](https://i.ibb.co/K7PxDck/2024-05-16-09-07-29.png)
The page of the lessons may contain image, text and video. On the screenshot you
can see that this lesson contains a video from YouTube. It is in frame, so the site
owner can easily add it by just adding a builtin link for it. If the site administer 
didn't upload the cover image for lesson, it will be taken from YouTube thumbnail if
the lesson contains the video or just a default image for lessons covers. User can 
easily navigate to the next or previous lesson, or go back to all lessons by clicking
buttons and the bottom.

- ### Subscription
As mentioned, the lessons available on subscription only. If a user without a
subscription clicks on 'lessons' on the menu, he will be redirected to the page
with subscriptions.
![image of subscription page](https://i.ibb.co/7JCmq89/2024-05-16-09-19-57.png)
We recommend to leave one free
subscription to provide the user with the opportunity to try it (and fall in love with
our lessons) before buying the subscription.
The user can use it only once. If the database with subscribed users contains
a record, the option of free subscription will not be shown. To purchase subscription,
the user will only need his credit card as this is an online service, no delivery info
required. 
The site admin can manage the subscriptions: name, corresponding image, description, 
price, promotional price (optionally) and duration. 
Additionally, the site admin can hide the subscription, for example, the time limited
special offer. It allows admin to keep it for future, instead of deleting and creating
it again.

- ### Products
![image of products page](https://i.ibb.co/n84Dd1D/2024-05-16-10-10-53.png)
The products page shows the user available products. They can be shown by categories,
sorted by price or filtered by brand. The user can add products to the bag and when he's
happy with his order - tu purchase it, using Stripe payments.

- ### Shopping Bag
- ![image of the bag section](https://i.ibb.co/hYYFMwm/2024-05-16-10-13-03.png)
The shopping bag feature allows a user to see what he picked, price, quantity and total cost.
A user can change quantity of an item or remove it from the bag if he changed his mind.


- ### User profile Page
![image of profile section](https://i.ibb.co/DpzQwf5/2024-05-16-10-14-36.png)
The registered user can navigate to his profile page, where he can update his personal information
and view his order history

- ### Newsletter
![imags of newsletter subscription section](https://i.ibb.co/mhFvWk3/2024-09-06-17-22-45.png)
The registered users can subscribe to the newsletter from Profile page. If the user is not subscribed to it, 
there will be a brief instruction how to subscribe and the form to enter email address 
(prefilled with the one user used to register) and 'Subscribe' button. If user is subscribed already,
the instruction will be how to unsubscribe, same form and 'Unsubscribe' button. This functionality creates or
removes entry from database. 

Site admin can send a letter to all subscribed users by choosing 'Send a newsletter' option in dropdown menu
of the user icon in the header. It opens the page with subject and body field with button 'Send' in the bottom.
![image of the newsletter creating page](https://i.ibb.co/1RXfLFg/2024-09-07-10-15-06.png)


- ### Site admin features
![image of the ux admin feature](https://i.ibb.co/QdbRysf/2024-05-16-10-16-01.png)
The admin of the site do not have to use django administration panel to manage the store, subscriptions
and lessons. It can be done on the related pages of the web site.

<hr>


## Database Design

![image of database structure](https://i.ibb.co/grbVH7C/2024-10-01-12-52-49.png)


[LucidApp](https://lucid.app/lucidchart/ff0f4383-925c-4df7-a389-8f6034b68372/edit?invitationId=inv_0e2a15b2-6bab-4088-b676-c6bc89f11e7a) was used to create an ERD to visualise the tables within the database and their relationships.

- ### Product 

| ID          | Type            | Relation             |
|-------------|-----------------|----------------------|
| category    | ForeignKey      | FK to Category model |
| sku         | CharField       |                      |
| name        | CharField       |                      |
| brand       | CharField       |                      |
| description | CharField       |                      |
| price       | DecimalField    |                      |
| old_price   | DecimalField    |                      |
| image_url   | URLField        |                      |
| image       | CloudinaryField |                      |

- ### Category 

| ID            | Type      | Relation |
|---------------|-----------|----------|
| name          | CharField |          |
| friendly_name | CharField |          |

- ### Order 

| ID              | Type          | Relation                |
|-----------------|---------------|-------------------------|
| order_number    | CharField     |                         |
| user_profile    | ForeignKey    | FK to UserProfile model |
| full_name       | CharField     |                         |
| email           | EmailField    |                         |
| phone_number    | CharField     |                         |
| country         | CountryField  |                         |
| postcode        | CharField     |                         |
| town_or_city    | CharField     |                         |
| street_address1 | CharField     |                         |
| street_address2 | CharField     |                         |
| county          | CharField     |                         |
| date            | DateTimeField |                         |
| delivery_cost   | DecimalField  |                         |
| order_total     | DecimalField  |                         |
| grand_total     | DecimalField  |                         |
| original_bag    | TextField     |                         |
| stripe_pid      | CharField     |                         |

- ### OrderLineItem 

| ID             | Type         | Relation            |
|----------------|--------------|---------------------|
| order          | ForeignKey   | FK to Order model   |
| product        | ForeignKey   | FK to Product model |
| quantity       | IntegerField |                     |
| lineitem_total | DecimalField |                     |


- ### Subscription 

| ID                | Type            | Relation |
|-------------------|-----------------|----------|
| name              | CharField       |          |
| description       | TextField       |          |
| duration          | IntegerField    |          |
| price             | DecimalField    |          |
| promotional_price | DecimalField    |          |
| is_active         | BooleanField    |          |
| image             | CloudinaryField |          |

- ### UserSubscription 

| ID                | Type          | Relation         |
|-------------------|---------------|------------------|
| user              | OneToOneField | FK to User model |
| subscribed        | BooleanField  |                  |
| subscription_name | CharField     |                  |
| start_date        | DateField     |                  |
| expiry_date       | DateField     |                  |

- ### Lesson 

| ID          | Type            | Relation             |
|-------------|-----------------|----------------------|
| name        | CharField       |                      |
| playlist    | ForeignKey      | FK to Playlist model |
| number      | IntegerField    |                      |
| cover_image | CloudinaryField |                      |
| img_url     | URLField        |                      |
| text        | TextField       |                      |
| video_url   | URLField        |                      |


- ### Playlist 

| ID            | Type      | Relation             |
|---------------|-----------|----------------------|
| name          | CharField |                      |
| friendly_name | CharField |                      |


- ### UserProfile 

| ID                       | Type          | Relation         |
|--------------------------|---------------|------------------|
| user                     | OneToOneField | FK to User model |
| default_phone_number     | CharField     |                  |
| default_street_address1  | CharField     |                  |
| default_street_address2  | CharField     |                  |
| default_town_or_city     | CharField     |                  |
| default_county           | CharField     |                  |
| default_postcode         | CharField     |                  |
| default_country          | CountryField  |                  |


- ### NewsSubscriber 

| ID    | Type          | Relation         |
|-------|---------------|------------------|
| user  | OneToOneField | FK to User model |
| email | EmailField    |                  |


## Testing
<hr>

### Code validation
<hr>

- ### HTML
For HTML validation I have used [W3C Validator](https://validator.w3.org/)


| Result for page                                                                                                                    | Errors    |
|------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2F)                                    | No errors |
| [Subscriptions](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Flessons%2Fsubscription%2F)  | No errors |
| [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Fproducts%2F)                     | No errors |
| [Sign Up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Fsignup%2F)             | No errors |
| [Log In](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Flogin%2F)               | No errors |

- ### CSS
For CSS validation I have used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

No errors found

- ### Python
All python files passed CI Python Linter. All issues fixed:
- line too long
- no blank line in the end of the file
- 2 blank lines expected found 1

## User stories testing


| User story                                                                                                                                                                             | Screenshot                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| As a site user I can create an account so that allows me to access my profile                                                                                                          | ![image of the registration section](https://i.ibb.co/zHJQcD8/2024-10-02-11-25-23.png)            |
| As a site user I can login or logout so that gives me access to my information and special site features                                                                               | ![image of the sign in page](https://i.ibb.co/FJhm6j2/2024-10-02-11-27-31.png)                    |
| As a site user I can recover my password so that allows me to set up a new password if I forgot it                                                                                     | ![image of the password reset page](https://i.ibb.co/ChxjKzp/2024-10-02-11-35-15.png)             |
| As a site user I can receive an email when registering so that ensure that my email was set up correct                                                                                 | ![image of the verification email](https://i.ibb.co/b5msxtC/2024-10-02-11-38-35.png)              |
| As a site user I can have a personal user profile so that allows me to view my personal information and activity history                                                               | ![image of the user profile page](https://i.ibb.co/5ck24nC/2024-10-02-11-40-36.png)               |
| As a site user I can locate and use navigation panel so I can access different parts of the website                                                                                    | ![image of the navigation panel](https://i.ibb.co/QQjHhbh/2024-10-02-11-44-04.png)                |
| As a site user I can see the subscription types so that allows me to chose one                                                                                                         | ![image of subscription page](https://i.ibb.co/7JCmq89/2024-05-16-09-19-57.png)                   |
| As a site owner I can add, edit and hide subscriptions so that allows me to update subscription types                                                                                  | ![image of the subscription management section](https://i.ibb.co/vkxXnk7/2024-10-02-11-48-30.png) |
| As a site owner I can see the subscribed users so that allows me to plan sells                                                                                                         | ![image of the subscribed users django panel](https://i.ibb.co/9VPD9Ky/2024-10-02-11-49-57.png)   |
| As a site user I can navigate to the product page so I can browse thorough available products                                                                                          | ![image of the products page](https://i.ibb.co/H7J643J/2024-10-02-11-52-08.png)                   |
| As a site user I can use the search form so that allows me to find a product faster                                                                                                    | ![image of the search bar](https://i.ibb.co/7RXvNxW/2024-10-02-11-43-44.png)                      |
| As a site user I can filter the products by categories so that allows me to see the pool of products I'm interested in                                                                 | ![image of the product category bar](https://i.ibb.co/ydDzm4Q/2024-10-02-11-55-15.png)            |
| As a site user I can sort products by brand so that allows me to chose among the products of the specific brand                                                                        | ![image of the brand filters](https://i.ibb.co/dt7vBdc/2024-10-02-11-56-35.png)                   |
| As a site user I can view the shopping bag so that allows me to see which products were chosen                                                                                         | ![image of the shopping bag page](https://i.ibb.co/wpyhdn2/2024-10-02-11-59-36.png)               |
| As a site user I can edit and remove items in my shopping bag so that allows me to manage the products I want to purchase                                                              | ![image of the shopping bag editing](https://i.ibb.co/rx0qT4p/2024-10-02-12-00-34.png)            |
| As a site user I can enter my billing info so that allows me to pay for my order                                                                                                       | ![image of the billing info form](https://i.ibb.co/fMt2L8T/2024-10-02-12-03-43.png)               |
| As a site user I can get an order confirmation so that ensure me that it was successful                                                                                                | ![image of the order confirmation page](https://i.ibb.co/JzQLB5c/2024-10-02-12-05-18.png)         |
| As a site user I can receive an email after submitting an order so that allows me to have the confirmation of my order in my mailbox                                                   | ![image of the order confirmation email](https://i.ibb.co/JpDDxbf/2024-10-02-12-27-45.png)                                                        |
| As a subscribed user I can view the lessons so that shows me purchased product                                                                                                         | ![image of the lessons section](https://i.ibb.co/VVWX6Lx/2024-10-02-12-06-59.png)                 |
| As a subscribed user I can go to the next, previous lesson or back to all lessons so that allows me easily navigate                                                                    | ![image of the lesson navigation](https://i.ibb.co/SmKZ9C1/2024-10-02-12-07-26.png)               |
| As a site user I can see custom 404 page instead of default one so that improves my user experience allowing to navigate to the other site sections                                    | ![image of custom 404 page](https://i.ibb.co/9gV8qjw/2024-10-02-12-07-48.png)                     |
| As a site user I can subscribe to the newsletter so that allows me to receive site news and special offers                                                                             | ![image of the newsletter subscription section](https://i.ibb.co/4jYYVHJ/2024-10-02-12-08-09.png) |
| As a site owner I can send newsletter to all subscribed users so that allows me to inform them about news, special etc.                                                                | ![image of the newsletter creation page](https://i.ibb.co/511b9pW/2024-10-02-12-09-48.png)        |


## Manual Testing
<hr>

### Home page, header and footer

- user (unregistered) role

| Action                                             | Before              | After                                                                     | Result       |
|----------------------------------------------------|---------------------|---------------------------------------------------------------------------|--------------|
| Click on logo                                      | Any page of website | Homepage renders                                                          | Test Success |
| Hover over the search bar button                   | White icon          | Orange icon                                                               | Test Success |
| Hover over the user button                         | White icon          | Orange icon                                                               | Test Success |
| Hover over the trolley button                      | White icon          | Orange icon                                                               | Test Success |
| Click on the search bar button (empty form)        | Any page            | Product page and warning message 'You didn't eneter any search criteria'  | Test Success |
| Click on the search bar button ('guitar' enetered) | Any page            | Product page contains only products with 'guitar' in title or description | Test Success |
| Click on the search bar button ('flower' enetered) | Any page            | Product page with text 'Sorry... No products found                        | Test Success |
| Click on the user button                           | Any page            | Dropdown items list with Register and Login options                       | Test Success |
| Hover over the Register                            | White text          | Orange background and black text                                          | Test Success |
| Hover over the Login                               | White text          | Orange background and black text                                          | Test Success |
| Click on Register                                  | Any page            | Sign Up page                                                              | Test Success |
| Click on Login                                     | Any page            | Login page                                                                | Test Success |
| Click on trolley button                            | Any page            | Bag page                                                                  | Test Success |
| Hover over the main navigation panel               | Orange text         | White text                                                                | Test Success |
| Click on 'Guitars' on the navigation panel         | White text          | Dropdown menu with sub-categories                                         | Test Success |
| Click on 'Equipment' on the navigation panel       | White text          | Dropdown menu with sub-categories                                         | Test Success |
| Click on 'Other' on the navigation panel           | White text          | Dropdown menu with sub-categories                                         | Test Success |
| Hover over sub-categories                          | White text          | Orange background and black text                                          | Test Success |
| Hover over product cards in 'special offers'       | Grey border         | Orange border                                                             | Test Success |
| Click on product card in 'special offers'          | Homepage            | Page of the product on the card                                           | Test Success |
| Hover over social media icons in footer            | Orange icons        | White icons                                                               | Test Success |
| Click on Facebook icon                             | Homepage            | Facebook mockup page in the new tab                                       | Test Success |
| Click on Youtube icon                              | Homepage            | YouTube Homepage in the new tab                                           | Test Success |
| Click on X(twitter) icon                           | Homepage            | X(twitter) Homepage in the new tab                                        | Test Success |
| Click on Instagram icon                            | Homepage            | Instagram Homepage in the new tab                                         | Test Success |
| Hover over social media icons in footer            | Orange text         | White text                                                                | Test Success |
| Click on 'Music Network'                           | Homepage            | musicnetwork.ie Homepage in the new tab                                   | Test Success |
| Click on 'Royal Irish Academy of Music'            | Homepage            | riam.ie Homepage in the new tab                                           | Test Success |

- user (registered) role

| Action                    | Before              | After                                                  | Result       |
|---------------------------|---------------------|--------------------------------------------------------|--------------|
| Click on the user button  | Any page            | Dropdown items list with My profile and Logout options | Test Success |
| Hover over the My profile | White text          | Orange background and black text                       | Test Success |
| Hover over the Logout     | White text          | Orange background and black text                       | Test Success |
| Click on My profile       | Any page            | User profile page                                      | Test Success |
| Click on Logout           | Any page            | Logout page                                            | Test Success |

- admin role

| Action                                      | Before                              | After                                                                      | Result       |
|---------------------------------------------|-------------------------------------|----------------------------------------------------------------------------|--------------|
| Click on the user button                    | Any page                            | Dropdown items list with Product Management, My profile and Logout options | Test Success |
| Hover over the Product management           | White text                          | Orange background and black text                                           | Test Success |
| Click on Product management                 | Any page                            | Add product page                                                           | Test Success |
| Hover over 'Add Product' button             | Orange text, transparent background | White text and orange background                                           | Test Success |
| Hover over 'Cancel' button                  | Black text transparent background   | White text black background                                                | Test Success |
| Click on 'Add Product' button (empty form)  | Product management page             | Same page, notification appears on the blank field                         | Test Success |
| Click on 'Add Product' button (filled form) | Product management page             | Same page, notification appears that product is successfully added         | Test Success |
| Click on 'Cancel' button                    | Product management page             | Products page                                                              | Test Success |

### Lessons

- unregistered user role

| Action                           | Before                             | After                                                                        | Result       |
|----------------------------------|------------------------------------|------------------------------------------------------------------------------|--------------|
| Click on 'Lessons on the navbar' | Any page                           | website page with the available subscriptions                                | Test Success |
| Hover over 'Subscribe buttons'   | Orange text, white background      | White text orange background                                                 | Test Success |
| Click on 'subscribe' (FREE)      | Subscriptions page                 | Same page, toast warning 'Please login or signup'                            | Test Success |
| Click on 'subscribe' (paid)      | Subscriptions page                 | Subscription details page. 'Please login or signup' instead of payment form. | Test Success |
| Hover over 'login' and 'signup'  | Orange text                        | White text                                                                   | Test Success |
| Click on 'login'                 | Subscription details page          | Login page                                                                   | Test Success |
| Click on 'signup'                | Subscription details page          | Signup page                                                                  | Test Success |
| Hover over 'back' button         | Black text transparent background  | White text black background                                                  | Test Success |
| Click on 'back' button           | Subscription details page          | Subscriptions page                                                           | Test Success |
| Hover over 'checkout' button     | The button is inactive, light-grey | Nothing changes                                                              | Test Success |
| Click on 'checkout' button       | The button is inactive, light-grey | Nothing changes                                                              | Test Success |


- registered user (unsubscribed) role

| Action                                           | Before                                 | After                                                                | Result       |
|--------------------------------------------------|----------------------------------------|----------------------------------------------------------------------|--------------|
| Click on 'subscribe' (FREE)                      | Subscriptions page                     | Lessons page and notification 'Your free subscription is active now' | Test Success |
| Click on 'subscribe' (paid)                      | Subscriptions page                     | Subscription details page with field for the card number             | Test Success |
| Hover over 'checkout' button                     | Orange text and transparent background | White text and orange background                                     | Test Success |
| Hover over 'back' button                         | Black text and transparent background  | White text and black background                                      | Test Success |
| Click on 'checkout' button (empty card field)    | Subscription details page              | Same page, alert that field is empty                                 | Test Success |
| Click on 'checkout' button (4242 4242 4242 4242) | Subscription details page              | Lessons page, notification 'Subscription Purchased'                  | Test Success |
| Click on 'back' button                           | Subscription details page              | Subscription page (with all available subscriptions)                 | Test Success |


- registered user (subscribed) role

| Action                                          | Before                              | After                                               | Result       |
|-------------------------------------------------|-------------------------------------|-----------------------------------------------------|--------------|
| Click on 'Lessons in the navigation bar'        | Any page                            | Lessons page with playlists                         | Test Success |
| Hover over arrow down button on the playlist    | Orange text transparent background  | White text and orange background                    | Test Success |
| Click on arrow down button on the playlist      | Collapsed lessons                   | Lessons list appears and button changes to arrow up | Test Success |
| Click on arrow up button on the playlist        | Lessons in playlist revealeed       | Lessons collapsed and button changes to arrow down  | Test Success |
| Hover over lesson image                         | White border                        | Orange border                                       | Test Success |
| Hover over lesson title                         | Orange text, transparent background | White text and orange background                    | Test Success |
| Click on lesson image                           | Lessons page                        | Page of the lesson                                  | Test Success |
| Click on lesson title                           | Lessons page                        | Page of the lesson                                  | Test Success |
| Hover over 'previous' button                    | Orange text, transparent background | White text, orange background                       | Test Success |
| Hover over 'next' button                        | Orange text, transparent background | White text, orange background                       | Test Success |
| Hover over 'Back to lessons' button             | Black text, transparent background  | White text, black background                        | Test Success |
| Click on 'next' button                          | Page with the lesson                | Page with the next lesson                           | Test Success |
| Click on 'previous' button                      | Page with the lesson                | Page with the previous lesson                       | Test Success |
| Click on 'next' untill the last lesson appears  | Page with the 5th lesson            | 'next' button is grey and inactive                  | Test Success |
| Click on 'back' untill the first lesson appears | Page with the 5th lesson            | 'previous' button is grey and inactive              | Test Success |
| Click on 'Back to lessons' button               | Lesson page                         | Lessons page, playlist is collapsed                 | Test Success |

- admin role

| Action                                                         | Before                              | After                                                                                             | Result       |
|----------------------------------------------------------------|-------------------------------------|---------------------------------------------------------------------------------------------------|--------------|
| Click on 'Lessons in the navigation bar'                       | Any page                            | Lessons page with playlists and management section                                                | Test Success |
| Hover over 'Add Lesson' button                                 | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'Add Playlist' button                               | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'Add Subscription' button                           | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'delete' button in 'All Playlists' section          | Red text                            | Red underlined text                                                                               | Test Success |
| Hover over 'edit' button in 'Subscriptions' section            | Black text                          | Black underlined text                                                                             | Test Success |
| Hover over 'delete' button in 'Subscriptions' section          | Red text                            | Red underlined text                                                                               | Test Success |
| Click on 'Add Playlist' button                                 | Lessons and management page         | Add a playlist page with form                                                                     | Test Success |
| Hover over 'Add Plalist' button                                | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'cancel' button                                     | Black text transparent background   | White text black background                                                                       | Test Success |
| Click on 'Add Plalist' button (empty form)                     | Add Playlist page                   | Same page, notification appears on the blank field                                                | Test Success |
| Click on 'Add Plalist' button (filled form)                    | Add Playlist page                   | Same page, notification appears that playlist is successfully created                             | Test Success |
| Click on 'cancel' button                                       | Add Playlist page                   | Lessons and management page                                                                       | Test Success |
| Click on 'Add Lesson' button                                   | Lessons and management page         | Add a lesson page with form                                                                       | Test Success |
| Hover over 'Add Lesson' button                                 | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'cancel' button                                     | Black text transparent background   | White text black background                                                                       | Test Success |
| Click on 'Add Lesson' button (empty form)                      | Add Lesson page                     | Same page, notification appears on the blank field                                                | Test Success |
| Click on 'Add Lesson' button (filled required fields)          | Add Lesson page                     | Same page, notification appears that lesson is successfully added                                 | Test Success |
| Click on 'cancel' button                                       | Add Lesson page                     | Lessons and management page                                                                       | Test Success |
| Click on 'Add Subscription' button (empty form)                | Add Subcription page                | Same page, notification appears on the blank field                                                | Test Success |
| Click on 'Add Subscription' button (filled required fields)    | Add Subcription page                | Same page, notification appears that subscription is successfully added                           | Test Success |
| Click on 'cancel' button                                       | Add Subcription page                | Lessons and management page                                                                       | Test Success |
| Hover over 'Edit' button on the lesson page                    | Orange text, transparent background | White text, orange background                                                                     | Test Success |
| Hover over 'Delete' button on the lesson page                  | Orange text, transparent background | White text, orange background                                                                     | Test Success |
| Click on 'Edit' button on the lesson page                      | Lesson page                         | Edit lesson page with prefilled form and notification 'You are edditing %Lesson name%'            | Test Success |
| Hover over 'Update Lesson' button on the lesson page           | Orange text, transparent background | White text, orange background                                                                     | Test Success |
| Hover over 'Cancel' button                                     | Black text transparent background   | White text black background                                                                       | Test Success |
| Click on 'Update Lesson' button                                | Edit lesson page                    | Lesson page and notification that lesson has been updated                                         | Test Success |
| Click on 'Cancel' button                                       | Edit lesson page                    | Lessons and management page                                                                       | Test Success |
| Click on 'Delete' button                                       | Lesson page                         | Same page and notification that lesson has been deleted                                           | Test Success |
| Click on 'Delete' on the playlist in All Playlists section     | Lessons and management page         | Same page and notification that playlist has been deleted                                         | Test Success |
| Click on 'Edit' on the subscription in Subscriptions section   | Lessons and management page         | Edit Subscription page with prefilled form and notification 'You are edditing %Subscription name% | Test Success |
| Hover over 'Update Subscription' button                        | Orange text, transparent background | White text and orange background                                                                  | Test Success |
| Hover over 'Cancel' button                                     | Black text transparent background   | White text black background                                                                       | Test Success |
| Click on 'Update Subscription' button                          | Edit Subscription page              | Lessons and management page with notification 'Successfully updated subscription'                 | Test Success |
| Click on 'cancel' button                                       | Edit Subscription page              | Lessons and management page                                                                       | Test Success |
| Click on 'delete' on the subscription in Subscriptions section | Lessons and management page         | Same page and notification that subscription has been deleted                                     | Test Success |

### Products

- user role

| Action                                       | Before                             | After                                                                   | Result       |
|----------------------------------------------|------------------------------------|-------------------------------------------------------------------------|--------------|
| Click on 'All products'                      | Any page                           | Products page containing all products                                   | Test Success |
| Click on 'Guitars' > 'Acoustic Guitars'      | Any page                           | Products page containing acoustic guitars only                          | Test Success |
| Click on 'Guitars' > 'Electric Guitars'      | Any page                           | Products page containing electric guitars only                          | Test Success |
| Click on 'Guitars' > 'Bass Guitars'          | Any page                           | Products page containing bass guitars only                              | Test Success |
| Click on 'Equipment' > 'Amplifiers'          | Any page                           | Products page containing amplifiers only                                | Test Success |
| Click on 'Equipment' > 'Sound pedals'        | Any page                           | Products page containing sound pedals only                              | Test Success |
| Click on 'Other' > 'Accessories'             | Any page                           | Products page containing accessories only                               | Test Success |
| Click on 'Other' > 'Merch' (empty category)  | Any page                           | Products page without any products but text "Sorry...No products found" | Test Success |
| Hover over products cards                    | No border                          | Orange border and brighter image                                        | Test Success |
| Hover over price sorting options             | Light-grey text                    | White text                                                              | Test Success |
| Hover over brands buttons                    | Black background white text        | Orange text and border                                                  | Test Success |
| Click on 'Gibson'                            | Products page                      | Only products of the Gibson brand                                       | Test Success |
| Click on product card                        | Products page                      | Product details page                                                    | Test Success |


### Product details

- user role

| Action                                       | Before                             | After                                                                   | Result       |
|----------------------------------------------|------------------------------------|-------------------------------------------------------------------------|--------------|
| Hover over the image                         | Product details page               | Image becomes brighter                                                  | Test Success |
| Click on the image                           | Product details page               | Image opens in the new tab                                              | Test Success |
| Hover over 'add to cart' button              | Orange text transparent background | White text orange background                                            | Test Success |
| Hover over 'back' button                     | Black text transparent background  | White text black background                                             | Test Success |
| Click on 'add to cart' button                | Product details page               | Same page, and notification, that product has been added to cart        | Test Success |
| Hover over 'go to secure checkout' button    | Orange text transparent background | White text orange background                                            | Test Success |
| Click on 'go to secure checkout' button      | Product details page               | Shopping bag page                                                       | Test Success |
| Click on 'back' button                       | Product details page               | All products page                                                       | Test Success |
| Click on '+' button next to 'Quantity' field | '1' in quantity field              | '2' in quantity field                                                   | Test Success |
| Click on '-' button next to 'Quantity' field | '2' in quantity field              | '1' in quantity field                                                   | Test Success |
| Click on '-' button next to 'Quantity' field | '1' in quantity field              | '1' in quantity field                                                   | Test Success |
| Click on '+' button next to 'Quantity' field | '99' in quantity field             | '99' in quantity field                                                  | Test Success |
| Enter 150 in 'Quantity' field                | '1' in quantity field              | alert appears that the value must be 99 or less                         | Test Success |
| Enter 0 in 'Quantity' field                  | '1' in quantity field              | alert appears that the value must be 1 or more                          | Test Success |


- admin role

| Action                             | Before                              | After                                                                                                 | Result       |
|------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------|--------------|
| Hover over 'Edit'                  | Blue text                           | Underlined blue text                                                                                  | Test Success |
| Hover over 'Delete'                | Red text                            | Underlined red text                                                                                   | Test Success |
| Click on 'Edit'                    | Product details page                | Product management page with prefilled product form and notification 'You are edditing %Product name% | Test Success |
| Hover over 'Update Product' button | Orange text, transparent background | White text, orange background                                                                         | Test Success |
| Hover over 'Cancel' button         | Black text transparent background   | White text black background                                                                           | Test Success |
| Click on 'Update Product' button   | Product management page             | Same page and notification that product has been updated                                              | Test Success |
| Click on 'Cancel' button           | Product management page             | All product page                                                                                      | Test Success |
| Click on 'Delete' button           | Product details page                | All products page and notification that product deleted                                               | Test Success |


### Shopping bag

| Action                                           | Before                               | After                                                             | Result       |
|--------------------------------------------------|--------------------------------------|-------------------------------------------------------------------|--------------|
| Hover over 'Secure Checkout' button              | Orange text transparent background   | White text orange background                                      | Test Success |
| Hover over 'Keep Shopping' button                | Black text transparent background    | White text black background                                       | Test Success |
| Click on 'Secure Checkout' button                | Shopping bag page                    | Checkout page                                                     | Test Success |
| Click on 'Keep Shopping' button                  | Shopping bag page                    | Products page                                                     | Test Success |
| Click on '+' button next to 'Quantity' field     | '1' in quantity field                | '2' in quantity field                                             | Test Success |
| Click on '-' button next to 'Quantity' field     | '2' in quantity field                | '1' in quantity field                                             | Test Success |
| Click on '-' button next to 'Quantity' field     | '1' in quantity field                | '1' in quantity field                                             | Test Success |
| Click on '+' button next to 'Quantity' field     | '99' in quantity field               | '99' in quantity field                                            | Test Success |
| Enter 150 in 'Quantity' field and click 'update' | '1' in quantity field                | alert appears that the value must be 99 or less                   | Test Success |
| Enter 0 in 'Quantity' field and click 'update'   | '1' in quantity field                | alert appears that the value must be 1 or more                    | Test Success |
| Click on 'remove'                                 | Shopping bag page                    | Same page and notification is there that %product name% removed   | Test Success |


### Checkout page

| Action                                                 | Before                             | After                                                                        | Result       |
|--------------------------------------------------------|------------------------------------|------------------------------------------------------------------------------|--------------|
| Hover over 'Complete order' button                     | Orange text transparent background | White text orange background                                                 | Test Success |
| Hover over 'Adjust Bag' button                         | Black text transparent background  | White text black background                                                  | Test Success |
| Click on 'Complete Order' button (empy address fields) | Checkout page                      | Same page, notification appears indicating the first required field          | Test Success |
| Click on 'Complete Order' button (empy card fields)    | Checkout page                      | Loading, same page, notification reports where is the problem in form        | Test Success |
| Click on 'Complete Order' button (all filled)          | Checkout page                      | Loading, order confirmation page and notification of the successful purchase | Test Success |
| Click on 'Adjust Bag' button                           | Checkout page                      | Shopping bag page                                                            | Test Success |


## Deployment
<hr>

### ElephantSQL Database

For the database I have used [ElephantSQL](https://www.elephantsql.com/) cloud service.
It uses PostgreSQL 13.12 version

To set up the database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: lunar_glow).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary media hosting
For images I have used [Cloudinary](https://cloudinary.com/) which provides cloud based sollution

### Heroku Deployment
The web application was deployed on Heroku, service providing cloud based server for the web-application running.
Deployment steps are as follows, after account setup:

- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set your environment variables.

| Key | Value            |
| --- |------------------|
| `DATABASE_URL` | user's own value |
| `CLOUDINARY_URL` | user's own value |
| `EMAIL_HOST_PASS`  | user's own value |
| `EMAIL_HOST_USER`  | user's own value |
|  `SECRET_KEY`   | user's own value |
|  `STRIPE_PUBLIC_KEY`   | user's own value |
|  `STRIPE_SECRET_KEY`   | user's own value |
|  `STRIPE_WH_SECRET`   | user's own value |


Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`


### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("AWS_ACCESS_KEY_ID", "user's own value")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

### Stripe payments

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these steps to connect the payment system.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://music-city-d688a3a37a92.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) for account verification and order confirmation emails.

Once you've created a Gmail (Google) account and logged-in, follow these steps to set up email server.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or lunar_glow
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address


## Improvement
<hr>

Working on the project and facing high pressure of the deadline I had to leave a few things for future
implementation. 

- to show the user the time left on his subscription
- email reminders to renew the subscription
- subscription information in user profile
- more complex form for sending newsletter including text formatting features.
- promo-code functionality (e.g. user with the subscription for lessons can get
a promo-code from the lesson and get a discount on the guitar the teacher plays.)
