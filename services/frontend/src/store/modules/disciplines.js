import axios from "axios"

const state = {
    disciplines: null,
    discipline: null
}

const getters = {
    stateDisciplines: state => state.disciplines,
    stateDiscipline: state => state.discipline
}

const actions = {
    async getDisciplines({ commit }) {
        let { data } = await axios.get("api/v1/discipline/")
        commit("setDisciplines", data)
    },
    async getDiscipline({ commit }, discipline_id) {
        let { data } = await axios.get(`api/v1/discipline/${discipline_id}`)
        commit("setDiscipline", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createDiscipline({}, discipline) {
        await axios.post("api/v1/discipline/", discipline.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateDiscipline({}, discipline) {
        await axios.put(`api/v1/discipline/${discipline.id}`, discipline.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteDiscipline({}, discipline_id) {
        await axios.delete(`api/v1/discipline/${discipline_id}`)
    }
}

const mutations = {
    setDisciplines(state, disciplines) {
        state.disciplines = disciplines
    },
    setDiscipline(state, discipline) {
        state.discipline = discipline
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}