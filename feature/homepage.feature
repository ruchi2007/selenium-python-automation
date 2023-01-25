Feature: Home Page
  Scenario: user should logout successfully
    Given i go to home page
    When i click logout_icon
    And i click logout_button
    Then i should see login page


