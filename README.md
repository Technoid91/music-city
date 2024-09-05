# Music City
<hr>

Music City - is a web platform for guitar players. 
It contains lessons of how to play the guitar, available 
on subscription, and products for guitar players of all levels.


## UX
<hr>

### Colour scheme

- `#000` used for primary text
- `#e67300` used for higlights
- `#fff` used for secondary text
- `#444`, `#555`, `#888`,`#999`, `#ddd` were used for background colours


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
To allow a user to 'try it before buy it' the options with free 7 days subscription is
included. The user can use it only once. If the database with subscribed users contains
a record, the option of free subscription will not be shown. To purchase subscription,
the user will only need his credit card as this is an online service, no delivery info
required. 

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


- ### Site admin features
![image of the ux admin feature](https://i.ibb.co/QdbRysf/2024-05-16-10-16-01.png)
The admin of the site do not have to use django administration panel to manage the store, subscriptions
and lessons. It can be done on the related pages of the web site.

<hr>

## Testing
<hr>

### Code validation
<hr>

- ### HTML
For HTML validation I have used [W3C Validator](https://validator.w3.org/)


| Result for page                     | Errors    |
|-------------------------------------|-----------|
| [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2F)     | No errors |
| [Subscriptions](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Flessons%2Fsubscription%2F) | No errors |
| [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Fproducts%2F) | No errors |
| [Sign Up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Fsignup%2F) | No errors |
| [Log In](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Flogin%2F) | No errors |

- ### CSS
For CSS validation I have used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

No errors found

- ### Python
All python files passed CI Python Linter. All issues fixed:
- line too long
- no blank line in the end of the file
- 2 blank lines expected found 1


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

Connect the git repository to Heroku and deploy from branch.

## Improvement
<hr>

Working on the project and facing high pressure of the deadline I had to leave a few things for future
implementation. 

- to show the user the time left on his subscription
- email reminders to renew the subscription
- subscription information in user profile
