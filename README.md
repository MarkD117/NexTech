# Nextech - Your Source for Premium Computer Components and Systems

Welcome to Nextech, where we specialize in providing high-quality computer components and fully built systems tailored to meet your needs. Whether you're a gamer seeking top-tier hardware or a professional in search of reliable office setups and laptops, Nextech offers a diverse range of products to elevate your computing experience. From CPUs and GPUs to custom-built gaming PCs and office workstations, we prioritize quality, performance, and customer satisfaction. Explore our catalog and take the next step in enhancing your computing journey with Nextech.

The live project can be accessed [here](https://nextech-5db9177526a4.herokuapp.com/)

<p align="center">
    <img src="documentation/other/am-i-responsive-img.png"/>
</p>

## Index – Table of Contents

* [UI/UX](#uiux)
* [Agile Development](#agile-development)
* [User Stories](#user-stories)
* [Database Structure](#database-structure)
* [Wireframes](#wireframes)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Bug Fixes](#bug-fixes)
* [Known Bugs](#known-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

## UI/UX

### Design Overview
The primary objective of the website is to offer users a curated selection of products tailored to the needs of computer enthusiasts. With an intuitive design at its core, our platform prioritizes simplicity and ease of navigation. Products are prominently displayed across various pages, encouraging users to explore further, while bold colors are strategically used to enhance visibility and attract attention. The commitment to seamless user experience is evident in every aspect of the site, with effortless accessibility and self-explanatory features. On-screen feedback messages are employed to guide users effectively, ensuring a smooth and enjoyable browsing experience.

### Colour Scheme

The color scheme of the site was carefully selected to create a visually appealing and cohesive user experience. Rich black serves as the primary color for all text elements throughout the site, ensuring clear readability and a sleek aesthetic. It is also strategically employed alongside other blue buttons to accentuate differences between various interactive elements. Complementing the richness of black, white is utilized for the site background, providing a clean canvas for content and enhancing contrast. Additionally, white is applied to icons and text displayed on blue or black backgrounds, ensuring optimal visibility and legibility across all interfaces.

In terms of accent colors, Chrysler Blue takes center stage in the navigation menu, adding a pop of vibrancy and guiding users seamlessly through different sections of the site. This bold hue also doubles as a hover effect on Palatinate Blue buttons, enhancing interactivity and user engagement. Chrysler Blue is also applied to the prices of products, making them stand out more and catching the attention of users browsing through the offerings on the site. Palatinate Blue serves as the predominant color for most buttons on the site, offering a harmonious blend of sophistication and functionality. Finally, Periwinkle adds a touch of softness and elegance as the background color for product cards, providing a pleasant backdrop for showcasing the curated selection of products. Together, these carefully chosen colors contribute to a visually appealing and intuitive browsing experience for users.

[Coolors.co](https://coolors.co/) was used to generate the images of the colour palettes below.

#### Site Colour Pallet

<p align="center">
    <img src="documentation/other/nextech-color-scheme.png"/>
</p>

- `#050316` used for text elements and buttons.
- `#FBFBFE` used for site background and text on dark backgrounds.
- `#2F27CE` used for site nav and hover effect.
- `#DDDBFF` used for product card backgrounds.
- `#443DFF` used for buttons.


### Fonts & Icons
- The 'Poppins' font was used for all text on the site. 

This font was sourced from [Google Fonts](https://fonts.google.com/).

- Up Arrow icon used back to top button.
- Shopping Cart icon used for cart navigation items.
- Chevron Left used for back buttons.
- Chevron Right used for newsletter submit button.
- Hastag used for categories on product cards.
- Star used for product ratings.
- Lock used for checkout buttons.
- Mangifying Glass used for search functions.
- Rotate Right Arrow used for update product buttons.
- Trash Can used for delete product from cart buttons.
- User icon used for user profile
- Bars icon used for mobile navigation dropdown.

Icons sourced from [Font Awesome](https://fontawesome.com/).


## Agile Development

Launching this project alongside a GitHub Projects Page was a strategic decision aimed at effectively measuring and managing the anticipated workload. The primary objective was to outline the projected workload, identify key epics, and subsequently break them down into actionable user stories or bite-sized tasks. This approach allowed for a systematic approach to project management, ensuring clarity of goals and progress tracking throughout the development process.

To see Kanban please click [here](https://github.com/users/MarkD117/projects/7).

By utilizing GitHub Projects, I was able to organize tasks and assign priorities in the form of the GitHub labels to ensure timely completion of the site. At the initial planning stages, I meticulously designed each page, outlining the requirements and features I intended to incorporate. From these detailed page plans, I derived user stories that served as the backbone of the development process. 

These user stories were strategically implemented to ensure seamless functionality across the site, with a particular focus on the customer journey—from product discovery to cart addition and ultimately, final purchase. By prioritizing core functionalities and user interactions, I aimed to create an intuitive and efficient browsing experience for our users.

For each user story, acceptance criteria were established along with corresponding tasks. As tasks were completed, the respective box was checked off. Upon fulfillment of all components of the user story and meeting the acceptance criteria, the user story transitioned from the **'In Progress'** column to the **'Completed'** column.

#### User stories

####  Completed User Stories

Click on a user story below to be directed to the Kanban project to examine any of the additional details of the user stories. If the specific story does not appear automatically, please click on it from the project page for more details.

 1. [USER STORY: Product List](https://github.com/MarkD117/nextech/issues/2)
 2. [USER STORY: View Products Without an Account](https://github.com/MarkD117/nextech/issues/4)
 3. [USER STORY: Product Details](https://github.com/MarkD117/nextech/issues/5)
 4. [USER STORY: Deals and Special Offers](https://github.com/MarkD117/nextech/issues/7)
 5. [USER STORY: Total Price](https://github.com/MarkD117/nextech/issues/8)
 6. [USER STORY: Create Account](https://github.com/MarkD117/nextech/issues/9)
 7. [USER STORY: Login/Logout](https://github.com/MarkD117/nextech/issues/11)
 8. [USER STORY: Password Reset](https://github.com/MarkD117/nextech/issues/12)
 9. [USER STORY: Confirmation Email](https://github.com/MarkD117/nextech/issues/13)
 10. [USER STORY: User Profile](https://github.com/MarkD117/nextech/issues/14)
 11. [USER STORY: Filters](https://github.com/MarkD117/nextech/issues/15)
 12. [USER STORY: Product Categories](https://github.com/MarkD117/nextech/issues/16)
 13. [USER STORY: Product Search](https://github.com/MarkD117/nextech/issues/17)
 14. [USER STORY: Numerous Category Search](https://github.com/MarkD117/nextech/issues/18)
 15. [USER STORY: Viewing Search and Filter Results](https://github.com/MarkD117/nextech/issues/19)
 16. [USER STORY: Add to Cart](https://github.com/MarkD117/nextech/issues/20)
 17. [USER STORY: Quantity Selection](https://github.com/MarkD117/nextech/issues/22)
 18. [USER STORY: Adjust Cart Quantity](https://github.com/MarkD117/nextech/issues/23)
 19. [USER STORY: Secure and Easy Payment System](https://github.com/MarkD117/nextech/issues/24)
 20. [USER STORY: Order Confirmation](https://github.com/MarkD117/nextech/issues/25)
 21. [USER STORY: Order Email Confirmation](https://github.com/MarkD117/nextech/issues/26)
 22. [USER STORY: Newsletter](https://github.com/MarkD117/nextech/issues/27)
 23. [USER STORY: Contact Form](https://github.com/MarkD117/nextech/issues/28)
 24. [USER STORY: Adding Products](https://github.com/MarkD117/nextech/issues/38)
 25. [USER STORY: Edit/Update Products](https://github.com/MarkD117/nextech/issues/39)
 26. [USER STORY: Delete Products](https://github.com/MarkD117/nextech/issues/40)
 27. [USER STORY: Wishlist](https://github.com/MarkD117/nextech/issues/45)
 

####  Incompleted User Stories

The following user stories have been marked as incomplete, as they were considered non-essential for the core functionality of the site at this stage. However, they represent potential [Future Features](#future-features) to be implemented in future iterations. While these issues were initially closed upon completing the project's code, they have since been reopened, as I am eager to revisit and incorporate them into a future patch of the site.

The majority of the 18 out of 45 incomplete user stories pertain to a single app known as the forums app, along with the associated admin logic. While these features were deemed non-essential for the core functionality of the site during the initial development phase, they again represent potential additions for future updates.

 1. [USER STORY: Landing Page](https://github.com/MarkD117/nextech/issues/1)
 2. [USER STORY: Stock Availability](https://github.com/MarkD117/nextech/issues/3)
 3. [USER STORY: Multiple Product Images](https://github.com/MarkD117/nextech/issues/6)
 4. [USER STORY: Social Media Signup](https://github.com/MarkD117/nextech/issues/10)
 5. [USER STORY: Buy Now Button](https://github.com/MarkD117/nextech/issues/21)
 6. [USER STORY: Dedicated Forum](https://github.com/MarkD117/nextech/issues/29)
 7. [USER STORY: Create Forum Post](https://github.com/MarkD117/nextech/issues/30)
 8. [USER STORY: Edit/Update Posts](https://github.com/MarkD117/nextech/issues/31)
 9. [USER STORY: Delete Posts](https://github.com/MarkD117/nextech/issues/32)
 10. [USER STORY: Comment/Reply on Forum Posts](https://github.com/MarkD117/nextech/issues/33)
 11. [USER STORY: Post Detail View](https://github.com/MarkD117/nextech/issues/34)
 12. [USER STORY: Site Pagination](https://github.com/MarkD117/nextech/issues/35)
 13. [USER STORY: Forum Post Upvotes](https://github.com/MarkD117/nextech/issues/36)
 14. [USER STORY: Forum Search](https://github.com/MarkD117/nextech/issues/37)
 15. [USER STORY: Admin - Create Forum Post](https://github.com/MarkD117/nextech/issues/41)
 16. [USER STORY: Admin - Edit/Update Posts](https://github.com/MarkD117/nextech/issues/42)
 17. [USER STORY: Admin - Delete Forum Posts/Replies](https://github.com/MarkD117/nextech/issues/43)
 18. [USER STORY: View Contact Form Contents](https://github.com/MarkD117/nextech/issues/44)


## Database Structure

During the project's planning stages, [Lucid Chart](https://www.lucidchart.com/) played a crucial role in designing the initial database structure, facilitating the planning of data storage and relationships for the site.

Although the database structure for the forums app was initially planned during the development phase, changes were implemented due to time constraints and project scope, leading to the postponement of the forums app for the time being.

In place of the forums app, the wishlist feature and app were developed. Since this app and its corresponding database structure were not part of the initial plan, they were not included in the original database diagram.

Furthermore, it's worth noting that the profile image field in the UserProfile model was removed due to its perceived insignificance at the time. Originally intended for prominence within the forums, where each user's profile image would display alongside their posts and replies, this feature may be reconsidered for inclusion in a future patch

<p align="center">
    <img src="documentation/other/initial-database-structure.png"/>
</p>