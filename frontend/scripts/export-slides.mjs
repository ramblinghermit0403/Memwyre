import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const exportDir = path.join(__dirname, '../slides-export');
if (!fs.existsSync(exportDir)) {
    fs.mkdirSync(exportDir);
}

const slides = [
    { id: 1, name: 'slide_1_omnipresent' },
    { id: 2, name: 'slide_2_chat' },
    { id: 3, name: 'slide_3_timeline' },
    { id: 4, name: 'slide_4_inbox' },
    { id: 5, name: 'slide_5_handoff' }
];

async function exportSlides() {
    console.log('🚀 Starting high-resolution slide export...');
    const browser = await chromium.launch();
    const page = await browser.newPage({
        viewport: { width: 1920, height: 1080 },
        deviceScaleFactor: 2 // High-DPI for crisp text and graphics
    });

    for (const slide of slides) {
        const url = `http://localhost:5173/export-slide/${slide.id}`;
        console.log(`📸 Capturing ${slide.name} from ${url}...`);

        try {
            await page.goto(url, { waitUntil: 'networkidle' });
            
            // Extra wait for any animations to settle
            await page.waitForTimeout(1000);

            const outputPath = path.join(exportDir, `${slide.name}.png`);
            await page.screenshot({
                path: outputPath,
                fullPage: true,
                type: 'png'
            });
            
            console.log(`✅ Saved to: ${outputPath}`);
        } catch (error) {
            console.error(`❌ Failed to capture ${slide.name}:`, error.message);
        }
    }

    await browser.close();
    console.log('\n✨ Export complete! Check the "slides-export" directory.');
}

exportSlides().catch(console.error);
