<template>
    <q-card
      dark bordered class="bg-grey-9 my-card text-white"
    >
      <q-card-section>
        <div class="text-h6">Clock</div>
      
        <div class="q-pa-md">
            <div class="q-gutter-md">
              <q-time
                v-model="time"
                format24h
                landscape
                color="yellow"
                text-color="black"
                dark
                bordered
              />
            </div>
        </div>
        <div class="q-pa-md" style="max-width: 300px">
            <q-input filled v-model="date" dark>
              <template v-slot:prepend>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                    <q-date v-model="date" mask="YYYY-MM-DD">
                      <div class="row items-center justify-end">
                        <q-btn v-close-popup label="Close" color="primary" flat />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
        </div>
      </q-card-section>
      <div class="q-pa-md">
        <q-btn 
            color="primary" 
            label="Update System Time" 
            @click="putDateAndTime" 
            class="full-width q-mt-md"
        />
</div>
    </q-card>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useQuasar } from 'quasar';
import axios from 'axios';

    export default defineComponent({
        name: "Clock",
        data() {
            const time = ref('10:56')
            const date = ref('2026-01-01')
            return {time, date};
        },

        methods: {
            putDateAndTime() {
                const $q = useQuasar();

                const dateTimeString = '${this.date}T${this.time}:00';
                const dateObj = new Date(dateTimeString);

                const unixNano = dateObj.getTime() * 1000000;

                axios.put('http://192.168.1.100:8080/api/setTime', JSON.stringify(unixNano), {
                    headers: {
                        'Content-Type': 'text/plain'
                    }
                } 
                ).then((_) => {
                    this.$q.notify({
                        message: "Device time updated successfully. Please check logged packets.",
                        color: "positive"
                    })
                }).catch((_) => {
                    this.$q.notify({
                        message: "Failed to update time. Please try again",
                        color: "negative"
                    })
                })
            }
        }
    })
</script>