<template>
  <div>
    <h1>Кимы</h1>
    <button type="submit" class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 mr-3 text-base font-semibold text-white outline-none hover:bg-blue-600">Типо кнопка добавления кима</button>
    <button type="submit" class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 text-base font-semibold text-white outline-none hover:bg-blue-600">Типо кнопка выгрузки случайных кимов</button>
    <p>Тут должен быть фильтр...</p>
    <TableComponent :set_checkbox=true header_title="Ким" :data="get_table_data()"></TableComponent>
  </div>
</template>

<script>
  import {mapGetters, mapActions} from "vuex";
  import TableComponent from "@/components/TableComponent.vue";

  export default {
    name: 'KimsView',
    components: {TableComponent},
    data() {
      return {}
    },
    created: function() {
      return this.$store.dispatch("getKims")
    },
    computed: {
      ...mapGetters({kims: "stateKims"})
    },
    methods: {
      ...mapActions(["getKims"]),
      get_table_data() {
        let data = this.kims
        let result = []
        if (data === null || data.length === 0) {
          return result
        }
        for (let i = 0; i < data.length; i++) {
          result.push({"title": data[i].text})
        }
        return result
      }
    }
  }
</script>

<style scoped>

</style>
