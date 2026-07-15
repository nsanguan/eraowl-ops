# AxonOS Shared UI Kit: APEX-Style Components

Welcome to the **AxonOS Shared UI Kit**. This directory contains a comprehensive suite of reusable React components meticulously designed to mirror the powerful data-density and functional patterns of the **Oracle APEX Universal Theme**, while adhering to the modern AxonOS design tokens and dark/light modes.

## Table of Contents

- [Core Form Controls & Filters](#core-form-controls--filters)
  - [ShuttleControl](#shuttlecontrol)
  - [FacetedSearch](#facetedsearch)
  - [LovModal](#lovmodal)
  - [DateRangePicker](#daterangepicker)
  - [NumberSpinner](#numberspinner)
  - [SwitchToggle](#switchtoggle)
- [Data Presentation Regions](#data-presentation-regions)
  - [CardsRegion](#cardsregion)
  - [TimelineRegion](#timelineregion)
  - [BadgeList](#badgelist)
  - [MasterDetailSplit](#masterdetailsplit)
- [Advanced Interactions](#advanced-interactions)
  - [Wizard](#wizard)
  - [DropzoneUpload](#dropzoneupload)
  - [RichTextEditor](#richtexteditor)
- [Theming & Colors](#theming--colors)

---

## Core Form Controls & Filters

### ShuttleControl
A dual-listbox control allowing users to move multiple items between "Available" and "Selected" lists. It features built-in search, "move all" controls, and item reordering.

**Usage:**
```tsx
import { ShuttleControl } from '@shared-ui/components/ui/ShuttleControl';

const [selected, setSelected] = useState<string[]>([]);

<ShuttleControl
  availableItems={[
    { id: '1', label: 'Admin Role', description: 'Full access' },
    { id: '2', label: 'User Role', description: 'Read-only access' }
  ]}
  selectedItems={selectedDataObjects}
  onChange={(newIds) => setSelected(newIds)}
/>
```

### FacetedSearch
A sidebar filtering component containing collapsible groups of checkboxes or radio buttons, commonly used alongside data grids or cards.

**Usage:**
```tsx
import { FacetedSearch } from '@shared-ui/components/ui/FacetedSearch';

const [filterState, setFilterState] = useState({});

<FacetedSearch
  facets={[
    { id: 'status', label: 'Status', type: 'checkbox', options: [
      { value: 'ACTIVE', label: 'Active', count: 12 },
      { value: 'INACTIVE', label: 'Inactive', count: 4 }
    ]}
  ]}
  state={filterState}
  onChange={setFilterState}
  onClear={() => setFilterState({})}
/>
```

### LovModal
A powerful "Search and Select" modal (List of Values) matching the EBS pattern. It displays a search bar and a data grid with radio-button selection.

**Usage:**
```tsx
import { LovModal } from '@shared-ui/components/ui/LovModal';

<LovModal
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
  title="Partner"
  columns={[{ key: 'code', header: 'Code' }, { key: 'name', header: 'Name' }]}
  data={partnerList}
  searchOptions={[{ key: 'name', label: 'Name' }]}
  onSelect={(row) => handleSelect(row)}
/>
```

### DateRangePicker
A standardized dual-date input for selecting a start and end date.

**Usage:**
```tsx
import { DateRangePicker } from '@shared-ui/components/ui/DateRangePicker';

<DateRangePicker
  label="Invoice Date"
  startDate={range.start}
  endDate={range.end}
  onChange={({ startDate, endDate }) => setRange({ start: startDate, end: endDate })}
/>
```

### NumberSpinner
A numeric input with built-in increment/decrement controls, step handling, and min/max clamping.

**Usage:**
```tsx
import { NumberSpinner } from '@shared-ui/components/ui/NumberSpinner';

<NumberSpinner
  label="Quantity"
  value={qty}
  onChange={setQty}
  min={1}
  max={99}
/>
```

### SwitchToggle
A stylized boolean toggle switch that replaces standard checkboxes.

**Usage:**
```tsx
import { SwitchToggle } from '@shared-ui/components/ui/SwitchToggle';

<SwitchToggle
  checked={isActive}
  onChange={setIsActive}
  label="Is Active"
/>
```

---

## Data Presentation Regions

### CardsRegion
A responsive grid of cards. Supports icons, titles, body text, badges, and primary/secondary actions.

**Usage:**
```tsx
import { CardsRegion } from '@shared-ui/components/ui/CardsRegion';

<CardsRegion
  columns={3}
  items={[
    {
      id: '1', title: 'John Doe', subtitle: 'Developer',
      badge: 'Active', badgeColor: 'success',
      icon: 'person',
      actions: [{ label: 'Edit', onClick: (data) => edit(data) }]
    }
  ]}
/>
```

### TimelineRegion
A vertical timeline component ideal for displaying approval histories or audit trails.

**Usage:**
```tsx
import { TimelineRegion } from '@shared-ui/components/ui/TimelineRegion';

<TimelineRegion
  events={[
    { id: '1', title: 'PO Approved', timestamp: new Date(), user: 'Admin', status: 'success', icon: 'check_circle' }
  ]}
/>
```

### BadgeList
A horizontal list or grid of KPI metric badges.

**Usage:**
```tsx
import { BadgeList } from '@shared-ui/components/ui/BadgeList';

<BadgeList
  items={[
    { id: '1', label: 'Total Invoices', value: '1,420', color: 'primary', icon: 'receipt' }
  ]}
/>
```

### MasterDetailSplit
A layout component that handles the classic Master-Detail view, allowing horizontal or vertical orientations.

**Usage:**
```tsx
import { MasterDetailSplit } from '@shared-ui/components/ui/MasterDetailSplit';

<MasterDetailSplit
  orientation="horizontal"
  masterTitle="Invoices"
  masterContent={<InteractiveGrid data={invoices} />}
  detailTitle="Invoice Lines"
  detailContent={<InteractiveGrid data={selectedInvoiceLines} />}
/>
```

---

## Advanced Interactions

### Wizard
A multi-step process indicator and container for complex form flows.

**Usage:**
```tsx
import { Wizard } from '@shared-ui/components/ui/Wizard';

<Wizard
  title="Create Purchase Order"
  steps={[
    { id: 'header', title: 'Header Details', content: <HeaderForm /> },
    { id: 'lines', title: 'Lines', content: <LinesGrid /> }
  ]}
  onComplete={() => submitForm()}
  onCancel={() => close()}
/>
```

### DropzoneUpload
An APEX-style drag-and-drop file upload region.

**Usage:**
```tsx
import { DropzoneUpload } from '@shared-ui/components/ui/DropzoneUpload';

<DropzoneUpload
  label="Attachments"
  onFilesAdded={(files) => handleUpload(files)}
  maxSize={5 * 1024 * 1024} // 5MB
/>
```

### RichTextEditor
A standardized wrapper for rich text input utilizing `contentEditable` and standard formatting commands.

**Usage:**
```tsx
import { RichTextEditor } from '@shared-ui/components/ui/RichTextEditor';

<RichTextEditor
  label="Comments"
  value={htmlContent}
  onChange={setHtmlContent}
  height="250px"
/>
```

---

---

## Extended Form Controls & Indicators

### ColorPicker
A styled input for selecting a hexadecimal color.

**Usage:**
```tsx
import { ColorPicker } from '@shared-ui/components/ui/ColorPicker';

<ColorPicker
  label="Theme Color"
  value={themeColor}
  onChange={setThemeColor}
/>
```

### RatingStars
A 5-star rating input commonly used for feedback.

**Usage:**
```tsx
import { RatingStars } from '@shared-ui/components/ui/RatingStars';

<RatingStars
  label="Satisfaction"
  value={rating}
  onChange={setRating}
/>
```

### RangeSlider
A visual horizontal slider for numeric values within a range.

**Usage:**
```tsx
import { RangeSlider } from '@shared-ui/components/ui/RangeSlider';

<RangeSlider
  label="Completion %"
  min={0}
  max={100}
  value={progress}
  onChange={setProgress}
/>
```

### ProgressBar
A read-only linear progress indicator.

**Usage:**
```tsx
import { ProgressBar } from '@shared-ui/components/ui/ProgressBar';

<ProgressBar
  label="Upload Progress"
  value={45}
  status="primary"
  animated
/>
```

### SegmentedControl
A horizontal group of buttons acting as a mutually exclusive toggle (like radio buttons).

**Usage:**
```tsx
import { SegmentedControl } from '@shared-ui/components/ui/SegmentedControl';

<SegmentedControl
  options={[
    { value: 'grid', label: 'Grid', icon: 'grid_view' },
    { value: 'list', label: 'List', icon: 'view_list' }
  ]}
  value={viewMode}
  onChange={setViewMode}
/>
```

---

## Rich Content Regions

### AccordionRegion
A stacked list of collapsible panels.

**Usage:**
```tsx
import { AccordionRegion } from '@shared-ui/components/ui/AccordionRegion';

<AccordionRegion
  items={[
    { id: '1', title: 'Advanced Settings', icon: 'settings', content: <AdvancedSettingsForm /> }
  ]}
/>
```

### HeroRegion
A large banner region placed at the top of a page.

**Usage:**
```tsx
import { HeroRegion } from '@shared-ui/components/ui/HeroRegion';

<HeroRegion
  title="Dashboard"
  subtitle="Welcome back, Admin"
  icon="space_dashboard"
  actions={<button>Create New</button>}
/>
```

### MediaList
A list view where each item displays a leading image/avatar and a trailing badge.

**Usage:**
```tsx
import { MediaList } from '@shared-ui/components/ui/MediaList';

<MediaList
  items={[
    { id: 1, title: 'Jane Doe', subtitle: 'Manager', avatarText: 'JD', badge: 'Online', badgeColor: 'success' }
  ]}
/>
```

### CommentsRegion
A structured region for displaying an activity stream with a reply box.

**Usage:**
```tsx
import { CommentsRegion } from '@shared-ui/components/ui/CommentsRegion';

<CommentsRegion
  comments={[
    { id: 1, author: 'Admin', timestamp: new Date(), content: 'Please review this PO.', avatarText: 'AD' }
  ]}
  onSubmitComment={async (content) => await saveComment(content)}
/>
```

---

## Theming & Colors
All components are built exclusively using the AxonOS utility classes mapping to CSS custom properties. You never need to hardcode hex colors.
- **Backgrounds**: `bg-surface-container-lowest`, `bg-surface-container`, `bg-surface-container-high`
- **Text**: `text-on-surface`, `text-on-surface-variant`, `text-outline`
- **Accents**: `text-primary`, `bg-primary`, `bg-primary-foreground`
- **Statuses**: `bg-error`, `text-error`, `bg-green-500`, `text-yellow-500`

By adhering to these classes, all UI components will automatically switch between Dark Mode and Light Mode instantly.
