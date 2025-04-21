import { useEffect, useState } from 'react';
import { Transaction } from '../types/transaction';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function TransactionsPage() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${API_URL}/transactions/`)
      .then(res => res.json())
      .then(data => {
        console.log('Fetched transactions:', data);
        setTransactions(data);
      })
      .finally(() => setLoading(false));
  }, []);

  return (
    <div style={{ padding: 24 }}>
      <h1>Transactions</h1>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <table border={1} cellPadding={8}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Date</th>
              <th>Description</th>
              <th>Amount</th>
            </tr>
          </thead>
          <tbody>
            {transactions.map(tx => (
              <tr key={tx.id}>
                <td>{tx.id}</td>
                <td>{tx.date}</td>
                <td>{tx.description}</td>
                <td>{tx.amount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
