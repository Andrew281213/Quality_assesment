import { createStore } from "vuex"

import questions from "./modules/questions"

export default createStore({
    modules: {
        questions
    }
})