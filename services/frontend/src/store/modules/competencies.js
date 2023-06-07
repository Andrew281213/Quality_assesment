import axios from "axios"

const state = {
    competencies: null,
    competence: null
}

const getters = {
    stateCompetencies: state => state.competencies,
    stateCompetence: state => state.competencies
}

const actions = {
    async getCompetencies({ commit }) {
        let { data } = await axios.get("api/v1/competence/")
        commit("setCompetencies", data)
    },
    async getCompetence({ commit }, competence_id) {
        let { data } = await axios.get(`api/v1/competence/${competence_id}`)
        commit("setCompetence", data)
    }
}

const mutations = {
    setCompetencies(state, competencies) {
        state.competencies = competencies
    },
    setCompetence(state, competence) {
        state.competence = competence
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}