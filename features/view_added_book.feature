
Feature: Användaren lägger till en bok samt kontrollera att boken hamnar nederst i listan med böcker


  Scenario: Boken ska läggas till samt visas sist i listan på böcker efter att den lagts till
    Given att användaren har öppnat sidan "lägg till bok"
    Then att användaren lägger till boken "Matz lär dig baka" av "Matz Eliasson"
    And ska boken "Matz lär dig baka" av "Matz Eliasson" visas nederst i listan
