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
            Название компетенции
          </label>
          <input
              type="text"
              name="title"
              id="title"
              placeholder="Название компетенции"
              v-model="form.title"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="code"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Шифр компетенции
          </label>
          <input
              type="text"
              name="code"
              id="code"
              placeholder="Шифр компетенции"
              v-model="form.code"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
          />
        </div>
        <div class="mb-5">
          <label
              for="type"
              class="mb-3 block text-base font-medium text-gray-700"
          >
            Тип компетенции
          </label>
          <select
              name="type"
              id="type"
              class="w-full rounded-md border border-blue-300 bg-white py-2 px-4 text-base font-medium text-gray-700 outline-none focus:border-blue-500 focus:shadow-md"
              v-model="form.type"
          >
            <option value="ОК">ОК</option>
            <option value="ОПК">ОПК</option>
            <option value="ПК">ПК</option>
          </select>
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
              v-model="form.opop_id"
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
  name: 'CompetenceView',
  components: {},
  props: ['competence_id'],
  data() {
    return {
      errors: [],
      form: {
        code: '',
        title: '',
        type: '',
        opop_id: ''
      }
    }
  },
  async created() {
    await this.viewCompetence()
    await this.getOpops()
  },
  computed: {
    ...mapGetters({competence: 'stateCompetence', opops: 'stateOpops'}),
  },
  methods: {
    ...mapActions(['getCompetence', 'updateCompetence', 'getOpops']),
    async viewCompetence() {
      try {
        await this.getCompetence(this.competence_id)
        console.log(this.competence)
        this.form.code = this.competence.code
        this.form.title = this.competence.title
        this.form.type = this.competence.type
        this.form.opop_id = this.competence.opop.id
      } catch (error) {
        console.error(error)
        this.$router.push("/competencies")
      }
    },
    async save() {
      try {
        let competence = {
          id: this.competence_id,
          form: this.form
        }
        await this.updateCompetence(competence)
        this.$router.push('/competencies')
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