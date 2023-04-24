<template>
  <div>
    <h1>Вопросы</h1>
    <QuestionsTable></QuestionsTable>
  </div>
</template>

<script>
  import QuestionsTable from "@/components/QuestionsTable.vue";

  export default {
    name: 'MainPage',
    components: {QuestionsTable},
    data() {
      return {}
    }
  }
</script>

<style scoped>

</style>
