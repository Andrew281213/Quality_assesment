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