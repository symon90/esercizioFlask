<template>
    <Line :data="chartData" :options="chartOptions" />
</template>
<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

export default {
    name: 'LineChart',
    components: {
        Line
    },
    props: {
        labels: {
            type: Array,
            required: true
        },
        values: {
            type: Array,
            required: true
        }
    },
    computed: {
        chartData() {
            return {
                labels: this.labels || [],
                datasets: [
                    {
                        label: 'Media',
                        backgroundColor: 'rgba(75,192,192,0.2)',
                        borderColor: 'rgba(75,192,192,1)',
                        borderWidth: 1,
                        data: this.values || [],
                        fill: true,
                        tension: 0.2,
                        pointRadius: 2,

                    }
                ]
            }
        }
    },
    data() {
        return {
            chartOptions: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: false,
                        ticks: {
                            callback: function(value) {
                                return value;
                            }
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Media giornaliera'
                    }
                }
            }
        }
    }
}
</script>