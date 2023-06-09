import { createStore } from "vuex"

import disciplines from "./modules/disciplines"
import competencies from "./modules/competencies";
import kims from "./modules/kims"
import directions from "./modules/directions"
import opops from "./modules/opops"
import disciplines_competencies from "./modules/disciplines_competencies";


export default createStore({
    modules: {
        disciplines,
        competencies,
        kims,
        directions,
        opops,
        disciplines_competencies
    }
})
