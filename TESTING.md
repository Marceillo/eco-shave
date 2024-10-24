

# Table of Contents

- [Testing](#testing)
- [Testing User Stories](#testing-user-stories)
- [Responsive Layout and Design](#responsive-layout-and-design)
- [Python Validation - PEP8](#python-validation-pep8)
  - 
  - 
  - 
- [Lighthouse](#lighthouse)
  - 
  - 
  - 
- [HTML Validation](#html-validation)
  - 
  -  
- [CSS Validation](#css-validation)
  - 
- [Manual Testing](#manual-testing)
- [Frontend](#frontend)
- [Backend Admin Panel](#backend-admin-panel)
- [Fixed Bugs](#fixed-bugs)
- [Unfixed Bugs](#unfixed-bugs)

# Testing

## Testing User Stories

<details>

<summary>User stories testing</summary>

## User Stories Test Table

## User Stories Test Table

| EPIC                                 | ID   | User Story                                                                 | Check | Test Result                                                                                      |
| :----------------------------------- | ---- | :------------------------------------------------------------------------- | :---: | :----------------------------------------------------------------------------------------------- |
| **E-commerce Integration**           |      |                                                                           |       |                                                                                                 |
|                                     | 1.1  | As a user, I want to add products to a shopping cart and proceed to check out, so I can easily make purchases on the site. | [ ]   | Products can be added, viewed, removed, and adjusted in quantity.                             |
|                                     | 1.2  | As a user, I want to receive confirmation of my purchase via email and on-screen notifications, so I can verify my order. | [ ]   | Users receive an email confirmation after a successful purchase.                               |
|                                     | 1.3  | As a user, I want a streamlined checkout process, so I can complete my purchases efficiently.  | [ ]   | Users can review their orders and enter payment details easily.                                 |
| **User Experience Design**          |      |                                                                           |       |                                                                                                 |
|                                     | 2.1  | As a user, I want an accessible and intuitive website, so I can navigate and interact with the content seamlessly. | [ ]   | The front-end meets WCAG accessibility guidelines.                                             |
|                                     | 2.2  | As a user, I want a mobile-responsive design, so I can access the website on different devices. | [ ]   | The website layout adapts to various screen sizes (desktop, tablet, mobile).                   |
|                                     | 2.3  | As a user, I want to edit and view my profile information, so I can keep my account details up-to-date. | [ ]   | Users can access and modify their profile information easily.                                   |
|                                     | 2.4  | As a user, I want to create and manage a wishlist within my profile modal, so I can save products for future consideration. | [ ]   | Users can add products to their wishlist from product pages; the wishlist is accessible from the user profile modal. |
| **Search Engine Optimization**       |      |                                                                           |       |                                                                                                 |
|                                     | 3.1  | As a user, I want to find products quickly using search functionality, so I can locate items efficiently.  | [ ]   | Each page includes Meta Description tags and a sitemap; a search bar is available for accurate results. |
|                                     | 3.2  | As a user, I want a helpful 404 error page with navigation options, so I can find my way back to the main site if needed.  | [ ]   | A 404 error page includes links to the homepage and contact page.                              |
| **Authentication and Authorization**|      |                                                                           |       |                                                                                                 |
|                                     | 4.1  | As a user, I want to register and log in securely to access my account information.           | [ ]   | A secure authentication system is implemented for registration and login.                      |
|                                     | 4.2  | As an admin, I want to manage user roles effectively, so I can control access levels based on user roles.           | [ ]   | Role-based access control is implemented with restricted access for non-admin users.          |
|                                     | 4.3  | As a user, I want to see my login status clearly on every page.                               | [ ]   | A visual indicator of the current login state is displayed prominently.                        |
| **Marketing and Brand Reach**       |      |                                                                           |       |                                                                                                 |
|                                     | 5.1  | As a user, I want to subscribe to newsletters for updates and promotions.                     | [ ]   | A newsletter signup form is available with automated welcome emails upon subscription.        |
|                                     | 5.2  | As a user, I want to share products on social media easily to recommend them to friends.     | [ ]   | Social media sharing buttons are available on product pages.                                   |
| **E-commerce Fundamentals**          ||                                                                         ||                                                                                               |
|                                     ||6.1 As a business owner, I want to document the e-commerce model clearly for outlining the application’s purpose and user value.| [ ]   ||A detailed marketing plan is included in the README file explaining the e-commerce model and target audience.| 
| **Customer Support and Information Access**|      ||                                                                     ||                                                                                               |
|                                     ||7.1 As a user, I want to submit a contact form so that I can easily reach out for support or inquiries.|[ ]    ||A contact form is available on the About Page; it includes fields for name, email, subject, and message; form validation ensures that all required fields are completed before submission; users receive a confirmation message upon successful submission.| 
|                                     ||7.2 As a user, I want to view frequently asked questions in a modal so that I can find quick answers without leaving the About Page.|[ ]    ||A button or link to open the FAQ modal is prominently displayed on the About Page; the modal contains common questions with expandable answers; users can close the modal easily.| 
|                                     ||7.3 As a user, I want links to additional support resources within the FAQ modal so that I can find more detailed information if needed.|[ ]    ||Each FAQ entry includes links to relevant articles or resources for further assistance; users can navigate directly from within the modal.| 
</details>

# Responsive Layout and Design

The project design was adapted to different devices and Bootstrap helped with most of this. My focus was really to have a working Django APP and as I have said before time was an issue for me to really do a design with all the bells and whistles this will be my future focus for this project.

* Testing was ongoing during this project from one feature to the next even so I left some of the final testing for last.
 


## Python Validation - PEP8

* I had a lot of errors found but none that could not be fixed, use this tool [pep8ci](https://pep8ci.herokuapp.com/)
* Cleared all until I received the below result. 

<br>

![Pyhton](/static/readme/test-image/blogviewpepnoerror.png)

<br>

<details>
<summary>Blog PeP8 errors/warnings fixed</summary>

</details>                                      

<details>

<summary>About PeP8 errors</summary>

                   |
|            |                                |            |                                    |

</details>

<details>
<summary>Main App PeP8 errors</summary>

## Main View



## Main Urls


## Main Settings


</details>

<details>
<summary>ENV file PEP8 errors</summary>

#### ENV File


</details> 


## Lighthouse

* Most of my light house score was in this range as seen below. 

![Lighthouse](/static/readme/images/homelight.png)

<details>
<summary>Lighthouse image of pages</summary>

* I added some of them but not all as the results where all similar.

#### Home

* [Lighthouse Home](/static/readme/images/homelight.png)
* [Lighthouse Home mobile](/static/readme/images/homelightmobile.png)

#### About 

* [Lighthouse About](/static/readme/images/aboutlight.png)
* [Lighthouse About](/static/readme/images/aboutlightmobile.png)

#### Profile

* [Lighthouse Profile](/static/readme/images/profilelight.png)
* [Lighthouse Profile Mobile](/static/readme/images/profilelightmobile.png)

#### Profile Edit 

* [Profile Edit ](/static/readme/images/profileeditlight.png)
* [Profile Edit mobile ](/static/readme/images/profilelighteditmobile.png)



</details>

[Back to Table of Contents](#table-of-contents)

## HTML Validation

* I used the [W3C Validator](https://validator.w3.org/)
* They managed to clear the errors I found from the validator on all the links.

![HTML](/static/readme/test-image/html-test/validator-w3-success.png)

<details>
<summary>links validated success </summary>

* [Profile](/static/readme/test-image/html-test/userprofilesuccess.png)
* [Profile Edit](/static/readme/test-image/html-test/profile_edit.png)
* [Delete Profile](/static/readme/test-image/html-test/deleteprofile.png)
* [Password Change](/static/readme/test-image/html-test/profilepasswordchange.png)
* [Password Reset](/static/readme/test-image/html-test/password-reset.png)
* [Home Page](/static/readme/test-image/html-test/homepage.png)
* [HTML About Page](/static/readme/test-image/html-test/aboutpagesuccess.png)

</details>


## CSS Validation

* MY custom CSS was validated using [W3C Jigsaw validation](https://jigsaw.w3.org/css-validator/)service. 

<details>
<summary>CSS success image</summary>

![CSS](/static/readme/test-image/success-css.png)

</details>
[Back to Table of Contents](#table-of-contents)

## Java Script 

* I used [jsHint](https://jshint.com/) for testing the JS in my static file 
* Removed all the warnings and errors.
* Undefinded variables and unused variables remained.
* I tried to remove these as well but ended up crashing my app features and decided to leave them as they are no risk. 

![JS](/static/readme/test-image/jshint.png)

<details>
<summary>jsHInt error summary </summary>

#### JS Errors

| Line | Error Message                                                           | Line | Error Message                                                           |
|------|-------------------------------------------------------------------------|------|-------------------------------------------------------------------------|
| 1    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 2    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
|
| Type | Variable |
|------|----------|
| Undefined | 7 bootstrap |

</details>

## Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.
<details>
<summary>Manual Testing results </summary>

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads the log in page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the About button on the nav bar loads the About page.
| &check; | Clicking While in the About page clicking on the contac us link loads the contact page.
| &check; | Clicking the Register link loads the Register page
| &check; | Clicking the Log In link loads the Log In page 
| &check; | Clicking In the Log In link clicking on the forget password link loads password reset.  
| &check; | Clicking on the Post title loads the review detail page
| &check; | In Post details view the user has no access to update post.
| &check; | In the details view the user cannot create a comment or delet.
| &check; | Clicking the Facebook link in the footer area opens Facebook link. 
| &check; | Clicking the X link in the footer area opens X link . 
| &check; | Clicking the You Tube in the footer area opens You Tube link.
| &check; | Clicking the search field and serching for Author,Body,Excerpt,Title works. 

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | User cannot access Admin Panel without being staff member
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the About button on the nav bar loads the About page.
| &check; | Clicking While in the About page clicking on the contac us link loads the contact page.
| &check; | Clicking in the Profile page loads the Profile page.
| &check; | While in the Profile page clicking on the button Password change loads the page to change password.
| &check; | While in the Profile page clicking on the button Profile Edit loads the page to edit profile.
| &check; | While in the Profile Edit page clicking on the button delete Profile Picture deletes profile picture.
| &check; | While in the Profile page clicking on the button Profile Delete loads confirm page and then when confirmed deletes profile.
| &check; | After it  deletes profile a success message is displayed or error message if not.
| &check; | In the detail post view or the home page will show buttons if user is the author of post.
| &check; | In the detail post view the logged in user can comment underneath a post.
| &check; | When user submits a comment a confirmation message is being shown on the page
| &check; | In the detail view the logged in user can update/delete the comments written by themselves.
| &check; | Clicking the update button the comment text will show in the comment box.
| &check; | Clicking the delete button loads the delete comment confirm message page.
| &check; | In the detail view the logged in user can Favorite/unfavorite posts.
| &check; | In the detail view the logged in user has full CRUD for the post written by themselves.
| &check; | Clicking the edit button in My Blog nav link view loads the edit btn and page.
| &check; | Clicking the delete button in the detail view loads the delete post confirmation page
| &check; | Clicking the My Blog nav link in the logged in user nav bar shows the logged in users posts
| &check; | While in the My Blog link the logged in user can see there drafts and published posts.
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the X link in the footer area opens X link . 
| &check; | Clicking the You Tube in the footer area opens You Tube link.
| &check; | Clicking the search field and serching for Author,Body,Excerpt,Title works. 

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | The Admin Panel is access b typing /admin
| &check; | Deleting a Profile works on the Admin Panel
| &check; | Deleting a Post works on the Admin Panel
| &check; | Deleting a Comment works on the Admin Panel
| &check; | Changing an email of any user works in the admin bar
| &check; | Changing a password of any user works in the admin bar
| &check; | Deleting a Profile will delete their posts, comments and email and logout the user before delet.

 Status | **Create A Post - User Logged In**
|:-------:|:--------|
| &check; | Title field is required
| &check; | Title field does not accept empty field
| &check; | Title field does not accept just spaces
| &check; | Featured Image is not required
| &check; | Body field is required
| &check; | Body field does not accept empty field
| &check; | Body field has to have 100 characters.
| &check; | Excerpt is not required
| &check; | Excerpt auto summorises the text.
| &check; | Status field defaults to Draft
| &check; | Posting as shows name of author
| &check; | If no image is selected a default is provided.
| &check; | **Home** page with a success message is displayed when the user submits the post

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field is required does not accept empty field
| &check; | Success message is displayed when the user creates a new user
| &check; | Error message with corresponding info when wrong input is submitted


Status | **Profile Page - User Logged In**
|:-------:|:--------|
| &check; | The default profile info is seen on the profile page (Field not provided).
| &check; | The profile success message or error is displayed when the user submits the profile form.
| &check; | A new user has CRUD on there profile and posts, like and crud on comment after registering.

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Multi Device Mockup Generator](https://techsini.com/multi-mockup/).

| Desktop    | Display <1200px       | Display >1200px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | iPad Air              | Asus Zenbook Fold  | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S8+/S20 Ultra  | iPhone XR/12Pro/14 Pro Max | Pixel 7 / 7 Pro      |
|------------|-----------------------|----------------------------|----------------------|
| Render     | pass                  | pass                       | pass      | pass     |
| Images     | pass                  | pass                       | pass      | pass     |
| Links      | pass                  | pass                       | pass      | pass     |

### Browser Compatibility
* Google Chrome Version 
* Mozilla Firefox 
* Microsoft Edge 
</details>
 
[Back to Table of Contents](#table-of-contents)

- All manual testing was done with DEBUG = False in the settings.py file.


* **All known bugs have been fixed**

## Fixed bugs

* I had quite a few bugs during this project some of them I have manged to document.
* There are probibly more bugs I fixed but can not remmeber as during troubleshooting I often forgot to document the process.

| **Bug**                                                                 | **Fix**                                                                                                          |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Bug1: Heroku log = Mis-cased Procfile detected; ignoring. to Heroku    | Rename it to `Procfile` to have it honored as it is case sensitive.                                            |

[Back to Table of Contents](#table-of-contents)

## Unfixed Bugs 

* I do not know of any other unfixed bugs .

| Bug                     | Status      | Why                                                                 |
|------------------------|-------------|---------------------------------------------------------------------|
| CSRF verification failed | Unfixed     | This is a known problem that happens intermitendly on login ; all resources, including tutor support, acknowledge that this is a known Django issue. |
