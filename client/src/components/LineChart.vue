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
        },
        min:{
            type:Array,
            required:false
        },
        max:{
            type:Array,
            required:false
        },
        weighted_average:{
            type:Number,
            required:false
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

                    },
                    {
                        label: 'Minimo',
                        backgroundColor: 'rgba(153,102,255,0.2)',
                        borderColor: 'rgba(153,102,255,1)',
                        borderWidth: 1,
                        data: this.min || [],
                        fill: false,
                        tension: 0.2,
                        pointRadius: 2,
                    },
                    {
                        label: 'Massimo',
                        backgroundColor: 'rgba(255,159,64,0.2)',
                        borderColor: 'rgba(255,159,64,1)',
                        borderWidth: 1,
                        data: this.max || [],
                        fill: false,
                        tension: 0.2,
                        pointRadius: 2,
                    },
                    {
                        label: 'Media ponderata',
                        backgroundColor: 'rgba(255,99,132,0.2)',
                        borderColor: 'rgba(255,99,132,1)',
                        borderWidth: 1,
                        data: Array(this.labels.length).fill(this.weighted_average) || [],
                        fill: false,
                        
                        tension: 0.2,
                        pointRadius: 0,
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