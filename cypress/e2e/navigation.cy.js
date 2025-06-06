describe('Navigation Tests', () => {
  beforeEach(() => {
    cy.visit('http://localhost:1234')
  })

  it('navigates to Card Sets', () => {
    cy.get('[data-cy=nav-card-sets]').click()
    cy.contains('Create Set')
  })

  it('navigates to About', () => {
    cy.get('[data-cy=nav-about]').click()
    cy.contains('About Study Night')
  })

  it('navigates to Home', () => {
    cy.get('[data-cy=nav-home]').click()
    cy.contains('Welcome to Study Night')
  })
})
