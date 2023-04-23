<template>
  <nav id="menu" class="bg-white border-gray-200">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-around ly mx-auto p-4">
      <a href="/" class="flex items-center">
        <img src="@/assets/logo.jpg" class="h-16 mr-3" alt="Лого"/>
      </a>
      <button data-collapse-toggle="navbar-default" type="button"
              class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200"
              aria-controls="navbar-default" aria-expanded="false"
               onclick="document.getElementById('navbar').classList.toggle('hidden')"
      >
        <span class="sr-only">Открыть главное меню</span>
        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
             xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
                d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                clip-rule="evenodd"></path>
        </svg>
      </button>
      <div class="hidden w-full md:block md:w-auto" id="navbar">
        <ul
            class="font-medium flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:p-0 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-white"
        >
          <li>
            <router-link
                :to="{name: 'MainPage'}"
                v-bind:class="(currentRouteName === 'MainPage') ?
                `block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0`:
                `block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0`"
                onclick="document.getElementById('navbar').classList.add('hidden')"
            >
              Главная
            </router-link>
          </li>
          <li>
            <router-link
                :to="{name: 'SpecialtiesView'}"
                v-bind:class="(currentRouteName === 'SpecialtiesView') ?
                `block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0`:
                `block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0`"
                onclick="document.getElementById('navbar').classList.add('hidden')"
            >
              Специальности
            </router-link>
          </li>
          <li>
            <router-link
                :to="{name: 'GroupsView'}"
                v-bind:class="(currentRouteName === 'GroupsView') ?
                `block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0`:
                `block py-2 pl-3 pr-4 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0`"
                onclick="document.getElementById('navbar').classList.add('hidden')"
            >
              Группы
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {}
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    }
  }
}
</script>

<style scoped>

</style>
