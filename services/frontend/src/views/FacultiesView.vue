<template>
  <div>
    <h1>Факультеты</h1>
    <TableComponent :set_checkbox=false header_title="Факультет" :data="this.get_table_data()"></TableComponent>
  </div>
</template>

<script>
  import TableComponent from "@/components/TableComponent.vue";
  import {mapActions, mapGetters} from "vuex";

  export default {
    name: 'FacultiesView',
    components: {TableComponent},
    data() {
      return {}
    },
    created: function() {
      return this.$store.dispatch("getFaculties")
    },
    computed: {
      ...mapGetters({faculties: "stateFaculties"}),
    },
    methods: {
      ...mapActions(["getFaculties"]),
      get_table_data() {
        let data = this.faculties
        let result = []
        if (data === null || data.length === 0) {
          return result
        }
        for (let i = 0; i < data.length; i++) {
          result.push({"title": data[i].full_title})
        }
        return result
      }
    }
  }
</script>

<style scoped>

</style>
