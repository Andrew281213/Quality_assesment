<template>
  <div>
    <h1>Направленя</h1>
    <TableComponent :set_checkbox=false header_title="Направление" :data="[]"></TableComponent>
  </div>
</template>

<script>
  import TableComponent from "@/components/TableComponent.vue";

  export default {
    name: 'DirectionsView',
    components: {TableComponent},
    data() {
      return {}
    }
  }
</script>

<style scoped>

</style>
