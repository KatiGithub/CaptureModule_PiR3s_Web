<template>
    <q-card flat bordered class="my-card">
        <q-card-section>
            <div class="text-h6">Toggle</div>
        </q-card-section>
              
        <q-card-section class="q-pt-none">
          Toggle types of packets for logging. (Logging Counters still get updated from the packet)
        </q-card-section>

        <div class="q-pa-md q-gutter-lg">
            <div>
              <q-toggle
                  v-model="tcp"
                  color="green"
                  label="TCP"
                  @click="updateToggleInformation"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="arp"
                  color="yellow"
                  label="ARP"
                  @click="updateToggleInformation"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="udp"
                  color="red"
                  label="UDP"
                  @click="updateToggleInformation"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="others"
                  color="blue"
                  label="Others"
                  @click="updateToggleInformation"
              />
            </div>
        </div>
                   
        <q-separator inset />
              
    </q-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
    export default defineComponent({
        name: "Toggle",
        mounted() {
            this.getToggleInformation()
        },
        data() {
            const tcp = true;
            const arp = true;
            const udp = true;
            const others = true;
            const can_update = true;
            return {tcp, arp, udp, others, can_update};
        },
        methods: {
            getToggleInformation() {
                axios.get('http://192.168.1.100:8080/api/loadConfig')
                    .then((val) => {
                        if(this.can_update) {
                            const response_body = val.data;
                            this.tcp = response_body["logTCP"]
                            this.arp = response_body["logARP"]
                            this.udp = response_body["logUDP"]
                            this.others = response_body["logOthers"]
                        }
                        setTimeout(() => {
                            this.getToggleInformation();
                        }, 200)
                    })
            },
            updateToggleInformation() {
                this.can_update = false;
                const req_body = {
                    "logTCP": this.tcp,
                    "logARP": this.arp,
                    "logUDP": this.udp,
                    "logOthers": this.others
                }
                let config = {
                    method: 'put',
                    maxBodyLength: Infinity,
                    url: 'http://192.168.1.100:8080/api/updateConfig',
                    headers: { 
                        'Content-Type': 'text/plain'
                    },
                    data : JSON.stringify(req_body)
                };

                axios.request(config)
                    .then((response) => {
                        console.log(response)
                        this.can_update = true;
                    })
                    .catch((error) => {
                    console.log(error);
                });
            }
        }
    })
</script>