# Grove Tennis Club

[View live project here!](https://grove-tennis-club.onrender.com)

**Grove Tennis Club** is a thriving tennis club in Sheffield, with four all-weather courts, three of them floodlit until 10pm. We have a brick built Clubhouse that includes a licensed bar. Located in the South West of the Sheffield, we have been here since 1900 with members young and old from all over the county.

We're a neighbourhood friendly tennis club, ideal for families, juniors and adults who are looking for social or competitive tennis opportunities, we welcome all comers!   .

<br>  

![Screenshots of site pages on different devices:](/docs/mockups)

---

## CONTENTS  
  
* [UXD (User Experience Design)](#user-experience-ux)
- [User Stories](#user-stories)
- [Further UX Considerations](#further-ux-considerations) 
  
* [Creation process (Strategy -> Surface)](#creation-process)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structural](#structural)
- [Skeleton](#skeleton)
- [Surface](#surface)
- [Design](#design)
- [Implementation](#implementation)
 
* [Tablet & Mobile View](#tablet--mobile-view)
 
* [Future Features](#future-features)
* [Technologies Used](#technologies-used)
  
* [Deployment](#deployment)
  
* [Testing](#testing)
  -[Availabilities](#availability)

* [Learning Points](#learning-points)
  - [Use of AI](#use-of-ai)
  - [What Went Well](#www)
  - [Even Better If](#ebi)
 
* [Validations & Audit](#html-and-css-validation-using-w3c-validation)

* [Credits](#credits)

---

## User Experience (UX)  
  
### **User Stories & Acceptance Criteria**  
User Stories

Must Have

    As a user, I must be able to log in to the system so that I can access court booking features.
    Acceptance Criteria:
        The user can log in using valid credentials (email and password).
        Invalid credentials show an appropriate error message (e.g., "Invalid username or password").
        Upon successful login, the user is redirected to the dashboard or booking page.

    As a user, I must be able to view the real-time availability of the four courts so that I can decide when to book.
    Acceptance Criteria:
        The booking page displays a grid or table showing court numbers, times, and availability status.
        Availability status updates dynamically without requiring a page reload.
        Courts are marked as "Available" or "Booked."

    As a user, I must be able to book an available court slot so that I can play tennis at my preferred time.
    Acceptance Criteria:
        The user can select an available time slot and court number.
        Clicking "Book" saves the booking in the database.
        Booked slots are no longer marked as "Available."
        The user receives a confirmation message (e.g., "Your court is booked for [date/time] on Court [number].").

    As a user, I must be able to cancel an existing booking so that I can free up the slot if I am unable to attend.
    Acceptance Criteria:
        The user can view a list of their upcoming bookings.
        Clicking "Cancel" removes the booking from the database.
        The canceled slot becomes available for others to book.
        The user receives a confirmation message (e.g., "Your booking for [date/time] on Court [number] has been canceled.").

    As a user, I must be able to rearrange my booking to a different available slot so that I can reschedule my court time if needed.
    Acceptance Criteria:
        The user can view their current bookings and available slots.
        The user can select a new slot and confirm the change.
        The system updates the database with the new slot and frees up the old one.
        The user receives a confirmation message (e.g., "Your booking has been rescheduled to [new date/time] on Court [number].").

    As a user, I must see clear error messages if my actions cannot be completed so that I understand what went wrong.
    Acceptance Criteria:
        Errors like "Slot unavailable," "Invalid login details," or "Session expired" are displayed appropriately.
        Error messages are user-friendly and provide guidance for resolving the issue.

Should Have

    As a user, I should be able to sign up for an account so that I can create my credentials and log in.
    Acceptance Criteria:
        The user can create an account by providing an email, password, and optional profile details.
        The system validates input (e.g., email format, password strength).
        A confirmation email is sent after successful signup.

    As a user, I should be able to log out of my account so that I can ensure the security of my booking data.
    Acceptance Criteria:
        Clicking "Log Out" ends the user’s session.
        The user is redirected to the login page.
        Any session-related data is cleared.

    As a user, I should be redirected to the login page if I try to access booking features without logging in so that unauthorized access is prevented.
    Acceptance Criteria:
        Attempting to access restricted pages without logging in redirects the user to the login page.
        A message (e.g., "Please log in to access this page.") is displayed.

    As a user, I should receive a confirmation message after booking, canceling, or rearranging a slot so that I know my action was successful.
    Acceptance Criteria:
        After completing an action, a success message appears on the page.
        The message includes details of the action (e.g., "Booking confirmed for [date/time].").

Could Have

    As a user, I could be able to view a list of my past bookings so that I can keep track of my court usage.
    Acceptance Criteria:
        A "Booking History" section displays all past bookings.
        Each entry shows the date, time, and court number.

    As a user, I could receive an email notification after making a booking or cancelation so that I have a record of the action.
    Acceptance Criteria:
        Upon booking or canceling, the user receives an email with details of the action.
        Emails are sent to the address linked to the user's account.

    As a user, I could use filters to search for available slots by time or court number so that I can find the most convenient option.
    Acceptance Criteria:
        Filters for date, time, and court number are available on the booking page.
        The displayed slots update based on the selected filters.

    As a user, I could be able to update my profile information so that my contact details remain current.
    Acceptance Criteria:
        A "Profile" page allows users to update their email, phone number, or password.
        Changes are saved successfully and reflected in the database.

Won't Have

    As a user, I won’t be able to invite other users to join my booking in this version of the system.
    Acceptance Criteria:
        No functionality exists for adding multiple users to a booking.

    As a user, I won’t be able to make payments directly through the system, as booking will remain free for this version.
    Acceptance Criteria:
        Booking confirmation does not include payment details.

    As a user, I won’t be able to book courts for recurring slots in this iteration.
    Acceptance Criteria:
        Each booking must be made individually without recurrence options.



### **Further UX Considerations**

#### **1. Navigation Simplicity**
- I intend to make the website with easy and intuitive navigation in mind, with a clear call to action for getting to the booking page
- The layout has been chosen to help users locate content efficiently.

#### **2. Responsive design**
-The site will be optimised and tested for different screen sizes and browsers, starting from mobile (320px) first. This is to ensure readability and functionality across mobile, tablet and desktops.

#### **3. Accessibility**

- Accessibility features such as image alt text and ARIA labels will be incorporated throughout the site.
-High contrast colour schemes and font sizing/family choices will enhance readability for visually impaired users.

#### **4. Content Clarity and Structure**

- The language used on this site will be clear and concise, with buttons and user feedback coloured appropriately to enhance user feedback


#### **5. Feedback Mechanisms**

- Interactive elements, such as modals and call to action buttons allow users to interact and encourages communication.

#### **6. Consistency in Design**

- A consistent use of fonts, colours and visual hierarchy across all pages will help the user become familiar with the layout, reducing cognitive overload.
- This consistency aims to improve the UX by making navigation feel intuitive and predictable. 


---

These considerations contribute to a user-friendly experience, reducing cognitive load and removing barriers to accessing the booking system while maintaining security and confidentiality of personal details.
   

--- 


## **Creation process (Strategy -> Surface)**

### **1. Strategy**  


- I required an easy-to-read, dependable website that provides the fundamental service of booking a tennis court.  
- The website will be designed for mobile first (320px) and adjusted for key breakpoints for tablets, desktops and larger screens.
- Target users for the site will be anyone interested in tennis, particularly novices or casual players as it is a small, local club
  

### **2. Scope**  

The Safeguarding information site must be available on a wide range of devices. 

- The site is to contain only relevant information, presented in a consistent fashion and layout.   
- Text must be clear, legible and high in contrast on any sized device to allow the user instant access to the menu, form and all information.  
- A brief introduction to the background of the club to be included in the landing page.
- Content will be a blurb about the club, a booking system and content form.
  

### **3. Structural**  

It was requested that the design was straightforward, clear and easy to understand with the following features:
 
- A hero section that quickly and clearly describe the purpose of the website.
- Call to action button on landing page to take you to the booking system
- Contact information included in the footer of the page

There will be a navigation structure with clear labels always visible, and a footer with contact information and social links on every page.

  
### **4. Skeleton**  

The site was designed to be straightforward with details about safeguarding and reporting clearly signposted.  
 
- A two-item navigation bar of 'Home', 'Book' and 'Contact', will at the top of the screen. An enlarge feature identifying the current page and colour change whether a cursor or touch was accurate.  On smaller screens the menu collapses into an accordion.
- A large, clear image dominates the landing page. 
- Centred in the image is a blurb explaining the purpose of the website.


### Wireframes  

[Wireframes are available here](/docs/wireframes)

### **5. Surface**  
 
- Two clean, sans-serif fonts, were used 'Lora' and 'Roboto'. Both of these are clear and nicely spaced making them readable for everyone.
- Two separate sites will be created for light and dark modes for the users preference, accessible from the navbar.


### **Design**
- Colour scheme for the site (initial palettes generated by chatGPT, specific colour tones amended to fit my preference). The text colour was chosen to provide sufficient context:

#### **Colour Palette**

| Purpose              | Colour       | Hex       | Usage                                           |
|----------------------|-------------|-----------|-------------------------------------------------|
| **Primary Background**          | Mint Green        | `#E6F7F1` | A calming, nature-inspired green for the main background, evoking the lush environment of the tennis club.                 |
| **Secondary Background**       | Soft Sky Blue   | `#B2C2E0` | A secondary color for sections or highlights, reflecting the tennis court's open-air setting.                       |
| **Primary Accent**     | Teal Green   | `#3A6F74` | A rich green-blue for key elements like headers, buttons, and active states.                              |
| **Secondary Accent** | Deep Sky Blue       | `#5C88C8` | A vibrant, complementary blue for secondary buttons or links. |
| **Light Text**    | White | `#FFFFFF` | Text colour for darker accents or buttons          |
| **Dark Text**    | Charcoal Black  | `#2D2D2D` | For main body text, headers, and any text on light backgrounds.         |

These colours were chosen to meet Accessibility Contrast Ratios; which are listed here:

    Primary Background (#E6F7F1) with Dark Text (#2D2D2D): 12.1:1
    Primary Accent (#3A6F74) with Light Text (#FFFFFF): 7.6:1
    Secondary Background (#B2C2E0) with Dark Text (#2D2D2D): 8.5:1
    Secondary Accent (#5C88C8) with Light Text (#FFFFFF): 4.5:1

These ratios meet or exceed WCAG 2.1 standards for both normal text and large text.
---

#### **Typography**

[Google Fonts](https://fonts.google.com/) was used to import the fonts 'Playfair Display' and 'Lora' as I thought this gave a classic/sophisticated feel to the site, appropriate for an old, well-established tennis club

---

#### **Imagery**

- I chose to use images of the club to give visitors an accurate view of what to expect when they arrive at the club.

---

Overall, the design was intended and created to be clean, clear and professional, avoiding any unnecessary details/information.

---

#### **Implementation**

- I (eventually) tried to adopt an iterative approach to building out each feature of the website. By focussing on one particular feature and building it out stage by stage I found it helped the work flow and removed the mental barriers to working, as well as making debugging simpler.
- An example of this iterative approach for the Availability model (which shows the user which Court is available to be booked) is as follows:
- 1) Add functionality for the admin to manually create availability. 2) Test manually using Python shell. 3) Test manually using admin dashboard. 4) Generate basic automatic tests (with help from AI). 5) Debug (if necessary). 6) Generate automatic tests for edge cases. 7) Debug. 8) Show on template
- By using this approach, I knew the feature worked at every stage before moving on, so if an error emerged I knew exactly where to focus on for bug fixes.
- By separating each feature and building in isolation, I anticipate it will make integrating the whole project together to be a smoother process, as I will be confident that each feature works as intended.

  #### **ERD**

  Entities:

| Entity      | Attributes                                                                                                  |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| Court       | court_number (PK, unique), court_type                                                                       |
| Availability| id (PK), date, start_time, end_time, is_available, court_id (FK)                                             |
| Booking     | id (PK), booking_date, booking_time, duration, is_active, user_id (FK), booked_by_id(FK), court_id(FK), availability_id (FK) |
| User        | id (PK), username (Unique), email, first_name, last_name, password |

Relationships:

*   Court 1:N Availability
*   User 1:N Booking
*   Availability 1:N Booking

---

## Tablet & Mobile View  
 
### **Desktop, Tablet & Mobile Differences**  

- To ensure responsivity I intend to use the Bootstrap grid to keep the website looking clean on all screen sizes.
  
---  

## **Testing**

## Basic Tests

| Test Category           | Description                                                                                                                                                                                             | Expected Outcome                                                                                                                                                | Successful? |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **Navigation**          | Verify that all menu links (e.g., Home, Book a Court, Login, Register, Dashboard) and buttons navigate to the correct pages.                                                                             | All links and buttons should direct to the intended pages.                                                                                                    |    yes         |
| **Booking Flow**        | Test the entire booking process: selecting a date, time slot, court, confirming the booking, and viewing the confirmation message.                                                                      | Users should be able to successfully book a court for a chosen time and date. The confirmation page should display the booking details.                               |    yes         |
| **Booking Availability** | Verify that booked time slots are correctly marked as unavailable on the booking page. Try booking overlapping time slots or the same court at the same time.                                        | The booking system should prevent double bookings and accurately reflect court availability.                                                                    |      yes       |
| **Date Selection**       | Check the date picker on the booking page. Verify that it displays the correct dates and allows users to navigate between months.                                                                        | The date picker should function correctly, allowing users to select any valid date.                                                                            |   yes          |
| **Login/Registration**    | Test the login and registration forms. Verify that valid credentials allow login and that appropriate error messages are displayed for invalid input (e.g., incorrect username/password, missing fields). | Users should be able to create new accounts and log in with valid credentials. Clear error messages should be shown for invalid input.                               |   yes          |
| **Logout**                | Test the logout functionality. Verify that users are logged out and redirected to the appropriate page (e.g., the homepage or login page).                                                              | Users should be successfully logged out and redirected appropriately.                                                                                           |    yes         |
| **Dashboard (My Bookings)** | After making a booking, verify that it appears correctly in the user's dashboard. Test the cancel booking functionality.                                                                                 | Bookings should be displayed in the dashboard with correct details. Cancelling a booking should remove it from the dashboard and make the time slot available again. |   yes          |
| **Form Validation**     | Check all forms (login, registration, booking) for required fields and proper error messages. Test with empty fields, invalid email addresses, etc.                                                       | Forms should provide clear and helpful error messages for invalid input.                                                                                      |   yes          |
| **Responsiveness**      | Check the layout on various screen sizes (desktop, tablet, mobile).                                                                                                                                  | Layout should adapt properly to different screen sizes, maintaining usability and readability.                                                                 |   yes          |
| **Link Accessibility**  | Ensure all links have descriptive text (avoid "click here").                                                                                                                                            | Link text should clearly indicate the destination or purpose of the link.                                                                                   |   yes          |


## Future Features  

- The ability to share bookings with another party
- Email confirmation of bookings
- Payment portal to be able to charge for courts
- Change membership functionality to allow anyone to book a court but give priority to a member (e.g members can book 10 days in advance rather than 7, and members get a 10% discount)
- Add a calendar to see upcoming events at the club
- Add a blog/news section to describe events which have happened at the club
- Be able to book more than one slot at a time, using an 'add to basket' system
- Be able to book slots on the half hour (e.g. 10.30-11.30)
- Be able to book slots for different time frames (e.g. 90 minutes)
  
## Technologies Used    

### **Languages Used**   

- HTML5
- CSS3
- Javascript
- Python3
- Django5

### **Frameworks, Libraries, Technologies & Programs Used**  

- Balsamiq - used to create wireframes
- GitHub - used to save and store all files for this website  
- Git - used for version control
- Google Fonts - fonts were imported from here 
- FontAwesome - icons and their associated kit were downloaded from here
- ChatGPT/Gemini - For user story refinement, debugging and guidance on the ideation of the project
- Google Dev Tools - to debug and for testing responsiveness 
- Google Lighthouse - for auditing the website
- W3C Validator - for validating the HTML and CSS code
- https://favicon.io - for favicon generation
- Django - for the booking system

---   

## Deployment
 
### Prerequisites

*   A Render account (create one at [https://render.com/](https://render.com/)).
*   A Git repository (GitHub, GitLab, Bitbucket, etc.) containing your Django project.
*   A working Django project with a `requirements.txt` file listing all dependencies.

### Steps

1.  **Prepare Your Project:**

    *   **`requirements.txt`:** Ensure you have a `requirements.txt` file in your project's root directory. You can generate it using:

        ```bash
        pip freeze > requirements.txt
        ```

    *   **`Procfile` (Important):** Create a file named `Procfile` (no extension) in your project's root directory with the following content:

        ```
        web: gunicorn your_project_name.wsgi --bind 0.0.0.0:$PORT
        ```

        Replace `your_project_name` with the name of your Django project's main directory (the one containing `settings.py`).

    *   **Static Files Configuration (Very Important):** Ensure your `settings.py` is configured for static files:

        ```python
        import os

        BASE_DIR = Path(__file__).resolve().parent.parent

        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        STATICFILES_DIRS = [
            BASE_DIR / 'static', #if you have a static folder in the root
        ]
        ```

        If you have static files in apps' static folders, make sure that `django.contrib.staticfiles` is in `INSTALLED_APPS` and use `{% load static %}` in your templates and `{% static 'path/to/file' %}` to reference them.

    *   **Database Configuration:** Configure your database settings in `settings.py`. For PostgreSQL on Render, use environment variables:

        ```python
        import dj_database_url
        import os

        DATABASES = {
            'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
        }
        ```

    *   **ALLOWED_HOSTS:** Set `ALLOWED_HOSTS` in `settings.py`:

        ```python
        ALLOWED_HOSTS = ['*'] # ONLY FOR DEVELOPMENT. When you have a custom domain or render provides you with one, put that in here instead.
        ```

    *   **Collect Static Files (Before Committing):** Run the following command locally:

        ```bash
        python manage.py collectstatic
        ```

        Commit the `staticfiles` directory that is created.

    *   **Commit Your Changes:** Commit all the changes to your Git repository.

2.  **Create a Web Service on Render:**

    *   Log in to your Render dashboard.
    *   Click "New +" and select "Web Service".
    *   Connect your Git repository.
    *   Give your service a name.
    *   Choose a region.
    *   Select the "Python" environment.
    *   Set the "Start Command" to: `gunicorn your_project_name.wsgi --bind 0.0.0.0:$PORT` (same as in your `Procfile`).
    *   Choose a plan (Free or paid).

3.  **Set Environment Variables (Database):**

    *   In your Render service's settings, go to the "Environment" tab.
    *   Add a new environment variable named `DATABASE_URL`.
    *   For PostgreSQL, the value should be in the format: `postgres://<user>:<password>@<host>:<port>/<database>`
    *   Render provides a PostgreSQL database addon which will give you this URL. Add the addon and Render will automatically add the `DATABASE_URL` environment variable.

4.  **Deploy:**

    *   Click "Save Changes" to deploy your service.

5.  **Migrate Database:**

    *   Once the deployment is complete, go to the "Shell" tab of your service on Render.
    *   Run the database migrations:

        ```bash
        python manage.py migrate
        ```

6.  **Access Your Application:**

    *   Render will provide you with a URL to access your deployed application.

### Common Issues and Troubleshooting

*   **Static Files Not Loading:** Double-check your `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS` settings, and ensure you ran `python manage.py collectstatic` and committed the `staticfiles` directory.
*   **Database Connection Errors:** Verify your `DATABASE_URL` environment variable is correct.
*   **Deployment Errors:** Check the Render logs for any error messages.
*   **`Procfile` Errors:** Make sure the `Procfile` is in the root directory and the command is correct.
*   **`ALLOWED_HOSTS`:** Ensure `ALLOWED_HOSTS` is correctly set in your settings.py file. Setting it to `*` is only for testing. In production, it should be set to your domain.


### **Initial testing plan**

I planned for this site to be accessible and legible on all screen sizes. I will use Chrome Dev Tools and multiple browsers to test, adjust and debug in the early stages.

### **Testing**    

Manual testing took place throughout the entire build using the Python shell and in built django admin dashboard for the models & views logic. 

#### **Availabilities**
Using the Python shell to create a slot, setting it to being available for booking by default:
new_slot = Availability.objects.create(
   ...:     court_id=1,
   ...:     day_of_week=0,
   ...:     start_time=time(9, 0),
   ...:     end_time=time(10, 0)
   ...: )
   ...: print(new_slot.is_available)
OUTPUT: True





### **Learning Points** 

#### **Use of AI**
- AI was primarily used for debugging and guidance on transferring elements the reference project (the medical booking system linked in credits) to be appropriate for a tennis club
- Gemini was used to generate the automated tests


#### **What Went Well & Even Better If**
##### **WWW**
- The project achieved its MVP and works as a system for booking tennis courts
- Good use of AI throughout, used chatGPT and Gemini against each other to help debug their own generated codes and carefully amended naming conventions as in previous projects I've not done that and got lost in a web 

##### **EBI**
- Project diverged slightly from the plan. e.g. I planned to have rescheduling pop up as a modal but I wasn't able to do that.
- Code could be cleaner in places

### **HTML and CSS Validation using W3C Validation**  

 Code validation is available [here](/docs/validations)

### **Lighthouse Audit**

Lighthouse website audit is available [here:](/docs/auditing)


## Credits  
  
### **Content References**
- Basic project was modelled from this tutorial: https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78. Used a combination of Gemini and chatGPT AIs to aid with repurposing to the tennis club where necessary.
- [Code Institute](https://codeinstitute.net/ie/), for their django deployment guide, [Codecademy](https://www.codecademy.com/) and [Free Code Camp](https://www.freecodecamp.org/) for their HTML/CSS/Javascript/Python learning material.
- [W3Schools](https://www.w3schools.com/) for additional learning material.
- [MDN Web Docs](https://developer.mozilla.org/) for tutorials on html, css, javascript and python.

