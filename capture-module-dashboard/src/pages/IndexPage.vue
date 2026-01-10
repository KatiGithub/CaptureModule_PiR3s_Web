<template>
  <HomePage/>
</template>

<style></style>

<script lang="ts">
import { defineComponent } from 'vue';
import type { Todo, Meta } from 'components/models';
import HomePage from './HomePage.vue';

export default defineComponent({
  name: 'IndexPage',

  components: {
    HomePage
  },
  data() {
    const todos: Todo[] = [
      {
        id: 1,
        content: 'ct1',
      },
      {
        id: 2,
        content: 'ct2',
      },
      {
        id: 3,
        content: 'ct3',
      },
      {
        id: 4,
        content: 'ct4',
      },
      {
        id: 5,
        content: 'ct5',
      },
    ];

    const meta: Meta = {
      totalCount: 1200,
    };

    return { todos, meta };
  },
  methods: {
    testMethod() {

    }
  }
});
</script>
