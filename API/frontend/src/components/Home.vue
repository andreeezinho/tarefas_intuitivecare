<script setup>
import { ref } from 'vue'
import  axios  from 'axios'
import { onMounted } from 'vue'

const data = ref([])

onMounted(async () => {
  try {
    const response = await axios.get("http://127.0.0.1:8000/search")
    data.value = response.data
  } catch (error) {
    console.error("Erro ao buscar as operadoras:", error)
  }
})

defineProps({
  msg: String,
})

</script>

<template>
  <h1>Teste IntuitiveCare</h1>

  <ul v-for="(item, index) in data" :key="index">
      <li>{{ item }}</li>
  </ul>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
