import sharp from 'sharp';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const inputSvg = path.join(__dirname, '../public/image.svg');
const outputApple = path.join(__dirname, '../public/apple-touch-icon.png');
const outputFavicon = path.join(__dirname, '../public/favicon-192.png');

async function convertIcons() {
  try {
    // Apple Touch Icon (180x180) - usually needs a solid background. Let's make it white.
    await sharp(inputSvg)
      .resize(180, 180)
      .flatten({ background: { r: 255, g: 255, b: 255 } })
      .png()
      .toFile(outputApple);
    console.log('Successfully created apple-touch-icon.png');

    // Favicon (192x192) - transparent is fine
    await sharp(inputSvg)
      .resize(192, 192)
      .png()
      .toFile(outputFavicon);
    console.log('Successfully created favicon-192.png');

  } catch (err) {
    console.error('Error converting icons:', err);
  }
}

convertIcons();
