<template>
    <!--div class="q-pa-md row items-start q-gutter-md"-->
        <div class="q-pa-md row q-col-gutter-md">
           <div class="col-6">
                <!-- 1.card -->
                <Chart/>       
           </div> 

           <div class="col-6">
                <!-- 2.card -->
                <Clock/>
           </div>
        </div>

        <div class="q-pa-md row q-col-gutter-md">
           <div class="col-6">
                <!-- 3.card -->
                <q-card dark bordered class="bg-grey-9 my-card">
                  <q-card-section>
                    <div class="text-h6">Sai Kah</div>
                    <div class="text-subtitle2">by John Doe</div>
                  </q-card-section>

                  <q-separator dark inset />

                  <q-card-section>
                    {{ value }}
                  </q-card-section>
                </q-card>
           </div> 

           <div class="col-6">
                <!-- 4.card -->
                <Toggle/>
           </div>
        </div>
        
    <!--/div-->

</template>

<script lang="ts">
import Chart from 'src/components/Chart.vue';
import Clock from 'src/components/Clock.vue';
import Toggle from 'src/components/Toggle.vue';
import { defineComponent, ref } from 'vue';

    export default defineComponent({
        name: "HomePage",
        components: {
            Chart, Clock, Toggle
        },
        data() {
            const tmp = 50;
            const value = false;
            
            return {value, tmp};
        }
    })
</script>