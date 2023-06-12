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
            Название дисциплины
          </label>
          <input
              type="text"
              name="title"
              id="title"
              placeholder="Название дисциплины"
              v-model="form.title"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="code"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Шифр дисциплины
          </label>
          <input
              type="text"
              name="code"
              id="code"
              placeholder="Шифр дисциплины"
              v-model="form.code"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="end_semester"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Семестр окончания
          </label>
          <input
              type="text"
              name="end_semester"
              id="end_semester"
              placeholder="Семестр окончания"
              v-model="form.end_semester"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="opop"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Профиль
          </label>
          <select
              name="opop"
              id="opop"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
              v-model="form.program_id"
          >
            <option
                v-for="opop in opops"
                :key="opop.id"
                :value="opop.id"
            >
              {{ opop.code + " " + opop.title }}
            </option>
          </select>
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
  name: 'DisciplineView',
  components: {},
  props: ['discipline_id'],
  data() {
    return {
      errors: [],
      form: {
        code: '',
        title: '',
        end_semester: '',
        program_id: ''
      }
    }
  },
  async created() {
    await this.viewDiscipline()
    await this.getOpops()
  },
  computed: {
    ...mapGetters({discipline: 'stateDiscipline', opops: 'stateOpops'}),
  },
  methods: {
    ...mapActions(['getDiscipline', 'updateDiscipline', 'getOpops']),
    async viewDiscipline() {
      try {
        console.log(this.discipline_id)
        await this.getDiscipline(this.discipline_id)
        this.form.code = this.discipline.code
        this.form.title = this.discipline.title
        this.form.end_semester = this.discipline.end_semester
        this.form.program_id = this.discipline.program.id
      } catch (error) {
        console.error(error)
        this.$router.push("/disciplines")
      }
    },
    async save() {
      console.log(this.form)
      try {
        let discipline = {
          id: this.discipline_id,
          form: this.form
        }
        await this.updateDiscipline(discipline)
        this.$router.push('/disciplines')
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