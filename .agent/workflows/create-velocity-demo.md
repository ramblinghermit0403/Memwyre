# Programmatic Velocity Edit Demos

Use this workflow when the user requests to turn reference images or ideas into programmatic, looping HTML/Tailwind videos featuring high-fidelity "velocity edit" style camera movements (aggressive snap-zooms, dynamic panning, and bouncy transitions).

## Phase 1: Reconstruct the UI
1. Closely analyze the reference screenshot provided by the user.
2. Build a static Tailwind CSS replica of the UI components within a Vue component.
3. Ensure absolute precision on paddings, widths, border radii, colors, and shadows.

## Phase 2: Setup the Camera Rig
1. Wrap the reconstructed UI inside an absolute container acting as the "Camera Rig". 
2. Add a `focusCamera` helper and Vue refs to dynamically control x, y, scale, and CSS layout timings.

```vue
<template>
  <!-- Outer clipping viewport -->
  <div class="relative overflow-hidden w-full h-[500px]">
    
    <!-- Virtual Camera Rig (Controls panning and zooming via CSS transform) -->
    <div class="absolute inset-0 z-10 flex flex-col origin-center ease-[cubic-bezier(0.25,1,0.35,1)]"
         :style="{ transform: `translate(${camX}px, ${camY}px) scale(${camScale})`, transitionDuration: camDuration + 'ms' }">
      
      <!-- YOUR COMPONENT UI GOES HERE -->
      
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const camX = ref(0);
const camY = ref(0);
const camScale = ref(1);
const camDuration = ref(1000);

// Helper function to animate the camera viewport
const focusCamera = (x, y, scale = 1, duration = 1000) => {
  camX.value = -x;
  camY.value = -y;
  camScale.value = scale;
  camDuration.value = duration;
};
</script>
```

## Phase 3: Setup the Animation Loop State Machine
1. Create an async `sleep()` utility function.
2. Create an `async function loop()` that cycles through phases (e.g. init, typing, click, toast).
3. Hook `loop()` to an `IntersectionObserver` so it only triggers when the user scrolls to it, to preserve browser performance.

```javascript
let alive = false;
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function loop() {
  while (alive) {
    // Phase 1: Aggressive Punch-in 
    focusCamera(100, 50, 1.8, 400); // Sharp zoom to coordinates
    await sleep(400);

    // Phase 2: Simulate interactions like typing or mouse moving
    let text = "Hello world";
    for (let i = 0; i < text.length; i++) {
        if (!alive) return;
        typedMsg.value += text[i];
        
        // PRO TIP: Dynamically step the camera progression inside the loop to avoid desync
        let progress = (i+1) / text.length;
        focusCamera(100 + (progress * 50), 50, 1.8, 3); // 3ms snap steps 
        
        await sleep(15); // Fast, legible typing
    }
    
    // Phase 3: Instant reset (Velocity pull-back)
    focusCamera(0, 0, 1.0, 250); 
    await sleep(3000);
  }
}
```

## Phase 4: Velocity Styling 
1. **Camera Transitions**: Ensure the Camera Rig `div` uses sharp, aggressive bezier curves: `ease-[cubic-bezier(0.25,1,0.35,1)]`.
2. **Snappy Bounces**: Use bouncy "pop" keyframes for any toasts, badges, or chat bubbles appearing in the UI.

```css
@keyframes bouncePop {
  0% { opacity: 0; transform: translateY(20px) scale(0.8); }
  60% { opacity: 1; transform: translateY(-5px) scale(1.05); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

.animate-fadeIn { 
  animation: bouncePop .5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards; 
}
```

## Core Velocity Principles For The AI
- **No drifting**: Never use linear, slow, uncalibrated pans. Movements should punch-in (`1.8x` to `2.1x`) rapidly, and pull-out instantly to `1.0x`.
- **Typing Lock**: When tracking typing, calculate the X/Y natively based on loop iteration so the camera frame mathematically tracks the expanding text bounds step-by-step.
- **Aggressive Timeframes**: Fast actions are fast. Use 10ms-25ms timing delays for typing sequences. Use 100ms-300ms for sharp drop-zooms and camera repositions.
