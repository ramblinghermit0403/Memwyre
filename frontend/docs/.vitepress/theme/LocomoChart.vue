<template>
  <div class="locomo-chart-outer">
    <!-- Corner Brackets for Outer Container -->
    <div class="bracket top-left"></div>
    <div class="bracket top-right"></div>
    <div class="bracket bottom-left"></div>
    <div class="bracket bottom-right"></div>

    <div class="locomo-chart-inner">
      <!-- Gridlines -->
      <div class="chart-gridlines">
        <div class="gridline"></div>
        <div class="gridline"></div>
        <div class="gridline"></div>
        <div class="gridline"></div>
        <div class="gridline"></div>
      </div>

      <!-- Chart Bars Area -->
      <div class="chart-bars-container">
        <!-- Category: Single-hop -->
        <div class="category-group">
          <div class="bars-wrapper">
            <!-- Old Bar -->
            <div class="bar-column">
              <span class="bar-label" :class="{ visible: animated }">53.0</span>
              <div 
                class="bar-fill old-bar" 
                :style="{ height: animated ? '53.0%' : '0%' }"
              ></div>
            </div>
            <!-- New Bar -->
            <div class="bar-column">
              <span class="bar-label new-label" :class="{ visible: animated }">80.0</span>
              <div 
                class="bar-fill new-bar" 
                :style="{ height: animated ? '80.0%' : '0%' }"
              ></div>
            </div>
          </div>
          <div class="category-name">Single-hop</div>
        </div>

        <!-- Category: Multi-hop -->
        <div class="category-group">
          <div class="bars-wrapper">
            <!-- Old Bar -->
            <div class="bar-column">
              <span class="bar-label" :class="{ visible: animated }">24.0</span>
              <div 
                class="bar-fill old-bar" 
                :style="{ height: animated ? '24.0%' : '0%' }"
              ></div>
            </div>
            <!-- New Bar -->
            <div class="bar-column">
              <span class="bar-label new-label" :class="{ visible: animated }">45.0</span>
              <div 
                class="bar-fill new-bar" 
                :style="{ height: animated ? '45.0%' : '0%' }"
              ></div>
            </div>
          </div>
          <div class="category-name">Multi-hop</div>
        </div>

        <!-- Category: Open-domain -->
        <div class="category-group">
          <div class="bars-wrapper">
            <!-- Old Bar -->
            <div class="bar-column">
              <span class="bar-label" :class="{ visible: animated }">50.0</span>
              <div 
                class="bar-fill old-bar" 
                :style="{ height: animated ? '50.0%' : '0%' }"
              ></div>
            </div>
            <!-- New Bar -->
            <div class="bar-column">
              <span class="bar-label new-label" :class="{ visible: animated }">76.0</span>
              <div 
                class="bar-fill new-bar" 
                :style="{ height: animated ? '76.0%' : '0%' }"
              ></div>
            </div>
          </div>
          <div class="category-name">Open-domain</div>
        </div>

        <!-- Category: Temporal -->
        <div class="category-group">
          <div class="bars-wrapper">
            <!-- Old Bar -->
            <div class="bar-column">
              <span class="bar-label" :class="{ visible: animated }">48.0</span>
              <div 
                class="bar-fill old-bar" 
                :style="{ height: animated ? '48.0%' : '0%' }"
              ></div>
            </div>
            <!-- New Bar -->
            <div class="bar-column">
              <span class="bar-label new-label" :class="{ visible: animated }">74.0</span>
              <div 
                class="bar-fill new-bar" 
                :style="{ height: animated ? '74.0%' : '0%' }"
              ></div>
            </div>
          </div>
          <div class="category-name">Temporal</div>
        </div>
      </div>

      <!-- Chart Legend & Footer -->
      <div class="chart-footer">
        <div class="legend-items">
          <div class="legend-item">
            <span class="legend-swatch swatch-old"></span>
            <span class="legend-text">Standard RAG</span>
          </div>
          <div class="legend-item">
            <span class="legend-swatch swatch-new"></span>
            <span class="legend-text new-text">Memwyre</span>
          </div>
        </div>
        <div class="footer-tag">LOCOMO</div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const animated = ref(false)

onMounted(() => {
  // Trigger bar animations shortly after mounting
  setTimeout(() => {
    animated.value = true
  }, 100)
})
</script>

<style scoped>
.locomo-chart-outer {
  position: relative;
  padding: 12px;
  border: 1px dashed var(--vp-c-border);
  border-radius: 6px;
  background-color: var(--vp-c-bg-soft);
  margin: 2rem 0;
  overflow: hidden;
}

