<template>
	<li 
	    class="list-item" 
	    @click="$emit('item-click', itemData)"
	    :class="{ 'active': active }"
	>
	    {{itemData.title}}
	</li>
</template>

<script setup lang="ts">
	defineProps({
	  active: {
	    type: Boolean,
	    default: false
	  },
	  itemData: {
	    type: Object,
	    default: () => ({})
	  }
	})
	
	defineEmits(['item-click'])
</script>

<style>
	
</style>