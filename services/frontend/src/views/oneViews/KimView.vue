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
              for="text"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Вопрос кима
          </label>
          <textarea
              name="text"
              id="text"
              placeholder="Вопрос кима"
              v-model="form.text"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
              style="height: 120px"
          />
        </div>
        <div class="mb-5">
          <label
              for="img"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Изображение
          </label>
          <input
              type="file"
              name="img"
              id="img"
              placeholder="Изображение кима"
              v-bind="form.img"
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
  name: 'KimView',
  components: {},
  props: ['kim_id'],
  data() {
    return {
      errors: [],
      form: {
        text: '',
        img: null
      }
    }
  },
  async created() {
    await this.viewKim()
  },
  computed: {
    ...mapGetters({kim: 'stateKim'}),
  },
  methods: {
    ...mapActions(['getKim', 'updateKim']),
    async viewKim() {
      try {
        await this.getKim(this.kim_id)
        this.form.text = this.kim.text
        this.form.img = this.kim.img
      } catch (error) {
        console.error(error)
        this.$router.push("/directions")
      }
    },
    async save() {
      try {
        let kim = {
          id: this.kim_id,
          form: this.form
        }
        await this.updateKim(kim)
        this.$router.push('/')
      } catch (error) {
        this.errors = []
        let req = error["request"]
        this.errors.push(JSON.parse(req["response"]))
        window.scrollTo(0, 0)
      }
    },
  }
}
</script>