.locomo-chart-inner {
  position: relative;
  width: 100%;
  background-color: var(--vp-c-bg);
  border: 1px solid var(--vp-c-border);
  border-radius: 4px;
  padding: 2rem 1.5rem 1.5rem 1.5rem;
  box-sizing: border-box;
}

/* Bracket styling to match landing page crosshairs */
.bracket {
  position: absolute;
  width: 16px;
  height: 16px;
  pointer-events: none;
}
.bracket::before, .bracket::after {
  content: "";
  position: absolute;
  background-color: var(--vp-c-text-3);
  opacity: 0.8;
}
.bracket::before {
  width: 100%;
  height: 1px;
}
.bracket::after {
  width: 1px;
  height: 100%;
}

.top-left {
  top: 4px;
  left: 4px;
}
.top-left::before { top: 8px; left: 0; }
.top-left::after { left: 8px; top: 0; }

.top-right {
  top: 4px;
  right: 4px;
}
.top-right::before { top: 8px; right: 0; }
.top-right::after { right: 8px; top: 0; }

.bottom-left {
  bottom: 4px;
  left: 4px;
}
.bottom-left::before { bottom: 8px; left: 0; }
.bottom-left::after { left: 8px; bottom: 0; }

.bottom-right {
  bottom: 4px;
  right: 4px;
}
.bottom-right::before { bottom: 8px; right: 0; }
.bottom-right::after { right: 8px; bottom: 0; }

/* Gridlines */
.chart-gridlines {
  position: absolute;
  top: 2rem;
  bottom: 4.5rem;
  left: 1.5rem;
  right: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  pointer-events: none;
  z-index: 0;
}
.gridline {
  width: 100%;
  border-top: 1px dashed var(--vp-c-divider);
}

/* Chart Area */
.chart-bars-container {
  position: relative;
  z-index: 1;
  height: 320px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 0.75rem;
}

.category-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  height: 100%;
  justify-content: flex-end;
}

.bars-wrapper {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 0.5rem;
  height: 80%;
  width: 100%;
  border-bottom: 1px solid var(--vp-c-divider);
}

@media (min-width: 640px) {
  .bars-wrapper {
    gap: 1.25rem;
  }
}

.bar-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  height: 100%;
  width: 28px;
  position: relative;
}

@media (min-width: 640px) {
  .bar-column {
    width: 44px;
  }
}

.bar-label {
  font-family: var(--vp-font-family-mono);
  font-size: 10px;
  color: var(--vp-c-text-2);
  margin-bottom: 4px;
  opacity: 0;
  transition: opacity 0.5s ease-in-out 0.5s;
}

@media (min-width: 640px) {
  .bar-label {
    font-size: 11px;
  }
}

.bar-label.visible {
  opacity: 1;
}

.new-label {
  color: #D97757;
  font-weight: 700;
}

.bar-fill {
  width: 100%;
  border: 1px solid var(--vp-c-text-1);
  border-bottom: none;
  border-radius: 3px 3px 0 0;
  transition: height 1s cubic-bezier(0.16, 1, 0.3, 1);
  transform-origin: bottom;
}

.old-bar {
  background-color: var(--vp-c-neutral);
  opacity: 0.75;
  background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, var(--vp-c-divider) 8px, var(--vp-c-divider) 9px);
}

.new-bar {
  background-color: #D97757;
  background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(0, 0, 0, 0.15) 8px, rgba(0, 0, 0, 0.15) 9px);
}

.dark .new-bar {
  background-image: repeating-linear-gradient(45deg, transparent, transparent 8px, rgba(255, 255, 255, 0.15) 8px, rgba(255, 255, 255, 0.15) 9px);
}

.category-name {
  margin-top: 10px;
  font-size: 11px;
  font-weight: 500;
  color: var(--vp-c-text-2);
  text-align: center;
}

@media (min-width: 640px) {
  .category-name {
    font-size: 13px;
  }
}

/* Legend & Footer */
.chart-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1.5rem;
  border-top: 1px solid var(--vp-c-divider);
  padding-top: 1rem;
}

.legend-items {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.legend-swatch {
  width: 12px;
  height: 12px;
  border-radius: 2px;
  border: 1px solid var(--vp-c-text-1);
}

.swatch-old {
  background-color: var(--vp-c-neutral);
  opacity: 0.75;
  background-image: repeating-linear-gradient(45deg, transparent, transparent 3px, var(--vp-c-divider) 3px, var(--vp-c-divider) 4px);
}

.swatch-new {
  background-color: #D97757;
}

.legend-text {
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-text-2);
}

.new-text {
  color: #D97757;
}

.footer-tag {
  font-family: var(--vp-font-family-mono);
  font-size: 11px;
  font-weight: 700;
  color: var(--vp-c-text-3);
  letter-spacing: 0.1em;
}
</style>
