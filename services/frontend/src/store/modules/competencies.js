import axios from "axios"

const state = {
    competencies: null,
    competence: null
}

const getters = {
    stateCompetencies: state => state.competencies,
    stateCompetence: state => state.competence
}

const actions = {
    async getCompetencies({ commit }) {
        let { data } = await axios.get("api/v1/competence/")
        commit("setCompetencies", data)
    },
    async getCompetence({ commit }, competence_id) {
        let { data } = await axios.get(`api/v1/competence/${competence_id}/`)
        commit("setCompetence", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createCompetence({}, competence) {
        await axios.post("api/v1/competence/", competence.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateCompetence({}, competence) {
        await axios.put(`api/v1/competence/${competence.id}`, competence.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteCompetence({}, competence_id) {
        await axios.delete(`api/v1/competence/${competence_id}`)
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