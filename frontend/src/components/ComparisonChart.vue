<template>
  <div class="w-full h-64 bg-gray-900/50 rounded-xl p-4 border border-gray-800">
    <Bar :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'
import { ref } from 'vue'

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

const chartData = ref({
  labels: ['MemWyRE', 'OpenAI Memory'],
  datasets: [
    {
      label: 'Recall Accuracy (%)',
      backgroundColor: ['#8b5cf6', '#1e1b4b'], // Violet vs Dark Blue
      borderRadius: 4,
      data: [64.0, 51.57],
      barThickness: 40
    }
  ]
})

const chartOptions = ref({
  indexAxis: 'y', // Horizontal Bar
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: (context) => `${context.raw}%`
      }
    }
  },
  scales: {
    x: {
      grid: {
        color: '#374151',
        drawBorder: false
      },
      ticks: {
        color: '#9ca3af'
      },
      max: 80
    },
    y: {
      grid: {
        display: false
      },
      ticks: {
        color: '#ffffff',
        font: {
          size: 14,
          weight: 'bold'
        }
      }
    }
  }
})
</script>
