<template>
  <div class="flex items-center justify-center p-12">
    <div class="mx-auto w-full max-w-[550px]">
      <div
          class="errors"
          v-for="(error, index) in errors"
          :key="index"
      >
        <p class="font-semibold text-red-700 pb-2">{{ error.detail }}</p>
      </div>
      <form @submit.prevent="save">
        <div class="mb-5">
          <label
              for="title"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Название профиля
          </label>
          <input
              type="text"
              name="title"
              id="title"
              placeholder="Название профиля"
              v-model="form.title"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="code"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Шифр профиля
          </label>
          <input
              type="text"
              name="code"
              id="code"
              placeholder="Шифр профиля"
              v-model="form.code"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="direction"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Направление
          </label>
          <select
              name="direction"
              id="direction"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
              v-model="form.direction_id"
          >
            <option
                v-for="direction in directions"
                :key="direction.id"
                :value="direction.id"
            >
              {{ direction.title }}
            </option>
          </select>
        </div>
        <div class="mb-5">
          <label
              for="start_year"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Год начала
          </label>
          <input
              type="text"
              name="start_year"
              id="start_year"
              placeholder="Год начала"
              v-model="form.start_year"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div>
          <button
              type="submit"
              class="hover:shadow-form rounded-md bg-blue-700 py-3 px-8 text-base font-semibold text-white outline-none hover:bg-blue-600"
          >
            Сохранить
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'OpopView',
  components: {},
  props: ['opop_id'],
  data() {
    return {
      errors: [],
      form: {
        code: '',
        title: '',
        direction_id: '',
        start_year: ''
      }
    }
  },
  async created() {
    await this.viewOpop()
    await this.getDirections()
  },
  computed: {
    ...mapGetters({opop: 'stateOpop', directions: "stateDirections"}),
  },
  methods: {
    ...mapActions(['getDirections', 'getOpop', 'updateOpop']),
    async viewOpop() {
      try {
        await this.getOpop(this.opop_id)
        this.form.code = this.opop.code
        this.form.title = this.opop.title
        this.form.start_year = this.opop.start_year
        this.form.direction_id = this.opop.direction.id
      } catch (error) {
        console.error(error)
        this.$router.push("/opops")
      }
    },
    async save() {
      try {
        let opop = {
          id: this.opop_id,
          form: this.form
        }
        await this.updateOpop(opop)
        this.$router.push('/opops')
      } catch (error) {
        this.errors = []
        let req = error["request"]
        if (req["status"] === 409) {
          this.errors.push(JSON.parse(req["response"]))
          window.scrollTo(0, 0)
        }
      }
    }
  }
}
</script>