# PNG Visualization Generation Guide

## Overview
This project now includes automated PNG generation for the expense tracker dashboard visualizations using Puppeteer for headless browser rendering.

## Generated Files

### 1. `dashboard-full.png`
- **Description**: Full-page screenshot of the entire dashboard
- **Resolution**: 3840 x 2160 pixels (2x scale factor)
- **Use Case**: Complete overview of all dashboard components

### 2. `dashboard-viewport.png`
- **Description**: Above-the-fold view of the dashboard
- **Resolution**: 3840 x 2160 pixels (2x scale factor)
- **Use Case**: Hero/preview image showing the main dashboard interface

## Quick Start

### Generate PNG Visualizations
```bash
npm run generate-png
```

This single command will:
1. Build the React application (`npm run build`)
2. Launch Puppeteer headless browser
3. Render the dashboard at high resolution
4. Capture and save PNG screenshots
5. Output files to the project root

### Manual Generation
If you need more control:
```bash
# Build first
npm run build

# Then generate PNGs
node generate-png.js
```

## Technical Details

### Dependencies
- **puppeteer**: Headless Chrome automation for screenshot capture
- **vite**: Build tool for creating production bundle

### Configuration
The PNG generation script (`generate-png.js`) uses:
- **Viewport**: 1920x1080 pixels
- **Device Scale Factor**: 2x (for retina/high-DPI displays)
- **Output Resolution**: 3840x2160 pixels
- **Format**: PNG (lossless)
- **Wait Time**: 3 seconds for chart rendering

### Customization
Edit `generate-png.js` to customize:
- Viewport dimensions
- Scale factor (for higher/lower resolution)
- Wait times (if charts need more time to render)
- Output filenames
- Additional screenshot regions

## Troubleshooting

### Charts Not Rendering
If charts appear blank, increase the wait time:
```javascript
await new Promise(resolve => setTimeout(resolve, 5000)); // 5 seconds
```

### Low Quality Images
Increase the device scale factor:
```javascript
await page.setViewport({
  width: 1920,
  height: 1080,
  deviceScaleFactor: 3 // Higher quality
});
```

### Memory Issues
If running on limited memory systems, reduce viewport size or scale factor:
```javascript
await page.setViewport({
  width: 1280,
  height: 720,
  deviceScaleFactor: 1
});
```

## File Structure
```
/vercel/sandbox/
├── generate-png.js          # PNG generation script
├── dashboard-full.png       # Generated: Full page screenshot
├── dashboard-viewport.png   # Generated: Viewport screenshot
├── dist/                    # Built application (generated)
└── components/              # React components
    └── Dashboard.tsx        # Main dashboard with charts
```

## Notes
- PNG files are generated at 2x resolution for crisp display on retina screens
- The script automatically waits for Recharts to render before capturing
- All screenshots use the production build for accurate representation
- Generated PNGs are suitable for presentations, documentation, and marketing materials
