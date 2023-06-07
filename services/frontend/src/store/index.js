import { createStore } from "vuex"

import questions from "./modules/questions"
import disciplines from "./modules/disciplines"
import faculties from "./modules/faculties";
import competencies from "./modules/competencies";
export default createStore({
    modules: {
        questions,
        disciplines,
        faculties,
        competencies
    }
})
