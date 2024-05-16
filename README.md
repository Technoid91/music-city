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
![image of products page](https://i.ibb.co/x8HwGkK/2024-05-16-09-25-44.png)
The products page shows the user 



- ### Other features
- Playlists 





A section of the web site 
## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
