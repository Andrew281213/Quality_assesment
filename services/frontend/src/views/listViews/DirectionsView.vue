<template>
  <div class="max-w-5xl mx-auto mt-5">
    <router-link
        :to="{name: 'DirectionCreateView'}"
        class="hover:shadow-form rounded-md bg-blue-700 py-3 px-3 mt-10 text-base font-semibold text-white outline-none hover:bg-blue-600"
    >
      Создать направление
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
                <td class="py-4 text-sm font-medium text-right">
                  <router-link :to="{name: 'DirectionView', params: {direction_id: item.id}}"
                               class="text-blue-600 hover:underline">
                    <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none"
                         xmlns="http://www.w3.org/2000/svg">
                      <path fill-rule="evenodd" clip-rule="evenodd"
                            d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z"
                            fill="#000000"/>
                    </svg>
                  </router-link>
                </td>
                <td @click="delete_direction(index)">
                  <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g id="Interface / Trash_Full">
                      <path id="Vector"
                            d="M14 10V17M10 10V17M6 6V17.8C6 18.9201 6 19.4798 6.21799 19.9076C6.40973 20.2839 6.71547 20.5905 7.0918 20.7822C7.5192 21 8.07899 21 9.19691 21H14.8031C15.921 21 16.48 21 16.9074 20.7822C17.2837 20.5905 17.5905 20.2839 17.7822 19.9076C18 19.4802 18 18.921 18 17.8031V6M6 6H8M6 6H4M8 6H16M8 6C8 5.06812 8 4.60241 8.15224 4.23486C8.35523 3.74481 8.74432 3.35523 9.23438 3.15224C9.60192 3 10.0681 3 11 3H13C13.9319 3 14.3978 3 14.7654 3.15224C15.2554 3.35523 15.6447 3.74481 15.8477 4.23486C15.9999 4.6024 16 5.06812 16 6M16 6H18M18 6H20"
                            stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </g>
                  </svg>
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
    return {}
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
