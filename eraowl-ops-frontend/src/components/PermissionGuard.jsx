import { useMemo } from 'react'
import useAuthStore from '../store/authStore'

/**
 * PermissionGuard - ควบคุมการแสดงผล UI ตามสิทธิ์ผู้ใช้
 * 
 * @param {Object} props
 * @param {string} props.module - ชื่อโมดูล (เช่น 'bom', 'admin', 'item')
 * @param {string} props.action - การกระทำ (เช่น 'create', 'approve', 'update')
 * @param {React.ReactNode} props.children - องค์ประกอบที่จะแสดงผล
 * @param {'hide'|'disable'} props.fallback - โหมดเมื่อไม่มีสิทธิ์: 'hide' (ซ่อน) หรือ 'disable' (ปิดการใช้งาน)
 * @param {Object} props.disabledProps - props เพิ่มเติมเมื่อ disabled (เช่น className, style)
 * @param {string} props.tooltip - ข้อความ tooltip เมื่อ disabled
 * @param {boolean} props.showTooltip - แสดง tooltip หรือไม่ (default: true)
 * 
 * @example
 * // ซ่อนปุ่มเมื่อไม่มีสิทธิ์
 * <PermissionGuard module="bom" action="approve" fallback="hide">
 *   <button>Approve</button>
 * </PermissionGuard>
 * 
 * @example
 * // ปิดการใช้งานปุ่มเมื่อไม่มีสิทธิ์
 * <PermissionGuard module="bom" action="create" fallback="disable">
 *   <button>Create BOM</button>
 * </PermissionGuard>
 */
export default function PermissionGuard({
  module,
  action,
  children,
  fallback = 'hide',
  disabledProps = {},
  tooltip,
  showTooltip = true,
}) {
  const hasPrivilege = useAuthStore((state) => state.hasPrivilege)
  const privileges = useAuthStore((state) => state.privileges)
  const isLoading = useAuthStore((state) => state.isLoading)

  const hasAccess = useMemo(() => {
    if (isLoading) return false
    return hasPrivilege(module, action)
  }, [isLoading, hasPrivilege, module, action])

  // กำลังโหลดสิทธิ์
  if (isLoading) {
    return (
      <div 
        className="permission-guard-loading"
        style={{
          opacity: 0.5,
          pointerEvents: 'none',
          transition: 'opacity var(--transition-base, 250ms)',
        }}
      >
        {children}
      </div>
    )
  }

  // มีสิทธิ์ - แสดงปกติ
  if (hasAccess) {
    return (
      <div 
        className="permission-guard-granted"
        style={{
          transition: 'opacity var(--transition-base, 250ms), transform var(--transition-base, 250ms)',
        }}
      >
        {children}
      </div>
    )
  }

  // ไม่มีสิทธิ์ - ใช้ fallback mode
  if (fallback === 'hide') {
    return null
  }

  // fallback === 'disable'
  const defaultTooltip = tooltip || `คุณไม่มีสิทธิ์ ${action} ในโมดูล ${module}`
  
  // Clone children และเพิ่ม disabled props
  const disabledChildren = useMemo(() => {
    if (!children) return null

    // ถ้า children เป็น element เดียว ให้เพิ่ม props
    if (typeof children === 'object' && children.props) {
      const { cloneElement } = require('react')
      return cloneElement(children, {
        disabled: true,
        'aria-disabled': true,
        title: showTooltip ? defaultTooltip : undefined,
        ...disabledProps,
        style: {
          ...children.props.style,
          opacity: 0.5,
          cursor: 'not-allowed',
          pointerEvents: 'auto',
          transition: 'opacity var(--transition-fast, 150ms)',
          ...disabledProps.style,
        },
      })
    }

    // ถ้าไม่ใช่ element ให้ wrap ด้วย div
    return (
      <div
        className="permission-guard-disabled"
        aria-disabled={true}
        title={showTooltip ? defaultTooltip : undefined}
        style={{
          opacity: 0.5,
          cursor: 'not-allowed',
          pointerEvents: 'auto',
          transition: 'opacity var(--transition-fast, 150ms)',
          ...disabledProps.style,
        }}
      >
        {children}
      </div>
    )
  }, [children, disabledProps, defaultTooltip, showTooltip])

  return disabledChildren
}

/**
 * PermissionGuardButton - เวอร์ชันเฉพาะสำหรับปุ่ม
 * ใช้งานง่ายกว่า PermissionGuard ปกติ
 */
export function PermissionGuardButton({
  module,
  action,
  children,
  fallback = 'disable',
  tooltip,
  ...buttonProps
}) {
  return (
    <PermissionGuard
      module={module}
      action={action}
      fallback={fallback}
      tooltip={tooltip}
      disabledProps={{
        className: `${buttonProps.className || ''} permission-guard-disabled-btn`,
      }}
    >
      <button {...buttonProps}>
        {children}
      </button>
    </PermissionGuard>
  )
}

/**
 * usePermission - Hook สำหรับตรวจสอบสิทธิ์
 * ใช้ในกรณีที่ต้องการตรวจสอบสิทธิ์ใน logic โดยไม่ต้องการ render
 */
export function usePermission(module, action) {
  const hasPrivilege = useAuthStore((state) => state.hasPrivilege)
  const isLoading = useAuthStore((state) => state.isLoading)

  return useMemo(() => {
    if (isLoading) return { hasAccess: false, isLoading: true }
    return {
      hasAccess: hasPrivilege(module, action),
      isLoading: false,
    }
  }, [isLoading, hasPrivilege, module, action])
}
