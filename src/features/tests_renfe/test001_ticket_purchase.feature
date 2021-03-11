Feature: Ticket purchase in renfe


  Scenario: Ticket purchase round trip (With cookies and navigate to section billetes)
    Given Site to navigate: "https://www.renfe.com/es/es"
    And Accept cookies all
    And Go to section: "Viajar-Tarifas-Billetes"
    When I want to go from "MADRID (TODAS)" to "BARCELONA (TODAS)"
    And Select date in calendar
    And Submit
    And Select basic price round trip
    And Wait "5" seconds

  Scenario: Ticket purchase round trip (without step cookies)
    Given Site to navigate: "https://www.renfe.com/es/es"
    When I want to go from "MADRID (TODAS)" to "BARCELONA (TODAS)"
    And Select date in calendar
    And Submit
    And Select basic price round trip
    And Wait "5" seconds




