import { render, screen, waitFor } from '@testing-library/react';
import TransactionsPage from '../src/pages/TransactionsPage';

global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve([
      {
        id: '1',
        date: '2024-01-01',
        description: 'Test Transaction',
        amount: '123.45',
      },
    ]),
  })
) as jest.Mock;

describe('TransactionsPage', () => {
  it('renders transactions', async () => {
    render(<TransactionsPage />);
    await waitFor(() => {
      expect(screen.getByText('Test Transaction')).toBeInTheDocument();
      expect(screen.getByText('123.45')).toBeInTheDocument();
    });
  });
});
