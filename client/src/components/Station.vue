<template>
    <div class="container-fluid" v-if="stationDetails">
        <section class="row">
            <div class="col-6">
                <h1 class="text-center">Dettagli stazione</h1>
                <a href="/" class="btn btn-primary">Ritorna alla home</a>

                <h2>Nome: {{ stationDetails.name }}</h2>
                <address>Indirizzo: {{ stationDetails.address }}</address>
                <p>Sito: {{ stationDetails.site }}</p>
                <p>Id Grafana: {{ stationDetails.grafana_id }}</p>
            </div>
            <div class="col-12">
                <div v-for="metric in stationDetails.metrics" :key="data_points">


                    <h3>Misurazione: {{ metric.name }}</h3>
                    <p v-if="metric.description" class="fw-bold">
                        Descrizione:
                        <span v-html="metric.description"></span>
                    </p>
                    <p v-if="metric.unit_of_measurement" class="fw-bold">Unità di misura: <span>
                            {{ metric.unit_of_measurement }}
                        </span></p>
                    <p v-if="metric.limit" class="fw-bold">Limite: <span>
                            {{ metric.limit }}
                        </span></p>
                    <p v-if="metric.limit_unit_of_measurement" class="fw-bold">Unità di misura del limite: <span>
                            {{ metric.limit_unit_of_measurement }}
                        </span></p>
                    <p v-if="metric.molar_mass" class="fw-bold">Massa molare: <span>
                            {{ metric.molar_mass }}
                        </span></p>
                    <p v-if="metric.type" class="fw-bold">Tipologia: <span>
                            {{ metric.type }}
                        </span></p>
                    <p v.if="metric.weighted_average" class="fw-bold">Media ponderata: <span>{{ metric.weighted_average
                    }}</span>
                    </p>
                    <p v-if="metric.n_zero_sample_size" class="fw-bold">Giorni senza misurazioni:
                        {{ metric.n_zero_sample_size }}</p>
                    <section class="row">
                        <div class="col-8">
                            <table class="table table-dark">
                                <thead>
                                    <tr>
                                        <th scope="col">Data</th>
                                        <th scope="col">Min</th>
                                        <th scope="col">Max</th>
                                        <th scope="col">Media</th>
                                        <th scope="col">Numero campioni</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="value in metric.data_points">
                                        <td>{{ value.date }}</td>
                                        <td>{{ value.min }}</td>
                                        <td>{{ value.max }}</td>
                                        <td>{{ value.average }}</td>
                                        <td>{{ value.sample_size }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <div class="col-4" v-if="metric.data_points && metric.data_points.length">
                            
                            <LineChart :labels="metric.data_points.map(dp => dp.date)"
                                :values="metric.data_points.map(dp => dp.average)" />

                        </div>
                    </section>
                </div>
            </div>
        </section>

        <a href="/" class="btn btn-primary">Ritorna alla home</a>
    </div>
</template>
<script>
import axios from 'axios';
import LineChart from './LineChart.vue';
export default {
    name: 'Station',
    components: {
        LineChart
    },
    data() {
        return {
            stationDetails: null,
        }
    },
    methods: {
        getStationDetails() {
            const stationId = this.$route.params.id;
            axios.get(`http://localhost:5000/station/${stationId}`)
                .then(response => {
                    this.stationDetails = response.data;
                }).catch(error => {
                    console.log(error);
                });
        }
    },
    created() {
        this.getStationDetails();
    }
}
</script>