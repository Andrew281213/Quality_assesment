import axios from "axios"

const state = {
    opops: null,
    opop: null
}

const getters = {
    stateOpops: state => state.opops,
    stateOpop: state => state.opop
}

const actions = {
    async getOpops({ commit }) {
        let { data } = await axios.get("api/v1/opop/")
        commit("setOpops", data)
    },
    async getOpop({ commit }, opop_id) {
        if (opop_id === null) {
            return
        }
        let { data } = await axios.get(`api/v1/opop/${opop_id}`)
        commit("setOpop", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createOpop({}, data) {
        await axios.post("api/v1/opop/", data.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateOpop({}, data) {
        await axios.put(`api/v1/opop/${data.id}`, data.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteOpop({}, opop_id) {
        await axios.delete(`api/v1/opop/${opop_id}`)
    }
}

const mutations = {
    setOpops(state, opops) {
        state.opops = opops
    },
    setOpop(state, opop) {
        state.opop = opop
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}