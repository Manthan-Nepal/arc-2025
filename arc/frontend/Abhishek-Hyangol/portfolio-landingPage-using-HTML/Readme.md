# HTML Learning

## Key Concepts Learned
    -ARIA(Accessible Rich Internet Applications):
        -I learned how ARIA attributes enhances accessibility for screen readers.
        -Used `aria-label`, `aria-labelledby`, and `role` attributes in HTML.
        -The landmarks like role will help screen readers for better accessibility.
        -HTML5 interactive elements are accessible by screen readers but non-interactive elements like <div>, <span> aren't so it helps for non-reactive elements to be accessible.
        -So in form handling ARIA can be best use for customizable error addressing and commanding.
        -Form submission as well as error information can be efficiently conveyed.


## CSS

# CSS Selectors
    -Selectors are those that tells which tells us which HTML element is to be styled. 
    -Here i implemented class, Id, Universal, Descendant and Pseudo Selectors to style the HTML elements.

# Box Modal 
    - Box modal in CSS simply means the box like shape made with margin, border, padding and content.
    - Margin is the space between the border and the external environment like between two boxes or between box and screen.
    - Border is the line that separates the contains.
    - Padding is the internal space between the border and the content.
    - Content is the actual HTML elements.

# Display Properties
    -The display property specifies the display behavior (the type of rendering box) of an element.
    - We have different display properties like flex, grid, inline, block, etc..
    - Here i have used flex and grid.
    - They also helps to make page responsive.

# Position
    -The position property specifies the type of positioning method used for an element (static, relative, fixed, absolute or sticky).
    - We have properties like [ Top, Bottom, Left, Right ] in CSS but we cannot use them unless we specify the positioning method and the position of element also depends upon what kind of position property is used.
    - Static position means the position will just move with the flow Top, Left, Right, Bottom won't work.
    - Relative positioning means the element will be positioned relative to it's normal flow like if positioning wasn't used then the code will have one flow which is original after using positioning the left,right whatever properties is given will be applied with respect to the original points. And the space left by the relative position will be left vacant no other element will adjust itself to fit in that.
    - Fixed positioning means the element will be positioned with respect to the viewport and will be fixed even if the screen is scrolled. Unlike relative it won't leave any vacant space.
    - absolute positioning means the element will be positioned with respect to the nearest ancestor with position value relative, absolute or fixed. Keep it in mind it most be ancestor. If there are no ancestor then it will position itself with respect to <body> or <html>.
    -sticky positioning property lies somewhere between relative and fixed. It means it behaves as relative until certain condition is met then sticks to behave as fixed. For this positioning we must use at least one property left, right, top, bottom. So if top:0 is kept for element in center it keep tracks of scrolling and while scrolling if that tag reaches the top making top:0 that element will be sticked making it fix. For example in these .md files in VScode anything written using hash will inherit sticky property and will be fixed according to the scroll. 
