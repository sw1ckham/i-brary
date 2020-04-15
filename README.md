<div style="align: center;">

# I-Brary

<p>I-brary is a fully responsive, user based, book recommendation site.
You can browse the Homepage for book recommendations and reviews. You can log in and add your own book reviews, you have the option
to 'share', once shared your book will show up on the homepage. If you don't share, 
your book review will only been seen in your own view.</p>

</div>

## UX

### Project Goals

To create a site that allows users to store books they have enjoyed/want to read. To allow the user to add a genre, review and rating
so if they decide to share their book, other users can get inspiration from the books they have added. 

### User Goals

I want to have a place online I can store my favourite books and also get information on other books I have not read. 

### User Stories

As a user I want...

* To be able to register quickly without the site taking any unneccesary information.
* To be able to find new books I haven't read before.
* To be able to see the Genre and rating of new books so there is enough information for me to decide whether I would enjoy it. 
* To be able to navigate around the site with ease.
* To be able to edit or delete my added books with ease.
* To know that I am the only person able to edit my books that I have added.
* To know my books will be saved when I log out, so when I revisit the site, my books are still there.


### Design Choices

I have decided to go for a simple, professional design. The demographic of my users are readers that use the internet as a resource to source new books.
This would be a large range of ages and backgrounds. Due to this I have stuck to a very classic look I think is already paired with English Literature.

+ Font
... The font I chose was 'Playfair Display' due to it's 'old timey' design lending itself to the 18th century. 

+ Colour
... I chose Blue as my main colour because it is known as a very calm colour, reading is a peaceful activitie and so should looking into books online. 
... Also there are a lot of colours and patterns on the covers of the books. I want the books to stand out and be the main feature on the page, therefore
... light blue background worked very well as it brings any elements to the foreground. 
... I chose a dark blue colour for the nav bar and the buttons. These are all points of contact for the user and I wanted them to stand out without
... contrasting with the rest of the sit. 

+ Styling
... I used the Materialize framework which kept the site clean and simple.
... I decided not to curve off any edges on photos/cards, I want the site to have the resemblence of book corners throughout and the book images, 
to stay looking like books. 

## Wireframes 

