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


| Result for page                                                                                                           | Errors                                                         |
|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2F)                           | No errors                                                      |
| [Subscriptions](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Flessons%2Fsubscription%2F) | No errors                                                      |
| [Products](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Fproducts%2F)         | No errors |
| [Sign Up](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Fsignup%2F)         | No errors                                                      |
| [Log In](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmusic-city-d688a3a37a92.herokuapp.com%2Faccounts%2Flogin%2F)     | No errors                                                      |

- ### CSS
For CSS validation I have used [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

No errors found

- ### Python
All python files passed CI Python Linter with no issues.

<hr>

## Manual Testing

<hr>

### Home page


- user role

| Action                                                      | Before                                | After                                              | Result  |
|-------------------------------------------------------------|---------------------------------------|----------------------------------------------------|---------|
| Click on logo                                               | Any page of website                   | Homepage renders                                   | Test Success |
| Click on 'Home' at the navbar                               | Any page of website                   | Homepage renders                                   | Test Success |
| Hover over the news headings at the left part of the page   | Grey background                       | Brown background                                   | Test Success |
| Click the news heading at the left part of the page         | News banners change change each other | The banner with the same heading and image appears | Test Success |
| Click on 'My bookings' at the navbar (unregistered)         | Any page of website                   | Sign Up page renders                               | Test Success |





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
