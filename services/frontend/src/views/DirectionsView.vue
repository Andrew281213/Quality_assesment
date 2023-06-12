<template>
  <router-link
      :to="{name: 'DirectionCreateView'}"
      class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 mb-5 mt-10 text-base font-semibold text-white outline-none hover:bg-blue-600"
  >
    Создать направление
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
                  Шифр
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  Название
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
                  v-for="(item, index) in this.directions"
                  :key="item.id"
              >
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.code }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-right whitespace-nowrap">
                  <router-link :to="{name: 'DirectionView', params: {direction_id: item.id}}"
                               class="text-blue-600 hover:underline">
                    Edit
                  </router-link>
                </td>
                <td @click="delete_direction(index)">
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
  name: 'DirectionsView',
  components: {},
  data() {
    return {
      currentDirection: null,
      isModalVisible: false,
    }
  },
  created: function () {
    return this.$store.dispatch("getDirections")
  },
  computed: {
    ...mapGetters({directions: "stateDirections"})
  },
  methods: {
    ...mapActions(["getDirections", "deleteDirection"]),
    async delete_direction(direction_index) {
      let direction = this.directions[direction_index]
      let answer = confirm(`Вы действительно хотите удалить направление ${direction.title}?`)
      if (answer) {
        await this.deleteDirection(direction.id)
        this.directions.splice(direction_index, 1)
      }
    }
  }
}
</script>

<style scoped>
.is-blurred {
  filter: blur(2px);
  -webkit-filter: blur(2px);
}
</style>
