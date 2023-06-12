<template>
  <router-link
      :to="{name: 'OpopCreateView'}"
      class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 mb-5 mt-10 text-base font-semibold text-white outline-none hover:bg-blue-600"
  >
    Создать ОПОП
  </router-link>
  <div class="max-w-5xl mx-auto mt-5">
    <div class="flex flex-col">
      <div class="overflow-x-auto shadow-md sm:rounded-lg">
        <div class="inline-block min-w-full align-middle">
          <div class="overflow-hidden ">
            <table id="questions-table" class="min-w-full divide-y divide-gray-200 table-fixed">
              <thead class="bg-gray-100">
              <tr>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Шифр программы
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Название профиля
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Название направления
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Год начала
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
                  v-for="(item, index) in this.opops"
                  :key="item.id"
              >
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.code }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.direction.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.start_year }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-right whitespace-nowrap">
                  <router-link :to="{name: 'OpopView', params: {opop_id: item.id}}"
                               class="text-blue-600 hover:underline">
                    Edit
                  </router-link>
                </td>
                <td @click="delete_opop(index)">
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
  name: 'OpopsView',
  components: {},
  data() {
    return {
    }
  },
  created: function () {
    return this.$store.dispatch("getOpops")
  },
  computed: {
    ...mapGetters({opops: "stateOpops"})
  },
  methods: {
    ...mapActions(["getOpops", "deleteOpop"]),
    async delete_opop(opop_index) {
      let opop = this.opops[opop_index]
      let answer = confirm(`Вы действительно хотите удалить ОПОП ${opop.code} ${opop.title}?`)
      if (answer) {
        await this.deleteOpop(opop.id)
        this.opops.splice(opop_index, 1)
      }
    }
  }
}
</script>

<style scoped>

</style>
