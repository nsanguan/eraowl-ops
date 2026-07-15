import { useQuery } from '@tanstack/react-query';
import { mcpCall } from '../lib/gateway';
import type { OnHandResponse } from '../types/inventory';

interface OnHandParams {
  itemId?: string;
  locationId?: string;
  lpnId?: string;
  page?: number;
  limit?: number;
}

export function useOnHandList(params?: OnHandParams) {
  return useQuery<OnHandResponse>({
    queryKey: ['inv', 'on-hand', params],
    queryFn: () => mcpCall<OnHandResponse>('inv.onhand.list', params as Record<string, unknown>),
  });
}
