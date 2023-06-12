<template>
  <div class="max-w-5xl mx-auto mt-5">
    <router-link
        :to="{name: 'DisciplineCreateView'}"
        class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 text-base font-semibold text-white outline-none hover:bg-blue-600"
    >
      Создать дисциплину
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
                  Последний семестр
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
                  v-for="(item, index) in this.disciplines"
                  :key="item.id"
              >
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.code }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.end_semester }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.program.code + " " + item.program.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-right whitespace-nowrap">
                  <router-link :to="{name: 'DisciplineView', params: {discipline_id: item.id}}"
                               class="text-blue-600 hover:underline">
                    Edit
                  </router-link>
                </td>
                <td @click="delete_discipline(index)">
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
  name: 'DisciplineView',
  components: {},
  data() {
    return {}
  },
  created: function () {
    return this.$store.dispatch("getDisciplines")
  },
  computed: {
    ...mapGetters({disciplines: "stateDisciplines"})
  },
  methods: {
    ...mapActions(["getDisciplines", "deleteDiscipline"]),
    async delete_discipline(discipline_index) {
      let discipline = this.disciplines[discipline_index]
      let answer = confirm(`Вы действительно хотите удалить дисциплину ${discipline.title}?`)
      if (answer) {
        await this.deleteDiscipline(discipline.id)
        this.disciplines.splice(discipline_index, 1)
      }
    }
  }
}
</script>

<style scoped>

</style>
