<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import maskUrl from '@/assets/pixel_starry_night.png';

const canvasRef = ref(null);
const startTime = ref(null);
let animationFrameId;

// Configuration
const fontSize = 7; 
const updateRate = 0.03;

onMounted(() => {
  const canvas = canvasRef.value;
  if (!canvas) return;
  const ctx = canvas.getContext('2d', { alpha: true });
  
  let width, height;
  let cols, rows;
  let grid = []; 
  
  const maskCanvas = document.createElement('canvas');
  const maskCtx = maskCanvas.getContext('2d', { willReadFrequently: true });
  const maskImage = new Image();
  
  const initGrid = () => {
    width = canvas.parentElement.clientWidth;
    height = canvas.parentElement.clientHeight;
    
    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    
    cols = Math.ceil(width / fontSize);
    rows = Math.ceil(height / fontSize);
    
    maskCanvas.width = cols;
    maskCanvas.height = rows;
    
    if (maskImage.complete && maskImage.naturalWidth > 0) {
      maskCtx.drawImage(maskImage, 0, 0, cols, rows);
    }
    
    const imgData = maskCtx.getImageData(0, 0, cols, rows).data;
    grid = [];
    for (let y = 0; y < rows; y++) {
      const row = [];
      for (let x = 0; x < cols; x++) {
        const idx = (y * cols + x) * 4;
        const brightness = (0.299 * imgData[idx] + 0.587 * imgData[idx+1] + 0.114 * imgData[idx+2]) / 255;
        
        // Ensure even "empty" spaces have very faint numbers (0.04 min)
        let opacity = brightness > 0.4 ? 0.4 : 0.15;
        if (brightness < 0.1) opacity = 0.04;

        row.push({
          char: Math.floor(Math.random() * 10).toString(),
          opacity: opacity,
          revealDelay: Math.random() * 1000
        });
      }
      grid.push(row);
    }
    ctx.font = `900 ${fontSize}px "Courier New", Courier, monospace`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
  };

  const draw = () => {
    ctx.clearRect(0, 0, width, height);
    if (!startTime.value) startTime.value = Date.now();
    const elapsed = Date.now() - startTime.value;

    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        const cell = grid[y][x];
        if (cell.opacity === 0) continue;
        if (elapsed < cell.revealDelay) continue;

        if (Math.random() < updateRate) {
          cell.char = Math.floor(Math.random() * 10).toString();
        }
        
        // Deep purple (81, 45, 168) for higher contrast
        ctx.fillStyle = `rgba(81, 45, 168, ${cell.opacity})`; 
        ctx.fillText(cell.char, x * fontSize + fontSize/2, y * fontSize + fontSize/2);
      }
    }
    animationFrameId = requestAnimationFrame(draw);
  };

  maskImage.onload = () => initGrid();
  maskImage.src = maskUrl;

  const ro = new ResizeObserver(() => { if (maskImage.complete) initGrid(); });
  ro.observe(canvas.parentElement);
  
  animationFrameId = requestAnimationFrame(draw);
  onUnmounted(() => {
    cancelAnimationFrame(animationFrameId);
    ro.disconnect();
  });
});
</script>

<template>
  <div class="absolute inset-0 bg-[#E1D5F5]/30">
    <canvas ref="canvasRef" class="w-full h-full pointer-events-none opacity-60"></canvas>
  </div>
</template>
