import axios from "axios"

const state = {
    dcs: null,
    dc: null
}

const getters = {
    stateDcs: state => state.dcs,
    stateDc: state => state.dc
}

const actions = {
    async getDcs({ commit }, params) {
        let { data } = await axios.get("api/v1/dcs/", { params: params })
        commit("setDcs", data)
    },
    async getDc({ commit }, dc_id) {
        let { data } = await axios.get(`api/v1/dcs/${dc_id}`)
        commit("setDc", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createDc({}, dc_form) {
        try {
            await axios.post("api/v1/dcs/", dc_form)
        } catch (error) {
            if (error["response"]["status"] !== 409) {
                console.log("error code", error["response"]["status"])
                throw error
            }
        }
    },
    // eslint-disable-next-line no-empty-pattern
    async updateDc({}, dc) {
        await axios.put(`api/v1/dcs/${dc.id}`, dc.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteDc({}, dc_id) {
        await axios.delete(`api/v1/dcs/${dc_id}`)
    }
}

const mutations = {
    setDcs(state, dcs) {
        state.dcs = dcs
    },
    setDc(state, dc) {
        state.dc = dc
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}