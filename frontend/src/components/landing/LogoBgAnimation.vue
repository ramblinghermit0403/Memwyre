<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import logoUrl from '/image.svg';

const props = defineProps({
  opacity: {
    type: Number,
    default: 0.8
  },
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

// Configuration
const fontSize = 8;
const updateRate = 0.05;

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
    maskCtx.clearRect(0, 0, cols, rows);
    
    if (maskImage.complete && maskImage.naturalWidth > 0) {
      const baseW = cols * 0.14;
      const aspect = maskImage.naturalHeight / maskImage.naturalWidth;
      
      // Top row corners
      maskCtx.drawImage(maskImage, cols * 0.02, rows * 0.05, baseW * 0.8, baseW * 0.8 * aspect);
      maskCtx.drawImage(maskImage, cols * 0.85, rows * 0.05, baseW * 0.9, baseW * 0.9 * aspect);
      
      // Mid-section framing
      maskCtx.drawImage(maskImage, -cols * 0.05, rows * 0.35, baseW * 0.9, baseW * 0.9 * aspect);
      maskCtx.drawImage(maskImage, cols * 0.92, rows * 0.4, baseW * 0.85, baseW * 0.85 * aspect);
      maskCtx.drawImage(maskImage, cols * 0.15, rows * 0.2, baseW * 0.7, baseW * 0.7 * aspect);
      maskCtx.drawImage(maskImage, cols * 0.7, rows * 0.22, baseW * 0.75, baseW * 0.75 * aspect);
      
      // Lower mid framing (still safe from footer)
      maskCtx.drawImage(maskImage, cols * 0.1, rows * 0.5, baseW * 0.8, baseW * 0.8 * aspect);
      maskCtx.drawImage(maskImage, cols * 0.75, rows * 0.52, baseW * 0.85, baseW * 0.85 * aspect);
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
        const a = imgData[idx + 3];
        
        const luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
        const alpha = a / 255;
        
        let brightness = alpha * luminance;
        
        let targetOpacity = Math.min(1.0, brightness * 5.0);
        let isLogo = targetOpacity > 0.15;
        
        // Base opacity for "empty spaces" (slightly darker light gray)
        if (!isLogo) {
          targetOpacity = 0.12;
        }
        
        row.push({
          char: Math.floor(Math.random() * 10).toString(),
          opacity: targetOpacity,
          isLogo: isLogo,
          revealDelay: Math.random() * 1500
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

  const draw = () => {
    ctx.clearRect(0, 0, width, height);
    
    if (!startTime.value) {
      animationFrameId = requestAnimationFrame(draw);
      return;
    }
    
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
        if (elapsed < cell.revealDelay) continue;

        if (Math.random() < updateRate) {
          cell.char = Math.floor(Math.random() * 10).toString();
        }

        const inGlitchRect = isGlitchRow && x >= glitchRect.x && x < glitchRect.x + glitchRect.w;
        let drawX = x * fontSize + fontSize / 2 + rowGlitchX;
        let drawY = y * fontSize + fontSize / 2;

        if (inGlitchRect && Math.random() < 0.1) {
          ctx.fillStyle = Math.random() > 0.5 ? '#00FFFF' : '#FF00FF';
          drawX += (Math.random() * 10 - 5);
        } else {
          ctx.fillStyle = props.invert ? `rgba(0,0,0,${cell.opacity})` : `rgba(255,255,255,${cell.opacity})`;
        }
        
        ctx.fillText(cell.char, drawX, drawY);
      }
    }
    animationFrameId = requestAnimationFrame(draw);
  };

  maskImage.onload = () => {
    initGrid();
  };
  maskImage.src = logoUrl;

  resizeObserver = new ResizeObserver(() => {
    if (maskImage.complete) initGrid();
  });
  resizeObserver.observe(canvas.parentElement);
  
  animationFrameId = requestAnimationFrame(draw);
});

onMounted(() => {
  observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting && !startTime.value) {
      startTime.value = Date.now();
      isVisible.value = true;
    }
  }, { threshold: 0.1 });
  
  if (canvasRef.value) {
    observer.observe(canvasRef.value);
  }
});

onUnmounted(() => {
  if (animationFrameId) cancelAnimationFrame(animationFrameId);
  if (resizeObserver) resizeObserver.disconnect();
  if (observer) observer.disconnect();
});
</script>

<template>
  <canvas ref="canvasRef" class="w-full h-full pointer-events-none" :style="{ opacity: props.opacity }"></canvas>
</template>

<style scoped>
canvas {
  /* Removed radial gradient that was causing big circles */
}
</style>
