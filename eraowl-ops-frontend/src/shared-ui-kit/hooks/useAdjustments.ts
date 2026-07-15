import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { mcpCall } from '../lib/gateway';
import type { AdjustmentRecord } from '../types/inventory';

export function usePendingAdjustments() {
  return useQuery<AdjustmentRecord[]>({
    queryKey: ['inv', 'adjustments', 'pending'],
    queryFn: () => mcpCall<AdjustmentRecord[]>('inv.adjustments.pending'),
  });
}

export function useApproveAdjustment() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: string) => mcpCall<{ message: string }>('inv.adjustments.approve', { id }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['inv', 'adjustments'] }),
  });
}

export function useRejectAdjustment() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: (id: string) => mcpCall<{ message: string }>('inv.adjustments.reject', { id }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['inv', 'adjustments'] }),
  });
}
