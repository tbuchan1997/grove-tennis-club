# Grove Tennis Club

[View live project here!]()

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

## Tablet & Mobile View  
 
### **Desktop, Tablet & Mobile Differences**  

- To ensure responsivity I intend to use the Bootstrap grid to keep the website looking clean on all screen sizes.
  

---  

## **Testing**

## Basic Tests

| Test Category             | Description                                                             | Expected Outcome                                            | Successful? |
|---------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------|-------------|
| **Navigation**            | Verify that all menu links and buttons navigate to the correct pages.   | All links and buttons should direct to the intended pages.  |      yes       |
| **Responsiveness**        | Check the layout on various screen sizes (desktop, tablet, mobile).     | Layout should adjust properly on all devices and screen sizes. |     yes     |
| **Accessibility**         | Test keyboard navigation for all interactive elements.                  | Users should be able to navigate using only the keyboard.   |        yes     |
| **Colour Contrast**        | Ensure text has high contrast against background colours.                | Text should be legible, meeting WCAG contrast guidelines.   |       yes      |
| **Image Alt Text**        | Verify that all images have descriptive alt text for screen readers.    | Alt text should describe images meaningfully for users with visual impairments. |    yes         |
| **Form Validation**       | Check form inputs for required fields and proper error messages.        | Forms should provide clear error messages for invalid input. |         yes    |
| **Performance**           | Measure page load speed and ensure media loads efficiently.             | Pages should load quickly, and images should not delay rendering. |     no        |
| **Link Accessibility**    | Ensure all links have meaningful text for screen readers.               | Links should be descriptive (no "click here" or "read more"). |       yes      |
| **Browser Compatibility** | Test site on popular browsers (Chrome, Firefox, Safari, Edge).          | Site should display correctly and function as expected on all tested browsers. |      no       |

| **Content Consistency**   | Review site for consistent fonts, colours, and layout across pages.     | All pages should maintain a uniform look and feel. |        yes     |

Need to further work on sizing images and optimising the top fold of the website to improve performance.
Could not get text and background colour compatibility for chrome. Hero section and navbar are not accessible as a result.



## Future Features  
- 
  
## Technologies Used    

### **Languages Used**   

- HTML5
- CSS3
- Javascript
- Python3

### **Frameworks, Libraries, Technologies & Programs Used**  

- Balsamiq - used to create wireframes
- GitHub - used to save and store all files for this website  
- Git - used for version control
- Google Fonts - fonts were imported from here 
- FontAwesome - icons and their associated kit were downloaded from here
- ChatGPT - For user story refinement, debugging and guidance on the ideation of the project
- Google Dev Tools - to debug and for testing responsiveness 
- Google Lighthouse - for auditing the website
- W3C Validator - for validating the HTML and CSS code
- https://favicon.io - for favicon generation
- Django - for the booking system

---   

## Deployment

### **How to deploy**  



### **Initial testing plan**

I planned for this site to be accessible and legible on all screen sizes. I will use Chrome Dev Tools and multiple browsers to test, adjust and debug in the early stages.

### **Testing**    

Testing took place throughout the entire build using the Python shell and in built django admin dashboard for the models & views logic. 

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



#### **What Went Well & Even Better If**
##### **WWW**


##### **EBI**


### **HTML and CSS Validation using W3C Validation**  

 Code validation is available [here](/docs/validations)

### **Lighthouse Audit**

Lighthouse website audit is available [here:](/docs/auditing)


## Credits  
  
### **Content References**
- All content templates are generated by [ChatGPT](https://chatgpt.com/), but amended and finalised by me.
- [Code Institute](https://codeinstitute.net/ie/), [Codecademy](https://www.codecademy.com/) and [Free Code Camp](https://www.freecodecamp.org/) for their HTML/CSS learning material.
- [W3Schools](https://www.w3schools.com/) for additional learning material.
- [MDN Web Docs](https://developer.mozilla.org/) for tutorials on html and css.


### **Media References**  
  











![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Tom Buchan,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **June 18, 2024**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py` if your Python file is named `app.py`, of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

By Default, Gitpod gives you superuser security privileges. Therefore, you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
