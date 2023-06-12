<template>
  <div class="max-w-5xl mx-auto mt-5">
    <router-link
        :to="{name: 'CompetenceCreateView'}"
        class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 text-base font-semibold text-white outline-none hover:bg-blue-600"
    >
      Создать компетенцию
    </router-link>
    <div class="flex flex-col mt-6">
      <div class="overflow-x-auto shadow-md sm:rounded-lg">
        <div class="inline-block min-w-full align-middle">
          <div class="overflow-hidden ">
            <table id="questions-table" class="min-w-full divide-y divide-gray-200 table-fixed">
              <thead class="bg-gray-100">
              <tr>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Шифр
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Название
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Тип
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Профиль
                </th>
                <th scope="col" class="p-4">
                  <span class="sr-only">Edit</span>
                </th>
                <th scope="col" class="p-4">
                  <span class="sr-only">Delete</span>
                </th>
              </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
              <tr
                  class="hover:bg-gray-100"
                  v-for="(item, index) in this.competencies"
                  :key="item.id"
              >
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.code }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.type }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.opop.code + " " + item.opop.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-right whitespace-nowrap">
                  <router-link :to="{name: 'CompetenceView', params: {competence_id: item.id}}"
                               class="text-blue-600 hover:underline">
                    Edit
                  </router-link>
                </td>
                <td @click="delete_competence(index)">
                  Delete
                </td>
              </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {mapGetters, mapActions} from "vuex";

export default {
  name: 'CompetenciesView',
  components: {},
  data() {
    return {}
  },
  created: function () {
    return this.$store.dispatch("getCompetencies")
  },
  computed: {
    ...mapGetters({competencies: "stateCompetencies"})
  },
  methods: {
    ...mapActions(["getCompetencies", "deleteCompetence"]),
    async delete_competence(competence_index) {
      let competence = this.competencies[competence_index]
      let answer = confirm(`Вы действительно хотите удалить компетенцию ${competence.title}?`)
      if (answer) {
        await this.deleteCompetence(competence.id)
        this.competencies.splice(competence_index, 1)
      }
    }
  }
}
</script>

<style scoped>

</style>
