<template>
	<div>
		<!-- 这个返回也完全可以用成ICO的嗷，自己改 -->
		<div @click="back()">返回</div> 
		<template v-if="error">
			<p class="error">{{ error }}</p>
		</template>
		<template v-else>
			<h1>{{ name }}</h1>
			<p>{{ description }}</p>
		</template>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

// 基础定义
const route = useRoute()
const id = ref(route.params.id)
const data = ref()

// 显示的的信息
const name = ref('')
const description = ref('')
const error = ref(null)

const fetchProblemDetail = async () => {
	// 获取详细信息
	try {
		const token = localStorage.getItem('token')
		const response = await axios.get(`http://127.0.0.1:8000/api/problems/${id.value}/`, {
			headers: {
				// Authorization: `Token ${token}`, //登录还没写，现在先用固定的token登录测试
				Authorization: "Token eeafaa5b76c308290672589fca3851f4900d8111"
			}
	})
		data.value = response.data
		name.value = data.value.title || '无标题'
		description.value = data.value.description || "无内容"
		//其他的你们看着加
	} catch (error) {
		console.error('获取题目详情失败:', error)
	}
}


onMounted(() => {
	fetchProblemDetail()
})
</script>

<style scoped>
.error {
  color: red;
  font-weight: bold;
}
</style>
