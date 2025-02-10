Feature: Basic Calculator

  Scenario: Add two numbers
    Given I have two numbers 3 and 5
    When I add the numbers
    Then the result should be 8

  Scenario: Subtract two numbers
    Given I have two numbers 10 and 4
    When I subtract the numbers
    Then the result should be 6
