import { createRouter, createWebHistory } from 'vue-router'
import ProblemView from '../views/ProblemView.vue'
import AboutViewVue from '../views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
	{
		// 这里流出来一个主页面，如果临时变更需要的话可以用，现在跳转到问题页面
		path: "/",
		redirect: "/problem",
	},
    {
		path: '/problem',
		name: 'problem',
		component: ProblemView,
    },
    {
		path: '/about',
		name: 'about',
		component: AboutViewVue,
    },
	{
		path: '/problem/:id',
		name: "ProblemDetail",
		component: () => import("@/views/ProblemDetail.vue")
	},
	{
		path: '/login',
		name: "login",
		component: () => import("@/views/LoginView.vue")
	}
  ],
})

export default router
