import { useState } from 'react';
import { useTheme } from '../../providers/ThemeProvider';
import { ColorPicker } from '../ui/ColorPicker';
import { SegmentedControl } from '../ui/SegmentedControl';

export function ThemeRoller() {
  const { config, setMode, setPrimaryColor, setBorderRadius, resetTheme } = useTheme();
  const [isOpen, setIsOpen] = useState(false);

  // Pre-defined color palettes for OKLCH strings that work well in Tailwind
  // We provide exact OKLCH strings since the user might want a specific theme
  const presetColors = [
    { name: 'Default (Blue)', value: 'oklch(0.45 0.14 260)' },
    { name: 'Redstell (Axon)', value: 'oklch(0.45 0.16 30)' },
    { name: 'Emerald', value: 'oklch(0.55 0.15 150)' },
    { name: 'Violet', value: 'oklch(0.55 0.15 300)' },
  ];

  return (
    <>
      {/* Floating Action Button */}
      <button
        onClick={() => setIsOpen(true)}
        className="bg-primary text-primary-foreground focus:ring-primary/30 fixed bottom-6 right-6 z-50 flex h-12 w-12 items-center justify-center rounded-full shadow-lg transition-transform hover:scale-110 focus:outline-none focus:ring-4"
        aria-label="Open Theme Configurator"
        title="Theme Configurator"
      >
        <span className="material-symbols-outlined !text-[24px]">palette</span>
      </button>

      {/* Backdrop */}
      {isOpen && (
        <div
          className="fixed inset-0 z-[60] bg-black/20 transition-opacity"
          onClick={() => setIsOpen(false)}
        />
      )}

      {/* Side Drawer */}
      <div
        className={`bg-surface-container-lowest border-outline-variant fixed right-0 top-0 z-[70] flex h-full w-[360px] max-w-[90vw] transform flex-col border-l shadow-2xl transition-transform duration-300 ease-in-out ${
          isOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        {/* Header */}
        <div className="border-outline-variant bg-surface-container-low flex items-center justify-between border-b p-4">
          <h2 className="text-on-surface flex items-center gap-2 text-lg font-black">
            <span className="material-symbols-outlined text-primary">format_paint</span>
            Theme Roller
          </h2>
          <button
            onClick={() => setIsOpen(false)}
            className="hover:bg-outline-variant/30 text-on-surface-variant flex h-8 w-8 items-center justify-center rounded-full transition-colors"
          >
            <span className="material-symbols-outlined !text-[20px]">close</span>
          </button>
        </div>

        {/* Content */}
        <div className="custom-scrollbar flex flex-1 flex-col gap-8 overflow-y-auto p-6">
          {/* Appearance (Light / Dark) */}
          <div className="flex flex-col gap-3">
            <label className="text-on-surface-variant text-xs font-bold uppercase tracking-wider">
              Appearance
            </label>
            <SegmentedControl
              fullWidth
              options={[
                { value: 'light', label: 'Light', icon: 'light_mode' },
                { value: 'dark', label: 'Dark', icon: 'dark_mode' },
                { value: 'system', label: 'System', icon: 'desktop_windows' },
              ]}
              value={config.mode}
              onChange={(v) => setMode(v as any)}
            />
          </div>

          {/* Primary Accent Color */}
          <div className="flex flex-col gap-3">
            <label className="text-on-surface-variant text-xs font-bold uppercase tracking-wider">
              Primary Accent Color
            </label>

            <div className="mb-2 grid grid-cols-4 gap-2">
              {presetColors.map((preset) => (
                <button
                  key={preset.name}
                  onClick={() => setPrimaryColor(preset.value)}
                  title={preset.name}
                  className={`mx-auto h-10 w-10 rounded-full border-2 transition-transform hover:scale-110 ${
                    config.primaryColor === preset.value ||
                    (!config.primaryColor && preset.name.includes('Default'))
                      ? 'border-on-surface scale-110 shadow-md'
                      : 'border-transparent shadow-sm'
                  }`}
                  style={{ backgroundColor: preset.value }}
                />
              ))}
            </div>

            <div className="text-outline mb-1 text-xs">Or enter a custom HEX value:</div>
            {/* We allow setting hex here. It works perfectly with Tailwind v4 overriding the variable */}
            <ColorPicker
              value={config.primaryColor?.startsWith('#') ? config.primaryColor : '#2563eb'}
              onChange={(val) => setPrimaryColor(val)}
            />
          </div>

          {/* Border Radius */}
          <div className="flex flex-col gap-3">
            <label className="text-on-surface-variant text-xs font-bold uppercase tracking-wider">
              Border Radius
            </label>
            <SegmentedControl
              fullWidth
              options={[
                { value: '0rem', label: 'Sharp' },
                { value: '0.375rem', label: 'Slight' },
                { value: '0.625rem', label: 'Rounded' },
                { value: '1.5rem', label: 'Pill' },
              ]}
              value={config.borderRadius || '0.625rem'}
              onChange={(v) => setBorderRadius(v)}
            />
          </div>
        </div>

        {/* Footer */}
        <div className="border-outline-variant bg-surface-container-low flex justify-end border-t p-4">
          <button
            onClick={resetTheme}
            className="text-on-surface bg-surface-container hover:bg-outline-variant/30 border-outline-variant rounded-lg border px-4 py-2 text-sm font-bold transition-colors"
          >
            Reset to Default
          </button>
        </div>
      </div>
    </>
  );
}
