import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders Movie Explorer title', () => {
  render(<App />);
  const heading = screen.getByText(/Movie Explorer/i);
  expect(heading).toBeInTheDocument();
});