All Wireframes were made using [Mock Plus](https://www.mockplus.com/)

* [Home Page Desktop](https://ibb.co/5K21mqw)    
* [My Books Desktop](https://ibb.co/DpCfWn6)
* [Log in Desktop](https://ibb.co/3f9GVdH)
* [Register Desktop](https://ibb.co/NjnygmY)
* [Add Book Desktop](https://ibb.co/0fcKBF6)

* [Home Page Mobile](https://ibb.co/bXJKL6p)    
* [My Books Mobile](https://ibb.co/dpNb3Lj)
* [Log in Mobile](https://ibb.co/X2LrHJL)
* [Register Mobile](https://ibb.co/mFjGqbM)
* [Add Book Mobile](https://ibb.co/xj2PQJG)


## Features

+ Nav Bar

+ Log In / Register options.

+ My books view.

+ Ability to add a book to your own view.

+ Ability to share that book for others to see on the homepage. 

+ Ability to edit or delete any book you have previously added. 

+ Footer with Log/Register options, social links on the developer.

## Features left to Implement

+ Search by Genre filter.

+ Able to save other books from the homepage into your own 'My Books' view.

+ Ability to buy/download the books on the homepage.


## Technologies used

* HTML5
* CSS3
* Python

* [MongoDB](https://www.mongodb.com/)

* [Materialize](https://materializecss.com/)
* Jquery
* Flask
* PyMongo
* Brycpyt

* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)

* [GitPod](https://gitpod.io/workspaces/)
* [GitHub](https://github.com/sw1ckham)

* Git

## Testing

I began my testing using.. 

- [HTML WC3 Markup Validation Service.](https://validator.w3.org/)
- [CSS WC3 Markup Validation Service](https://jigsaw.w3.org/css-validator/)

#### Mid-point CSS Validation bugs:

- line 227 - min-wdith is an unknown vendor extension (Corrected typo)
- line 213 - Same color for background-color and color (I kept this the same otherwise the line is not a block colour.)

#### Mid-point HTML Validation bugs:

- Throughout all my html pages I had forgotton to add an alt tag to my images (Corrected)

### Bugs during developement

1. The columns the cards from Materialize were in, were not centering inside their row.
* [Solution](https://stackoverflow.com/questions/50671682/center-align-items-in-materializecss-row): Add a flexbox class to the column you need to center. Add custom styles to center. 

2. Edit book function, when you edit a book, they book would disappear. 
* Solution - I needed to add a 'username' field in the form, and in tell the function to pull the 'added by' username from the form and fill
that field in the database. Once I made those changes, the new edited version had the same username in the 'added_by' field as before and therefore
showed up correctly on the 'My Books' page with the correct changes made. 

3. Following from the bug above, I now need to make sure all fields are required, otherwise the book may not show in 'My Books', and the display will not look good. 
I added 'required' to the end of each input but this did not work. 
* [Solution](https://stackoverflow.com/questions/17966390/html5-required-attribute-seems-not-working) - I found a stack overflow post voicing the same bug, 
the solution was to close the input tags properly /> 

4. The height of my cards. The height of the card was changing dependant on how much text you wrote in the 'comments' sections. This was a problem
as design wise, it did not look good all the cards different heights. Also the cards overspill into other containers.
* Solution - Set a max charactor limit on each comments input. I found out what height the card was when all the charactors were used and set all cards
to be that height. 

#### Client Stories Testing

* To be able to register quickly without the site taking any unneccesary information.
- When signing up to the site I am currently only asking for a 'Username' and 'Password' to set up. As there is no purchasing from the site, I currently do not need anymore
of their personal information. 
* To be able to find new books I haven't read before.
- On the homepage is a library of all the books users have uploaded and decided to share. 
* To be able to see the Genre and rating of new books so there is enough information for me to decide whether I would enjoy it. 
- Each book is displayed on a card, on this card are tabs displaying more information about the books. These fields have been set as 'required', so there will always be
Genre and Rating information on each book on the site. 
* To be able to navigate around the site with ease.
- The site's navigation bar is fixed therefore it is very obvious how to navigate from page to page. Also there are options to 'Log In' and 'Register' in the footer.
* To be able to edit or delete my added books with ease.
- In the 'My Books' view, each book has an 'Edit' or 'Delete' button, when you choose to edit a book, it is required to input your username, this way the book will stay in 
your 'My Books' view, and replace the old version of the book. 
* To know that I am the only person able to edit my books that I have added.
- The Edit and Delete buttons only show up in the 'My Books' view, and you can only see 'My Books' when you are logged in. The books shows in the 'My Books' view, are only
the books you have uploaded whilst being logged in. 
* To know my books will be saved when I log out, so when I revisit the site, my books are still there.

#### Manual Testing



#### Bugs Disovered during testing



## Deployment

#### I developed this project using the GitPod, committing to Git and pushing to GitHub via the locally installed Git commands. 

#### The following steps are how to create an app in heroku and connect it to 

- Login to heroku and go into your personal apps.
- Click **New** in the top right corner and create a new app, pick your closest region.
- In your CLI associate the heroku application as our remote master branch - heroku git:remote - a [app name]

#### The following steps run through how I deployed this project to [Heroku.](https://dashboard.heroku.com/) 

- Add a requirements file (list of applications heroku requires to run the app) - **pip3 freeze --local > requirements.txt**
- Git add and commit requirements file
- Add a Procfile (we need to tell heroku which file is used as our entry point to the app) - **echo web: python app.py > Procfile**
- Git add and commit requirements file
- Push to Github and Heroku - **git push origin master && git push heroku master**
- Tell Heroku to get the app up and running - **heroku ps:scale web=1**
- Go to settings in Heroku - Reveal config vars - Put in IP and PORT values (remember if the values are IP: 0.0.0.0, PORT: 5000)
- Open app. 

#### Running this project locally... 

1. Log into your GitHub
2. Find the repository via this link [I-brary](https://github.com/sw1ckham/i-brary)
3. Click on **clone or download**, copy the clone URL under **clone with HTTPS**.
4. Open up your IDE, and open **git bash**
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type **git clone**, and then paste the URL you copied. example: **$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY**
7. Press Enter. Your local clone will be created.

## Credits

### Content

All content written in this project was written by the developer.

### Media

- I sourced all photos for the books from online mainly google images and copied the image url. 

- All icons came from [Materialize's library](https://materializecss.com/icons.html) 

### Code 
* Retrieved the [code](https://materializecss.com/cards.html) for my books cards from materialze and Edited.  
* This [Stack Overflow post](https://stackoverflow.com/questions/50671682/center-align-items-in-materializecss-row) helped me center the cards on index.html.*
* I used [CSS matic](https://www.cssmatic.com/box-shadow) to create my box shadows
* I used [W3 Schools](https://www.w3schools.com/tags/att_textarea_maxlength.asp) to help me work out how to apply a max-length to a text area.

### Acknowledgements

Thank you very much to my mentor Spencer who helped me throughout. Also to the student care tutors and 'Igor' on Slack who was always quick to lend a hand. 

