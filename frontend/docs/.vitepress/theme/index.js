import DefaultTheme from 'vitepress/theme'
import './custom.css'
import { h } from 'vue'
import SubNavBar from './SubNavBar.vue'
import LocomoChart from './LocomoChart.vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'nav-bar-content-after': () => h(SubNavBar)
    })
  },
  enhanceApp({ app }) {
    app.component('LocomoChart', LocomoChart)
  }
}
