import { useQuery } from '@tanstack/react-query';
import { mcpCall } from '../lib/gateway';
import type { LpnEventResponse } from '../types/inventory';

export function useLpnEvents(lpnId: string) {
  return useQuery<LpnEventResponse>({
    queryKey: ['inv', 'lpn-events', lpnId],
    queryFn: () => mcpCall<LpnEventResponse>('inv.events.byLpn', { lpnId }),
    enabled: !!lpnId,
  });
}
