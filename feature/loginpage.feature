Feature: Login Page
  As a valid user i should able to login successfully
  In order to login successfully
  As a valid user
  I want to enter valid credential and click submit button

  Scenario: User should login successfully with valid credentials
    Given I am in login page
    When I enter valid user
    And I enter valid password
    And I click on submit button
    Then I should land to home page