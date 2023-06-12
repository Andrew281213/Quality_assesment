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
            Название направления
          </label>
          <input
              type="text"
              name="title"
              id="title"
              placeholder="Название направления"
              v-model="form.title"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="code"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Шифр направления
          </label>
          <input
              type="text"
              name="code"
              id="code"
              placeholder="Шифр направления"
              v-model="form.code"
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
  name: 'DirectionView',
  components: {},
  props: ['direction_id'],
  data() {
    return {
      errors: [],
      form: {
        code: '',
        title: ''
      }
    }
  },
  async created() {
    await this.viewDirection()
  },
  computed: {
    ...mapGetters({direction: 'stateDirection'}),
  },
  methods: {
    ...mapActions(['getDirection', 'updateDirection']),
    async viewDirection() {
      try {
        await this.getDirection(this.direction_id)
        this.form.code = this.direction.code
        this.form.title = this.direction.title
      } catch (error) {
        console.error(error)
        this.$router.push("/directions")
      }
    },
    async save() {
      try {
        let direction = {
          id: this.direction_id,
          form: this.form
        }
        await this.updateDirection(direction)
        this.$router.push('/directions')
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