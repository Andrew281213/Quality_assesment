import { createStore } from "vuex"

import questions from "./modules/questions"
import disciplines from "./modules/disciplines"
import faculties from "./modules/faculties";
import competencies from "./modules/competencies";
import kims from "./modules/kims"
export default createStore({
    modules: {
        questions,
        disciplines,
        faculties,
        competencies,
        kims
    }
})
