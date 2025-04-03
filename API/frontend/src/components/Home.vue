<script setup>
import { onMounted, ref } from 'vue'
import  axios  from 'axios'

const filtro = ref('')
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
    const resp = await api.search(filtro.value)
    console.log("Busca: ", resp)
    data.value = resp
  } catch (error) {
    console.error("Erro ao buscar as operadoras:", error)
    return null
  }
}

</script>

<template>
  <div class="col">
    <h1>Teste IntuitiveCare</h1>
    <p>Procure o nome da operadora</p>

    <div>
      <input type="text" v-model="filtro" class="input-filter" placeholder="Digite aqui">
      <button @click="getResult">Buscar</button>
    </div>

    <div class="contact">
      <h4>Entre em contato</h4>

      <a href="https://github.com/andreeezinho">
        <img src="https://skillicons.dev/icons?i=github" alt="My Github">
      </a>
      <a href="https://www.linkedin.com/in/andr%C3%A9-sapucaia-96476b2b1/">
        <img src="https://skillicons.dev/icons?i=linkedin" alt="My LinkedIn">
      </a>
    </div>
  </div>

  <div class="col">
    <div v-for="(item, index) in data" :key="index" class="container-item bg-card">
        <p class="card-info">Razão: {{ item.Razao_Social }}</p>
        <p class="card-info">Nome: {{ item.Nome_Fantasia }}</p>
        <p class="card-info">Modalidade: {{ item.Modalidade }}</p>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}

.input-filter{
  margin-right: 10px;
  padding: 10px;
  width: 300px;
}

.col{
  width: 50%;
}

.container-item{
  background-color: #202020;
  border-radius: 20px;
  border: 1px solid #888;
  padding: 10px;
  margin: 10px 0 10px 0;
}

.card-info{
  text-align: justify;
}

.contact{
  margin-top: 150px;
}

.contact a {
  margin: 0 5px 0 5px;
}
</style>
