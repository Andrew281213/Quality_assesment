<template>
  <div>
    <h1>Компетенции</h1>
    <TableComponent :set_checkbox=false header_title="Компетенция" :data="competencies"></TableComponent>
  </div>
</template>

<script>
  import {mapGetters, mapActions} from "vuex";
  import TableComponent from "@/components/TableComponent.vue";

  export default {
    name: 'CompetenciesView',
    components: {TableComponent},
    data() {
      return {}
    },
    created: function() {
      return this.$store.dispatch("getCompetencies")
    },
    computed: {
      ...mapGetters({competencies: "stateCompetencies"})
    },
    methods: {
      ...mapActions(["getCompetencies"])
    }
  }
</script>

<style scoped>

</style>
