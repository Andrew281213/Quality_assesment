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
        let { data } = await axios.get(`api/v1/kim/${kim_id}`)
        commit("setKim", data)
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