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
          <label class="mb-3 block text-base font-medium text-gray-700">Компетенции</label>
          <VueMultiselect
              v-model="selected_competencies"
              :options="competencies_for_select"
              :multiple="true"
              placeholder="Наберите слово для поиска"
              label="code"
              track-by="id"
              :closeOnSelect="false"
              v-if="competencies !== null"
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
import VueMultiselect from "vue-multiselect"

export default {
  name: 'DisciplineView',
  components: {VueMultiselect},
  props: ['discipline_id'],

  data() {
    return {
      selected_competencies: [],
      competencies_for_select: [],
      errors: [],
      form: {
        code: '',
        title: '',
        end_semester: '',
        program_id: ''
      },
      dcs_form: {
        competencies: []
      }
    }
  },
  async created() {
    await this.getOpops()
    await this.viewDiscipline()
  },
  computed: {
    ...mapGetters({
      discipline: 'stateDiscipline',
      opops: 'stateOpops',
      dcs: 'stateDcs',
      competencies: 'stateCompetencies'
    })
  },
  methods: {
    ...mapActions(['getDiscipline', 'updateDiscipline', 'getOpops', 'getDcs', 'createDc', 'deleteDc', 'getCompetencies']),
    async viewDiscipline() {
      try {
        await this.getDiscipline(this.discipline_id)
        this.form.code = this.discipline.code
        this.form.title = this.discipline.title
        this.form.end_semester = this.discipline.end_semester
        this.form.program_id = this.discipline.program.id
        await this.get_competencies()
      } catch (error) {
        console.error(error)
        this.$router.push("/disciplines")
      }
    },
    async get_competencies() {
      await this.getCompetencies()
      await this.getDcs({"discipline_id": this.discipline_id})
      let competencies_for_select = []
      this.competencies.forEach(function (item) {
        competencies_for_select.push({"title": item.title, "code": item.code, "id": item.id})
      })
      let selected_competencies = []
      this.dcs.forEach(function (item) {
        selected_competencies.push({"id": item.competence.id, "code": item.competence.code, "title": item.competence.title})
      })
      this.competencies_for_select = competencies_for_select
      this.selected_competencies = selected_competencies
    },
    async save() {
      try {
        let discipline = {
          id: this.discipline_id,
          form: this.form
        }
        await this.updateDiscipline(discipline)
        // Находим id выбранных компетенций
        let competencies = []
        this.selected_competencies.forEach(function (item) {
          competencies.push(item.id)
        })
        let exist_competencies = []
        this.dcs.forEach(function (item) {
          exist_competencies.push(item.competence.id)
        })
        // Находим id компетенций для удаления
        let to_delete_dcs = []
        this.dcs.forEach(function (item) {
          if (!competencies.includes(item.competence.id)) {
            to_delete_dcs.push(item.id)
          }
        })
        // Перебираем массив id выбранных компетенций
        for (let i = 0; i < competencies.length; i++) {
          // Если компетенция уже связана - пропускаем
          if (exist_competencies.includes(competencies[i])) {
            continue
          }
          // Создаем новую связь
          let dc_form = {
            "competence_id": competencies[i],
            "discipline_id": this.discipline_id
          }
          await this.createDc(dc_form)
        }
        // Удаляем связи
        for (let i = 0; i < to_delete_dcs.length; i++) {
          await this.deleteDc(to_delete_dcs[i])
        }
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

<style src="vue-multiselect/dist/vue-multiselect.css"></style>