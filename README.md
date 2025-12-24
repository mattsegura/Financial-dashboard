<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# Run and deploy your AI Studio app

This contains everything you need to run your app locally.

View your app in AI Studio: https://ai.studio/apps/drive/1JHHm-Hqco_j92E8pE88vB9cqyNmJMvKF

## Run Locally

**Prerequisites:**  Node.js


1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`

## Generate PNG Visualizations

To generate high-quality PNG screenshots of the dashboard:

```bash
npm run generate-png
```

This will:
1. Build the application
2. Launch a headless browser
3. Capture multiple PNG screenshots:
   - `dashboard-full.png` - Full page screenshot
   - `dashboard-viewport.png` - Above-the-fold view (1920x1080)
   - `dashboard-charts.png` - Main dashboard view

All images are generated at 2x resolution (deviceScaleFactor: 2) for crisp, high-quality output.
