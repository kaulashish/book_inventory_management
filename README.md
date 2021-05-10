# Books Inventory System

A Django Web Application where a user can create multiple stores and add books to their respective stores.

*This project is an assignment for [Gloify](https://gloify.com/)*

## Implementation

- The whole project was implemented using Class Based Views which is always my priority choice as it looks a lot cleaner
as well as explain all the intricacies that helps trmendously when trying to understand the concepts even though the code
can be a lot more than Generic Views.

- The Search functionality for the books uses Google Books API, which turned out to be the backbone of this project since 
one would be able to not only provide search results for most of the books out there but also provide every other detail
about the book such as Google book id, isbn, author, etc.

- The Search results have been limited to only 5 results, since I didnt have enough time to implement pagination and also,
the search query would match the first couple results.

- I have also implemented Sentry, in order to show any errors when debug is set to false.

## How To Run 

- Visit the project [website](https://gloifyinventoryproj.herokuapp.com/) where you will be first greeted with the login page.

- Create an account using the 'Signup' hyperlink. This will redirect you directly to the home page.

- Add a new store by clicking on the 'New Store' Button. Choose a name for your store and click 'Submit' or hit enter.

- You will be redirected back to the home page and your store will be listed under 'Your Stores'

- Click on your store. Now to add books, click on 'Search books to add to inventory'.

- Enter your search query for the book and hit enter, this will return 5 search items.

- Click on the book item which will redirect you to the Book details page.

- To add this book, click 'add to inventory' and mention the amount of books you would like to add to your store.

- You will be redirected to your store and under the Book Inventory, you will get a list of all the books you have added.

- In order to edit/delete your book inventory, click on the Edit or Delete button respectively.

- To log out of your account, go to the homepage and click 'logout' under the Welcome text.
