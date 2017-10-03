Feature: As end user I want to search behave on google

  Scenario: Search behave on google
    Given I at google search homepage
    When I search for "behave" keyword
    Then I should see "behave" search result
    And I should see "behave" official homepage