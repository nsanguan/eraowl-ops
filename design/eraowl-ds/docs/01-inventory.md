# Component Inventory — EraOwl Design System

> **Generated:** 2026-07-14 &nbsp;|&nbsp; **Version:** 1.0.0 &nbsp;|&nbsp; **Target:** APEX 24.x + Universal Theme

---

## Legend

| Column | Description |
|--------|-------------|
| **Usage Frequency** | H = High (every app), M = Medium (most apps), L = Low (specialized) |
| **Reusable?** | Y = Can be normalized into global component, N = Unique per instance |
| **Business-Specific?** | Y = Contains business logic, N = Purely presentational |
| **Template Options** | Comma-separated list of relevant Universal Theme template options |

---

## Regions

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Interactive Report | Region | H | Y | N | CSS, JS, IG Engine, APEX_IR | `.a-IRR` | Show Toolbar, Show Search Bar, Show Actions Menu, Fixed Header, Stretch Report, Pagination (Top/Bottom), Show Row Selector, Alt Row Colors |
| Interactive Grid | Region | H | Y | N | CSS, JS, IG Engine, APEX_IG | `.a-IG` | Show Toolbar, Show Search, Show Column Heading Menu, Fixed Headers, Stretch Report, Pagination Type, Edit Mode (Row/Inline), Show Add Row |
| Dashboard | Region | H | N | Y | Charts, Cards, IG, CSS Grid | `.a-DashboardRegion` | Stretch to Fit, Show Title, Compact |
| Chart | Region | H | Y | N | Oracle JET, Chart Engine, Data Source | `.a-Chart` | Show Toolbar, Stacked, Legend Position, Animation, 3D |
| Calendar | Region | M | Y | N | FullCalendar library, Data Source | `.a-Calendar` | Month/Week/Day/List view, Show Toolbar, Show Week Numbers |
| Map | Region | L | Y | N | Oracle Maps / MapLibre GL, Spatial Data | `.a-MapRegion` | Show Toolbar, Layer Control, Full Screen Toggle |
| Form | Region | H | Y | N | Page Items, Validations, Processes | `.a-FormRegion` | Stretch Form, Compact, Large Labels, Floating Labels, Field Labels Above |
| Modal Dialog | Region | H | Y | N | CSS, JS, Focus Trap, Backdrop | `.a-ModalDialog` | Show Header, Show Footer, Auto Height, Stretch Dialog, Close Button, Resizable |
| Dynamic Action | Region | H | N | N | jQuery (built-in), APEX DA Engine | N/A | Fire on Initialization, Wait for Result |
| List | Region | H | Y | N | Shared Components > Lists, Template | `.a-ListRegion` | Template (Cards, Badge List, Links List, Navigation List, Tabs), Show Icons |
| Tabs | Region | M | Y | N | CSS, JS, List Template | `.a-Tabs` | Pill, Simple, Remember Active Tab |
| Carousel | Region | L | Y | N | CSS, JS, Auto-play Timer | `.a-Carousel` | Auto-play, Indicators, Controls, Crossfade |
| Breadcrumb | Region | H | Y | N | Shared Components > Breadcrumbs | `.a-Breadcrumb` | Vertical, Horizontal, Show Parent Page |
| Tree | Region | M | Y | N | CSS, JS, Hierarchical Data | `.a-Tree` | Expand All, Collapse All, Show Connectors, Collapse on Load |
| Content Row | Region | H | Y | N | CSS, Layout | `.a-ContentRow` | Stretch, Compact |
| Classic Report | Region | H | Y | N | SQL Query, Template, Pagination | `.a-CWReport` | Fixed Headers, Stretch Report, Pagination, Alt Row Colors, Row Highlighting |
| Wizard | Region | M | Y | N | CSS, JS, Process, Multi-step | `.a-Wizard` | Show Step Indicator, Show Progress Bar, Breadcrumb Style |
| Cards | Region | H | Y | N | CSS, Template, SQL Query | `.a-CardsRegion` | Grid/List Layout, Basic/Elevated/Outlined, Icon, Media, Compact |
| Static Content | Region | H | Y | N | None (plain HTML/CSS) | `.a-StaticRegion` | Remove Body Padding, Show Border, Compact |
| Popup Region | Region | L | Y | N | CSS, JS, Position Engine | `.a-PopupRegion` | Position (Above/Below/Left/Right), Arrow, Dismiss on Blur |

---

