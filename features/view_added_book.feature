Feature: Visa tillagd bok
  Scenario: Boken visas sist i listan efter att den lagts till
    Given att användaren har lagt till boken "Matz lär dig baka" av "Matz Eliasson"
    Then ska boken "Matz lär dig baka" av "Matz Eliasson" visas i listan
