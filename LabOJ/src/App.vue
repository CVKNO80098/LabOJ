<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
	<div>
		<header>
			<nav class="navbar">
				<RouterLink to="/">题库</RouterLink>
				<RouterLink to="/about">About</RouterLink>
				<RouterLink class="right" to="/login">登录</RouterLink>
			</nav>
		</header>
		<main>
			<RouterView />
		</main>
	</div>
</template>

<style scoped>
	/* 临时美化，可以修改 */
	div {
		height: 100vh;
		width: 100vh;
	}
	.navbar {
	  display: flex;
	  justify-content: space-between; 
	  align-items: center;
	  padding: 10px; 
	}
	
	.right {
	  margin-left: auto; 
	}

</style>
