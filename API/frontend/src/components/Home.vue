<script setup>
import { onMounted, ref } from 'vue'
import  axios  from 'axios'

const data = ref([])

const api = {
  async search(filter){
    try {
      const response = await axios.get(`http://127.0.0.1:8000/search?filter=${filter}`)
      return response.data
    } catch (error) {
      console.error("Erro ao buscar as operadoras:", error)
      return []
    }
  }
}

const getResult = async () => {
  try {
    const resp = await api.search(["ASSOCIAÇÃO DOS FUNCIONÁRIOS DO FISCO DO ESTADO DE GOIÁS"])
    console.log("Busca: ", resp)
    data.value = resp
  } catch (error) {
    console.error("Erro ao buscar as operadoras:", error)
    return null
  }
}

</script>

<template>
  <h1>Teste IntuitiveCare</h1>

  <input type="text" v-model="busca" placeholder="Digite o nome da operadora">

  <ul v-for="(item, index) in data" :key="index">
      <li>{{ item }}</li>
  </ul>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
