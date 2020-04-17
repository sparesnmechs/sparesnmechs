Feature: Homepage improvements

    Rework done on the homepage to move it closer to achieve it's goals. These features
    only apply to the homepage (Landing page).

    Background:
        Given the landing page on a phone web and desktop web are treated separately

    Scenario: Adding car model and car make filter forms
        Given the phone web page
        When the user opens the landing page
        Then there should be a form for filtering using car make and car model on the jumbotron
        Then there should be a button for advanced searching

    Scenario: Adding year of manufacture to the filters
        Given the phone and desktop web pages
        When the user chooses the advanced search option
        Then alongside the available filters should be a filter for year of manufacture

    Scenario: Update finding mechanic prompt
        Given the phone and desktop web pages
        Then the find mechanic prompt should be changed to find a garage/mechanic instead

    Scenario: Update the hero image
        Given the phone and desktop web pages
        Then the existing hero image should have a sample product as its background
        And the sample product should be a complete representation of an actual product

    Scenario: Phone web page navigation bar
        Given the phone web page
        Then the navigation bar should be at the bottom
        And it should contain:
        * Home button
        * Sell a part
        * Request a part
        * User profile

    Scenario: Desktop web page navigation bar
        Given the desktop web page
        Then the navigation bar should resemble (jiji.co.ke)
        And should contain:
        * Logo
        * Search bar
        * Sell a part
        * Request a part
        * Profile

    Scenario: Request a part
        Given both phone and desktop web pages
        When a part is not found
        Then a user can place a request for the part
        And an email will be sent to the admin/sparesnmechs email

    Scenario: Centering the elements
        Given the phone and web pages categories
        Then the should all be centered

    Scenario: Displaying items in the categories
        Given items in a category
        Then the container should just display enough information
        * Image
        * Name
        * Price information
        * Location
        Then the conatiner holding the items should be clickable to give more details
        And the containers should be aligned vertically
