Feature: Favoritmarkering av bok

  Scenario: Användaren markerar "Matz lär dig baka" som favorit
    Given att användaren är på hemsidan efter att boken "Matz lär dig baka" lagts till
    When användaren öppnar boklistan
    And användaren klickar på hjärtikonen för boken "Matz lär dig baka"
    Then ska boken "Matz lär dig baka" vara markerad som favorit
