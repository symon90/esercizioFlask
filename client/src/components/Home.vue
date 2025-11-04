<template>
   <!-- <pre>{{ JSON.stringify(msg,null,2) }}</pre>
     -->

     {{ stationJson }}
   <ul>
    <li v-for="station in stationJson" :key="station.id">
        {{ station.name }} - {{ station.address }}
    </li>
   </ul>

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
            axios.get('http://localhost:5000/')
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