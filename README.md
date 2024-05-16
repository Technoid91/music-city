<h1> Music City </h1>
<hr>

Music City - is a web platform for guitar players. 
It contains lessons of how to play the guitar, available 
on subscription, and products for guitar players of all levels.

<hr>
<h2>Features</h2>


- ### Responsive design
![responsive design image](https://i.ibb.co/H2LGvmb/resp.png)

The website is designed to work properly on screens of all popular sizes



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

<h2> Testing </h2>

The website has been tested manually during the development process and using the PyCharm builtin 
functions. 

<hr>

<h2> Deployment </h2>
The website was deployed to Heroku, using the ElephantSQL cloud database and Cloudinary for images hosting

<hr>

<h2> Improvements </h2>
Working on the project and facing high pressure of the deadline I had to leave a few things for future
implementation. 

- to show the user the time left on his subscription
- email reminders to renew the subscription
- subscription information in user profile
