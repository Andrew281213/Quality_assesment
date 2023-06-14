import axios from "axios"

const state = {
    kims: null,
    kim: null
}

const getters = {
    stateKims: state => state.kims,
    stateKim: state => state.kim
}

const actions = {
    async getKims({ commit }) {
        let { data } = await axios.get("api/v1/kim/")
        commit("setKims", data)
    },
    async getKim({ commit }, kim_id) {
        let { data } = await axios.get(`api/v1/kim/${kim_id}/`)
        commit("setKim", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createKim({}, kim) {
        await axios.post("api/v1/kim/", kim.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateKim({}, kim) {
        await axios.put(`api/v1/kim/${kim.id}`, kim.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteKim({}, kim_id) {
        await axios.delete(`api/v1/kim/${kim_id}`)
    }
}

const mutations = {
    setKims(state, kims) {
        state.kims = kims
    },
    setKim(state, kim) {
        state.kim = kim
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}