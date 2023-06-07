<template>
  <div>
    <h1>Дисциплины</h1>
    <TableComponent :set_checkbox=false header_title="Дисциплина" :data="disciplines"></TableComponent>
  </div>
</template>

<script>
  import {mapGetters, mapActions} from "vuex";
  import TableComponent from "@/components/TableComponent.vue";

  export default {
    name: 'DisciplinesView',
    components: {TableComponent},
    data() {
      return {}
    },
    created: function() {
      return this.$store.dispatch("getDisciplines")
    },
    computed: {
      ...mapGetters({disciplines: "stateDisciplines"})
    },
    methods: {
      ...mapActions(["getDisciplines"])
    }
  }
</script>

<style scoped>

</style>
