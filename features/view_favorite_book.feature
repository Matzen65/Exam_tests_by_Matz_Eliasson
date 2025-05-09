Feature: Visa favoritbok


  Scenario: Användaren ser den favoritmarkerade boken i "Mina böcker"
    Given att användaren är på hemsidan och har markerat boken "Matz lär dig baka" som favorit
    When användaren klickar på knappen "Mina böcker"
    Then ska boken "Matz lär dig baka" visas i listan med favoritböcker