<template>
    <q-card dark bordered class="bg-grey-9 my-card">
        <q-card-section>
            <div class="text-h6">Inject Packet</div>
        </q-card-section>

        <q-card-section>
            <q-input dark outlined v-model="inputValue" label="Inject ethernet packet (String -> Bytes)"
                hint="Enter packet for injection" />

            <div class="row justify-end q-mt-md">
                <q-btn color="primary" label="Update" @click="handleClick" />
            </div>
        </q-card-section>
    </q-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios'
import { useQuasar } from 'quasar';

export default defineComponent({
    data() {
        const $q = useQuasar()
        const inputValue = "";
        return { $q, inputValue }
    },
    methods: {
        handleClick() {
            const req_body = this.inputValue;
            let config = {
                method: 'post',
                maxBodyLength: Infinity,
                url: 'http://192.168.1.100:8080/api/injectPacket',
                headers: {
                    'Content-Type': 'text/plain'
                },
                data: JSON.stringify(req_body)
            };
            axios.request(config)
                .then((val) => {
                    this.$q.notify({
                        message: "Packet successfully injected",
                        color: "positive"
                    })
                })
                .catch((error) => {
                    this.$q.notify({
                        message: "Injection unsuccessful",
                        color: "negative"
                    })
                })
        }
    }
})
</script>