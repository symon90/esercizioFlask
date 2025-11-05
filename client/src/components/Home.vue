<template>
  <h1 class="text-center">Lista delle stazioni</h1>
<table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">id</th>
      <th scope="col">Nome</th>
      <th scope="col">Indirizzo</th>
      <th scope="col">Sito</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="station in stationJson" :key="station.id">
        <th scope="row">{{ station.grafana_id }}</th>
        <td>{{ station.name }}</td>
        <td>{{ station.address }}</td>
        <td>{{ station.site }}</td>
        <td><a :href="`/station/${station.id}`">Dettagli</a></td>
    </tr>
  </tbody>
</table>
   

</template>
<script>

import axios from 'axios';
export default {
    name: 'Home',
    data() {
        return {
            stationJson: null,
        }
    },
    methods: {
        getJson() {
            axios.get('http://localhost:5000/api/stations')
                .then(response => {
                    this.stationJson= response.data;
                }).catch(error => {
                    console.log(error);
                });
        }
    },
    created() {
        this.getJson();
    }

}
</script>