## Page Items

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Text Field | Page Item | H | Y | N | CSS, Validation | `.a-TextInput` | Compact, Floating Label, Stretch, Pill, Large, Pre/Post Text |
| Textarea | Page Item | H | Y | N | CSS, Validation, Character Count | `.a-TextArea` | Compact, Stretch, Auto Resize, Character Counter, Rich Text |
| Select List | Page Item | H | Y | N | CSS, List of Values, Cascade | `.a-SelectList` | Compact, Stretch, Pill, Show Icon, None Value |
| Shuttle | Page Item | M | Y | N | CSS, JS, List of Values | `.a-Shuttle` | Compact, Show Order Buttons, Show Search |
| Popup LOV | Page Item | H | Y | N | CSS, JS, Modal, List of Values | `.a-PopupLOV` | Compact, Hide Search, Multiple Values, Show Display As |
| Date Picker | Page Item | H | Y | N | Oracle JET Date Picker, CSS | `.a-DatePicker` | Compact, Show Time, Show Today Button, Year Picker, Month Picker |
| Number Field | Page Item | H | Y | N | CSS, Validation | `.a-NumberInput` | Compact, Stretch, Pill, Show Buttons (spinner) |
| Checkbox | Page Item | M | Y | N | CSS, JS | `.a-Checkbox` | Compact, Switch Style, Pill |
| Switch | Page Item | H | Y | N | CSS, JS | `.a-Switch` | Compact, Pill, Label Position (Left/Right) |
| Radio Group | Page Item | M | Y | N | CSS, JS, List of Values | `.a-RadioGroup` | Compact, Pill, Horizontal/Vertical |
| Rich Text Editor | Page Item | L | Y | N | CKEditor or Quill, CSS, JS | `.a-RichTextEditor` | Toolbar Style (Complete/Compact/Basic), Height |
| File Browse | Page Item | M | Y | N | CSS, JS, File System, Validation | `.a-FileBrowse` | Compact, Stretch, Drag and Drop, Multiple |
| Display Only | Page Item | H | Y | N | CSS | `.a-DisplayOnly` | Compact, Show Icon, Format as Link, Format as Text |
| Hidden | Page Item | H | Y | N | None | N/A | N/A |
| Password | Page Item | H | Y | N | CSS, Validation | `.a-Password` | Compact, Stretch, Show/Hide Toggle |
| Color Picker | Page Item | L | Y | N | CSS, JS, Color Engine | `.a-ColorPicker` | Compact, Show As Swatches, Show RGB |
| Slider | Page Item | L | Y | N | CSS, JS, Range | `.a-Slider` | Compact, Show Value, Show Min/Max |
| List Manager | Page Item | L | Y | N | CSS, JS, List of Values | `.a-ListManager` | Compact, Show Order Buttons |

---

## Buttons

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Submit | Button | H | Y | N | CSS, Process, Validation | `.a-Button` | Hot (Primary), Warning, Danger, Success, Large, Compact, Pill, Icon Only, Link Style |
| Redirect to Page (This App) | Button | H | Y | N | CSS, Branch Engine | `.a-Button` | Same as Submit + Target Options |
| Redirect to Page (Other App) | Button | L | Y | N | CSS, Branch Engine, Session | `.a-Button` | Same as Submit + Application Selection |
| Redirect to URL | Button | M | Y | N | CSS, URL Engine | `.a-Button` | Same as Submit + URL Target |
| Defined by Dynamic Action | Button | H | Y | N | CSS, Dynamic Actions | `.a-Button` | Same as Submit |
| Trigger Action (Menu Button) | Button | M | Y | N | CSS, JS, Menu | `.a-Button--withIcon` | Icon, Menu Style, Split Button |
| Confirmation | Button | M | Y | N | CSS, JS, Dynamic Action | `.a-Button` | Same as Submit + Confirm Dialog Options |
| Menu Button | Button | L | Y | N | CSS, JS, Menu, List | `.a-Button--menu` | Menu (Dropdown), Split Button |
| Reset | Button | M | Y | N | CSS, JS, Form Reset | `.a-Button` | Same as Submit |
| Cancel | Button | H | Y | N | CSS, JS, Dynamic Action | `.a-Button` | Same as Submit |
| Delete | Button | H | Y | N | CSS, JS, Confirmation, Process | `.a-Button` | Danger |

---

