<template>
  <div>
    <h1>ОПОПы</h1>
    <TableComponent :set_checkbox=false header_title="ОПОП" :data="[]"></TableComponent>
  </div>
</template>

<script>
  import TableComponent from "@/components/TableComponent.vue";

  export default {
    name: 'OpopsView',
    components: {TableComponent},
    data() {
      return {}
    }
  }
</script>

<style scoped>

</style>
