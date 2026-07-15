import { useQuery } from '@tanstack/react-query';
import { mcpCall } from '../lib/gateway';
import type { StockSummary } from '../types/inventory';

export function useStockSummary() {
  return useQuery<StockSummary>({
    queryKey: ['inv', 'stock-summary'],
    queryFn: () => mcpCall<StockSummary>('inv.stock.summary'),
  });
}
