import axios from "axios"

const state = {
    directions: null,
    direction: null
}

const getters = {
    stateDirections: state => state.directions,
    stateDirection: state => state.direction
}

const actions = {
    async getDirections({ commit }) {
        let { data } = await axios.get("api/v1/direction/")
        commit("setDirections", data)
    },
    async getDirection({ commit }, direction_id) {
        if (direction_id === null) {
            return
        }
        let { data } = await axios.get(`api/v1/direction/${direction_id}`)
        commit("setDirection", data)
    },
    // eslint-disable-next-line no-empty-pattern
    async createDirection({}, direction) {
        await axios.post("api/v1/direction/", direction.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async updateDirection({}, direction) {
        await axios.put(`api/v1/direction/${direction.id}`, direction.form)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteDirection({}, direction_id) {
        await axios.delete(`api/v1/direction/${direction_id}`)
    }
}

const mutations = {
    setDirections(state, directions) {
        state.directions = directions
    },
    setDirection(state, direction) {
        state.direction = direction
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}