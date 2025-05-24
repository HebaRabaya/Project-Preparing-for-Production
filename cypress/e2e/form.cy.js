describe('Form Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:1234')
  })

  it('creates a new set with valid input', () => {
    cy.get('[data-cy=nav-create-set]').click()
    cy.get('[data-cy=set-name]').type('Math')
    cy.get('[data-cy=create-set-btn]').click()
    cy.contains('Math')
  })

  it('shows error when input is empty', () => {
    cy.get('[data-cy=nav-create-set]').click()
    cy.get('[data-cy=create-set-btn]').click()
    cy.contains('Please enter a name')
  })
})
