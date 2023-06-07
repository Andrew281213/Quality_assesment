import axios from "axios"

const state = {
    faculties: null,
    faculty: null
}

const getters = {
    stateFaculties: state => state.faculties,
    stateFaculty: state => state.faculty
}

const actions = {
    async getFaculties({ commit }) {
        let { data } = await axios.get("api/v1/faculty/")
        commit("setFaculties", data)
    },
    async getDFaculty({ commit }, faculty_id) {
        let { data } = await axios.get(`api/v1/faculty/${faculty_id}`)
        commit("setFaculty", data)
    }
}

const mutations = {
    setFaculties(state, faculties) {
        state.faculties = faculties
    },
    setFaculty(state, faculty) {
        state.faculty = faculty
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