## Templates & Shared Components

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Base App Structure | Template | H | Y | N | CSS, Page Templates, Navigation | `.a-AppStructure` | Logo, Navigation Position, Side/Nav Collapse State |
| Authentications | Shared Component | H | N | Y | APEX Auth Schemes, Login Page | N/A | LDAP, Custom, Social Sign-In, Open Door |
| Authorizations | Shared Component | H | N | Y | APEX AuthZ Schemes, Roles | N/A | Role-Based, Component-Level, Page-Level |
| LOVs (List of Values) | Shared Component | H | Y | N | SQL, REST, Static Data | N/A | Static, Dynamic (SQL), Cascading |
| Breadcrumbs | Shared Component | H | Y | N | Page Hierarchy, Navigation | N/A | Standard Breadcrumb Template |
| Static Files | Shared Component | H | N | N | File Storage, CSP, MIME Types | N/A | CSS, JS, Images, Fonts, Documents |
| Lists | Shared Component | H | Y | N | Template, SQL, Build Options | N/A | Static, Dynamic, Navigation, Badge |
| Component Settings | Shared Component | H | N | N | Build Options, Substitutions | N/A | Theme Style, Component Defaults |
| Build Options | Shared Component | M | N | N | Conditional Display | N/A | Include/Exclude |
| Data Load Definitions | Shared Component | M | N | Y | REST, SOAP, File Upload | N/A | CSV, XML, JSON, Spreadsheet |
| REST Data Sources | Shared Component | H | N | Y | HTTP, REST, JSON, Auth | N/A | GET, POST, PUT, DELETE, Pagination |
| Web Credentials | Shared Component | H | N | Y | Auth, Secrets, HTTPS | N/A | Basic Auth, OAuth2, API Key, OCI |
| Shortcuts | Shared Component | M | N | N | Substitution Engine | N/A | Text, HTML, PL/SQL, Message |
| Plug-ins | Shared Component | L | N | N | CSS, JS, PL/SQL, Custom Rendering | N/A | Item, Region, Process, Dynamic Action, Authentication |
| Application Items | Shared Component | H | N | Y | Session State | N/A | N/A |
| Application Processes | Shared Component | H | N | Y | AJAX Callback, PL/SQL | N/A | On Demand, By Process Point |
| Application Computations | Shared Component | M | N | Y | Session State, PL/SQL | N/A | On New Instance, On Demand |

---

## Navigation & Layout

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Navigation Menu (Side) | Navigation | H | Y | N | CSS, JS, Lists, Collapse | `.a-Nav` | Collapsed, Expanded, Fixed, Accordion |
| Navigation Menu (Top) | Navigation | H | Y | N | CSS, JS, Lists, Dropdown | `.a-Nav--top` | Fixed, Sticky, Logo, Search Bar |
| Mega Menu | Navigation | L | Y | N | CSS, JS, Lists, Grid | `.a-MegaMenu` | Grid Layout, Icon Menu, Column Count |
| Hamburger Menu | Navigation | H | Y | N | CSS, JS, Breakpoint | `.a-HamburgerMenu` | Slide-Out, Push, Overlay |
| Slide-Out Drawer | Navigation | H | Y | N | CSS, JS, Backdrop | `.a-Drawer` | Left, Right, Width, Overlay |
| Tab Navigation | Navigation | M | Y | N | CSS, JS, Lists | `.a-Tabs` | Pill, Simple, Underline, Scrollable |
| Pagination | Navigation | H | Y | N | CSS, JS, IG/IR Engine | `.a-Pagination` | Show Row Count, Compact, Page Jump |

---

## Other Components

| Component Name | Category | Usage Frequency | Reusable? | Business-Specific? | Dependencies | Universal Theme Class | Template Options |
|---|---|---|---|---|---|---|---|
| Dialog (Modal) | Overlay | H | Y | N | CSS, JS, Focus Trap, Backdrop | `.a-Dialog` | Size (Small/Medium/Large/Full), Header, Footer, Close Button |
| Login Page | Page | H | Y | N | Authentication, CSS, JS | `.a-LoginPage` | Logo, Background, Social Sign-In, Password Reset |
| Badge | Indicator | H | Y | N | CSS, JS, Data Source | `.a-Badge` | Color (Default/Success/Warning/Danger/Info), Pill, Size |
| Badge List | Region | M | Y | N | CSS, Lists, Template | `.a-BadgeList` | Compact, Horizontal/Vertical, Show Icons |
| Alerts / Notifications | Feedback | H | Y | N | CSS, JS, Auto-dismiss, Toast | `.a-Alert` | Success, Warning, Danger, Info, Dismissible |
| Progress Bar | Indicator | M | Y | N | CSS, Data Source | `.a-ProgressBar` | Animated, Striped, Height, Show Percentage |
| Loading Spinner | Indicator | H | Y | N | CSS, JS | `.a-Spinner` | Size (sm/md/lg), Color, Overlay |
| Tooltip | Feedback | M | Y | N | CSS, JS, Positioning | `.a-Tooltip` | Position (Top/Bottom/Left/Right), Delay |
| Menu (Dropdown) | Overlay | H | Y | N | CSS, JS, Positioning, ARIA | `.a-Menu` | Position, Width, Divider, Icon |
| Legend | Indicator | M | Y | N | CSS, Data Source | `.a-Legend` | Horizontal/Vertical, Interactive |

---

## Summary

| Category | Count |
|----------|-------|
| Regions | 20 |
| Page Items | 18 |
| Buttons / Actions | 11 |
| Templates & Shared Components | 16 |
| Navigation & Layout | 7 |
| Overlays & Feedback | 5 |
| Indicators | 4 |
| **Total Identified Components** | **81** |

| Reusability | Count | Percentage |
|-------------|-------|------------|
| Fully Reusable (Y) | 67 | 82.7% |
| Not Reusable (N) or Conditional | 14 | 17.3% |

| Business Logic Embedded | Count |
|------------------------|-------|
| Contains Business Logic (Y) | 16 |
| Purely Presentational (N) | 65 |
