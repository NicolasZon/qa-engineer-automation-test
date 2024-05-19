@regression_tests

Feature: Validate navigation to menu pages

  Scenario Outline: Navigate between countries and validate the URL
      Given I navigate to the kayak main page
      When  I click on the "<name>" "<type>"
      Then I should be in the "<name>" page
    Examples:
      | name        | type   |
      | flights     | option |
      | stays       | option |
      | cars        | option |
      | citybreaks  | option |
