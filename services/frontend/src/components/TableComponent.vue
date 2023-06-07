<template>
  <div class="max-w-5xl mx-auto">
    <div class="flex flex-col">
      <div class="overflow-x-auto shadow-md sm:rounded-lg">
        <div class="inline-block min-w-full align-middle">
          <div class="overflow-hidden ">
            <table id="questions-table" class="min-w-full divide-y divide-gray-200 table-fixed">
              <thead class="bg-gray-100">
              <tr v-if="this.set_checkbox">
                <th scope="col" class="p-4">
                  <div class="flex items-center">
                    <input
                        id="checkbox_all" type="checkbox"
                        class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 focus:ring-2"
                        onclick="checkAll()"
                    >
                  </div>
                </th>
                <th scope="col"
                    class="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase">
                  {{ this.header_title }}
                </th>
                <th scope="col" class="p-4">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
              <tr
                  class="hover:bg-gray-100"
                  v-for="item in this.data"
                  :key="item.id"
              >
                <td class="p-4 w-4" v-if="this.set_checkbox">
                  <div class="flex items-center">
                    <input id="checkbox-table-1" type="checkbox"
                           class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 focus:ring-2">
                  </div>
                </td>
                <td class="py-4 px-6 text-sm font-medium text-gray-900">
                  {{ item.title }}
                </td>
                <td class="py-4 px-6 text-sm font-medium text-right whitespace-nowrap">
                  <a href="#" class="text-blue-600 hover:underline">Edit</a>
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
export default {
  name: "TableComponent",
  props: ["header_title", "set_checkbox", "data"],
  data() {
    return {}
  }
}
</script>