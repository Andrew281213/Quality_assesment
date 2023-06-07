import { createStore } from "vuex"

import questions from "./modules/questions"
import disciplines from "./modules/disciplines"

export default createStore({
    modules: {
        questions,
        disciplines
    }
})
