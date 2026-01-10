<template>
    <q-card flat bordered class="my-card">
        <q-card-section>
            <div class="text-h6">Toggle</div>
        </q-card-section>
              
        <q-card-section class="q-pt-none">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
          tempor incididunt ut labore et dolore magna aliqua.
        </q-card-section>

        <div class="q-pa-md q-gutter-lg">
            <div>
              <q-toggle
                  v-model="tcp"
                  color="green"
                  label="TCP"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="arp"
                  color="yellow"
                  label="ARP"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="udp"
                  color="red"
                  label="UDP"
              />
            </div>
            
            <div>
              <q-toggle
                  v-model="others"
                  color="blue"
                  label="Others"
              />
            </div>
        </div>
                   
        <q-separator inset />
              
        <q-card-section>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua.
        </q-card-section>
    </q-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
    export default defineComponent({
        name: "Toggle",
        data() {
            const tcp = false;
            const arp = false;
            const udp = false;
            const others = false;
            return {tcp, arp, udp, others};
        }
    })
</script>