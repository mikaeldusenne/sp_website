import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
		state: {
				logged: false
		},
		mutations: {
				change(state, logged){
						state.logged = logged;
				}
		},
		actions: {
		},
		modules: {
		},
		getters: {
				logged: state => state.logged
		}
})
