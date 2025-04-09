<!-- ProblemView.vue -->
<template>
  <ul class="list-container">
    <ListItem
      v-for="item in items"
      :key="item.id"
      :item-data="item"
      :active="selectedItem?.id === item.id"
      @item-click="handleItemClick(item)"
    >
    </ListItem>
  </ul>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import axios from 'axios'
import ListItem from '../components/ListItem.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const items = ref<any[]>([])
const nextUrl = ref<string | null>(null)
const prevUrl = ref<string | null>(null)
const currentPage = ref(1)

// 网络请求
const fetchProblems = async (url = 'http://127.0.0.1:8000/api/problems/') => {
  try {
	console.log('Sending request to /api/problems/');
    const response = await axios.get(url)
	console.log('Response received:', response.data);
    items.value = response.data.results // 获取题目列表信息
    nextUrl.value = response.data.next // 获取下一页的链接
    prevUrl.value = response.data.previous //获取上一页的链接

    // 提取当前页码，不一定能用上，用不上就删掉
    const match = url.match(/page=(\d+)/)
    currentPage.value = match ? parseInt(match[1]) : 1
  } catch (error) {
    console.error('分页加载失败:', error)
  }
}

const selectedItem = ref(null)
const handleItemClick = (item) => {
  selectedItem.value = item
  router.push({ name: 'ProblemDetail', params: { id: item.id } })
}

onMounted(() => {
	fetchProblems();
})

</script>