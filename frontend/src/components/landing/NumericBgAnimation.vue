<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import maskUrl from '@/assets/pixel_starry_night.png';

const props = defineProps({
  invert: {
    type: Boolean,
    default: false
  }
});

const canvasRef = ref(null);
const isVisible = ref(false);
const startTime = ref(null);
let animationFrameId;
let resizeObserver;
let observer;
let startAnimation = () => {};
let stopAnimation = () => {};

// Configuration
const fontSize = 10;
const updateRate = 0.02;
const frameInterval = 1000 / 24;

onMounted(() => {
  const canvas = canvasRef.value;
  if (!canvas) return;
  const ctx = canvas.getContext('2d', { alpha: true });
  
  let width, height;
  let cols, rows;
  let grid = []; // 2D array of { char, isMap }
  
  // Offscreen canvas for masking
  const maskCanvas = document.createElement('canvas');
  const maskCtx = maskCanvas.getContext('2d', { willReadFrequently: true });
  
  const maskImage = new Image();
  maskImage.crossOrigin = "Anonymous";
  
  const initGrid = () => {
    width = canvas.parentElement.clientWidth;
    height = canvas.parentElement.clientHeight;
    
    // Support high DPI displays
    const dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    
    cols = Math.ceil(width / fontSize);
    rows = Math.ceil(height / fontSize);
    
    // Prepare mask image
    maskCanvas.width = cols;
    maskCanvas.height = rows;
    
    // Clear mask
    maskCtx.clearRect(0, 0, cols, rows);
    
    if (maskImage.complete && maskImage.naturalWidth > 0) {
      const imgAspect = maskImage.naturalWidth / maskImage.naturalHeight;
      const canvasAspect = cols / rows;
      
      let drawW, drawH, drawX, drawY;
      
      if (canvasAspect > imgAspect) {
        drawW = cols;
        drawH = drawW / imgAspect;
      } else {
        drawH = rows;
        drawW = drawH * imgAspect;
      }
      
      drawX = (cols - drawW) / 2;
      drawY = (rows - drawH) / 2;
      
      maskCtx.drawImage(maskImage, drawX, drawY, drawW, drawH);
    }
    
    const imgData = maskCtx.getImageData(0, 0, cols, rows).data;
    
    grid = [];
    for (let y = 0; y < rows; y++) {
      const row = [];
      for (let x = 0; x < cols; x++) {
        const idx = (y * cols + x) * 4;
        const r = imgData[idx];
        const g = imgData[idx + 1];
        const b = imgData[idx + 2];
        
        const brightness = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
        
        let targetOpacity = Math.min(1.0, brightness * 5.0);
        if (targetOpacity < 0.20) {
          targetOpacity = 0;
        }
        
        row.push({
          char: Math.floor(Math.random() * 10).toString(),
          opacity: targetOpacity,
          revealDelay: Math.random() * 2000
        });
      }
      grid.push(row);
    }
    
    ctx.font = `900 ${fontSize}px "Courier New", Courier, monospace`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
  };

  let glitchFramesRemaining = 0;
  let glitchRect = { x: 0, y: 0, w: 0, h: 0 };
  let lastFrame = 0;

  const draw = (timestamp = 0) => {
    if (!isVisible.value) return;
    animationFrameId = requestAnimationFrame(draw);
    if (timestamp - lastFrame < frameInterval) return;
    lastFrame = timestamp;

    ctx.clearRect(0, 0, width, height);
    
    if (!startTime.value) startTime.value = Date.now();
    
    const elapsed = Date.now() - startTime.value;

    if (glitchFramesRemaining > 0) {
      glitchFramesRemaining--;
    } else if (Math.random() < 0.03) {
      glitchFramesRemaining = Math.floor(Math.random() * 5) + 2;
      glitchRect = {
        x: Math.floor(Math.random() * cols),
        y: Math.floor(Math.random() * rows),
        w: Math.floor(Math.random() * 40) + 10,
        h: Math.floor(Math.random() * 20) + 5
      };
    }
    
    for (let y = 0; y < rows; y++) {
      const isGlitchRow = glitchFramesRemaining > 0 && y >= glitchRect.y && y < glitchRect.y + glitchRect.h;
      const rowGlitchX = isGlitchRow && Math.random() < 0.3 ? (Math.random() * 40 - 20) : 0;
      
      for (let x = 0; x < cols; x++) {
        const cell = grid[y][x];
        
        if (cell.opacity === 0) continue;
        if (elapsed < cell.revealDelay) continue;

        if (Math.random() < updateRate) {
          cell.char = Math.floor(Math.random() * 10).toString();
        }
        
        const inGlitchRect = isGlitchRow && x >= glitchRect.x && x < glitchRect.x + glitchRect.w;
        let drawX = x * fontSize + fontSize / 2 + rowGlitchX;
        let drawY = y * fontSize + fontSize / 2;
        
        if (inGlitchRect && Math.random() < 0.1) {
          ctx.fillStyle = Math.random() > 0.5 ? `#00FFFF` : `#FF00FF`;
          drawX += (Math.random() * 10 - 5);
        } else {
          ctx.fillStyle = props.invert ? '#000000' : '#FFFFFF';
        }
        
        ctx.fillText(cell.char, drawX, drawY);
      }
    }
  };

  startAnimation = () => {
    if (animationFrameId) return;
    if (!startTime.value) startTime.value = Date.now();
    isVisible.value = true;
    animationFrameId = requestAnimationFrame(draw);
  };

  stopAnimation = () => {
    isVisible.value = false;
    if (animationFrameId) {
      cancelAnimationFrame(animationFrameId);
      animationFrameId = null;
    }
  };

  maskImage.onload = () => {
    initGrid();
  };
  maskImage.src = maskUrl;

  resizeObserver = new ResizeObserver(() => {
    if (maskImage.complete) {
      initGrid();
    }
  });
  resizeObserver.observe(canvas.parentElement);
});

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      startAnimation();
    } else {
      stopAnimation();
    }
  }, { threshold: 0.1 });
  
  if (canvasRef.value) {
    observer.observe(canvasRef.value);
  }
});

onUnmounted(() => {
  stopAnimation();
  if (resizeObserver) resizeObserver.disconnect();
  if (observer) observer.disconnect();
});
</script>

<template>
  <canvas ref="canvasRef" class="w-full h-full pointer-events-none"></canvas>
</template>

<style scoped>
canvas {
  mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, black 60%, transparent 100%);
}
</style>
