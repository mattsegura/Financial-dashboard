import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { existsSync } from 'fs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function generateDashboardPNG() {
  console.log('🚀 Starting PNG generation...');
  
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu'
    ]
  });

  try {
    const page = await browser.newPage();
    
    // Set viewport to a large desktop size for high-quality screenshots
    await page.setViewport({
      width: 1920,
      height: 1080,
      deviceScaleFactor: 2 // 2x resolution for crisp images
    });

    // Check if dist folder exists
    const distPath = join(__dirname, 'dist', 'index.html');
    if (!existsSync(distPath)) {
      throw new Error('Build not found. Please run "npm run build" first.');
    }

    console.log('📂 Loading built application...');
    await page.goto(`file://${distPath}`, {
      waitUntil: 'networkidle0',
      timeout: 30000
    });

    // Wait for charts to render
    console.log('⏳ Waiting for charts to render...');
    await new Promise(resolve => setTimeout(resolve, 3000));

    // Take full dashboard screenshot
    console.log('📸 Capturing full dashboard...');
    await page.screenshot({
      path: join(__dirname, 'dashboard-full.png'),
      fullPage: true,
      type: 'png'
    });
    console.log('✅ Saved: dashboard-full.png');

    // Capture specific sections with better viewport
    await page.setViewport({
      width: 1920,
      height: 3000,
      deviceScaleFactor: 2
    });

    // Wait a bit more for any animations
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Take a viewport screenshot (above the fold)
    await page.setViewport({
      width: 1920,
      height: 1080,
      deviceScaleFactor: 2
    });
    
    await page.screenshot({
      path: join(__dirname, 'dashboard-viewport.png'),
      type: 'png'
    });
    console.log('✅ Saved: dashboard-viewport.png');

    // Try to capture individual chart sections if possible
    try {
      // Wait for recharts to be present
      const hasCharts = await page.evaluate(() => {
        return document.querySelector('.recharts-wrapper') !== null;
      });

      if (hasCharts) {
        console.log('📊 Charts detected, capturing high-resolution version...');
        
        // Scroll to ensure all content is loaded
        await page.evaluate(() => window.scrollTo(0, 0));
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Take another screenshot focused on the main content
        await page.screenshot({
          path: join(__dirname, 'dashboard-charts.png'),
          fullPage: false,
          type: 'png',
          clip: {
            x: 0,
            y: 0,
            width: 1920,
            height: 1080
          }
        });
        console.log('✅ Saved: dashboard-charts.png');
      }
    } catch (err) {
      console.log('⚠️  Could not capture individual charts:', err.message);
    }

    console.log('\n🎉 PNG generation complete!');
    console.log('📁 Generated files:');
    console.log('   - dashboard-full.png (full page)');
    console.log('   - dashboard-viewport.png (above the fold)');
    console.log('   - dashboard-charts.png (main view)');

  } catch (error) {
    console.error('❌ Error generating PNG:', error);
    throw error;
  } finally {
    await browser.close();
  }
}

// Run the generator
generateDashboardPNG().catch(console.error);
