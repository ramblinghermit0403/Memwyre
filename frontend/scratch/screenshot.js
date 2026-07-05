import { chromium } from 'playwright';

async function run() {
  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 360, height: 640 }, // 16:9 phone resolution
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
  });

  console.log('Navigating to http://localhost:5174/ ...');
  await page.goto('http://localhost:5174/');
  await page.waitForTimeout(2000); // Let animations run a bit

  const screenshotPath = 'C:\\Users\\himan\\.gemini\\antigravity\\brain\\bca7efe1-debd-4ca4-b6ad-163b68ddd686\\mobile_portrait_after.png';
  console.log('Taking screenshot and saving to:', screenshotPath);
  await page.screenshot({ path: screenshotPath, fullPage: true });

  await browser.close();
  console.log('Done!');
}

run().catch(console.error);
