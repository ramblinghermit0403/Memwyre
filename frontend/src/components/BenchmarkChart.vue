<template>
  <div class="w-full h-96 bg-gray-900/50 rounded-xl p-4 border border-gray-800">
    <Chart type="bar" :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Chart } from 'vue-chartjs'
import { ref } from 'vue'

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  Title,
  Tooltip,
  Legend
)

const chartData = ref({
  labels: ['A-Mem', 'LangMem', 'RAG (K=2)', 'Zep', 'MemWyRE v1', 'MemWyRE Graph'],
  datasets: [
    {
      type: 'line',
      label: 'P95 Latency (s)',
      borderColor: '#f87171', // Red
      backgroundColor: '#f87171',
      borderWidth: 2,
      data: [35, 82, 25, 27, 8, 4.34],
      yAxisID: 'y1',
      tension: 0.3
    },
    {
      type: 'line',
      label: 'P50 Latency (s)',
      borderColor: '#4ade80', // Green
      backgroundColor: '#4ade80',
      borderWidth: 2,
      data: [15, 68, 14, 21, 5, 1.98],
      yAxisID: 'y1',
      tension: 0.3
    },
    {
      type: 'bar',
      label: 'LLM-Judge Accuracy (%)',
      backgroundColor: '#3b82f6', // Blue
      data: [48.4, 58.1, 61.0, 66.0, 66.9, 64.0],
      yAxisID: 'y',
      barPercentage: 0.6
    }
  ]
})

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: false,
  interaction: {
    mode: 'index',
    intersect: false,
  },
  plugins: {
    legend: {
      labels: {
        color: '#cbd5e1'
      }
    }
  },
  scales: {
    x: {
      grid: {
        color: '#1e293b'
      },
      ticks: {
        color: '#94a3b8'
      }
    },
    y: {
      type: 'linear',
      display: true,
      position: 'left',
      min: 0,
      max: 80,
      grid: {
        color: '#1e293b'
      },
      ticks: {
        color: '#94a3b8'
      },
      title: {
        display: true,
        text: 'Accuracy (%)',
        color: '#3b82f6'
      }
    },
    y1: {
      type: 'linear',
      display: true,
      position: 'right',
      min: 0,
      max: 100,
      grid: {
        drawOnChartArea: false // only want the grid lines for one axis to show up
      },
      ticks: {
        color: '#f87171'
      },
      title: {
        display: true,
        text: 'Latency (s)',
        color: '#f87171'
      }
    }
  }
})
</script>
