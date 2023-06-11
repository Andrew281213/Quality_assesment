import { createStore } from "vuex"

import disciplines from "./modules/disciplines"
import competencies from "./modules/competencies";
import kims from "./modules/kims"
export default createStore({
    modules: {
        disciplines,
        competencies,
        kims
    }
})
