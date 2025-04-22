import { render, screen, waitFor } from '@testing-library/react'
jest.mock('../src/config/api', () => ({
  API_URL: 'http://localhost:8000',
}))
import TransactionsPage from '../src/pages/TransactionsPage'

const mockResponse = {
  ok: true,
  status: 200,
  json: () =>
    Promise.resolve([
      {
        id: '1',
        date: '2024-01-01',
        description: 'Test Transaction',
        amount: '123.45',
      },
    ]),
} as Response

const mockFetch = jest.fn(() => Promise.resolve(mockResponse))
global.fetch = mockFetch

describe('TransactionsPage', () => {
  it('renders transactions', async () => {
    render(<TransactionsPage />)
    await waitFor(() => {
      expect(screen.getByText('Test Transaction')).toBeInTheDocument()
      expect(screen.getByText('123.45')).toBeInTheDocument()
    })
  })
})
