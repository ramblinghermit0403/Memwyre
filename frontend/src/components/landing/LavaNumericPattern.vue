<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const canvasRef = ref(null);
const startTime = ref(null);
let animationFrameId;

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

  const initGrid = () => {
    width = canvas.parentElement.clientWidth;
    height = canvas.parentElement.clientHeight;
    
    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    
    cols = Math.ceil(width / fontSize);
    rows = Math.ceil(height / fontSize);
    
    grid = [];
    for (let y = 0; y < rows; y++) {
      const row = [];
      for (let x = 0; x < cols; x++) {
        row.push({
          char: Math.floor(Math.random() * 10).toString(),
        });
      }
      grid.push(row);
    }
    ctx.font = `900 ${fontSize}px "Courier New", Courier, monospace`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
  };

  // Static noise-like function
  const getLavaValue = (x, y) => {
    const t = 100; // Fixed time for a static snapshot
    let val = Math.sin(x * 0.05 + t) * Math.cos(y * 0.05 - t);
    val += Math.sin(x * 0.02 - t * 0.5) * Math.sin(y * 0.03 + t * 0.7);
    val += Math.cos((x + y) * 0.01 + t);
    return val;
  };

  const draw = () => {
    ctx.clearRect(0, 0, width, height);
    
    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        const cell = grid[y][x];
        
        // Use a static value for the lava pattern
        const lava = getLavaValue(x, y);
        
        // Thresholding for the organic "lava lamp" shapes in dark mode
        if (lava > 0.3) {
          ctx.fillStyle = '#FFFFFF'; // White
          ctx.globalAlpha = 0.15;
        } else {
          ctx.fillStyle = '#FFFFFF'; // Light Gray
          ctx.globalAlpha = 0.05;
        }
        
        ctx.fillText(cell.char, x * fontSize + fontSize/2, y * fontSize + fontSize/2);
      }
    }
  };

  initGrid();
  const ro = new ResizeObserver(() => {
    initGrid();
    draw();
  });
  ro.observe(canvas.parentElement);
  
  draw();
  onUnmounted(() => {
    ro.disconnect();
  });
});
</script>

<template>
  <div class="absolute inset-0 bg-transparent">
    <canvas ref="canvasRef" class="w-full h-full pointer-events-none"></canvas>
  </div>
</template>
