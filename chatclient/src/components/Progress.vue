<template>
  <div class="demo-progress">
    <el-progress type="circle" :percentage="per" :status="per === 100 ? 'success' : ''" />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

const per = ref(0);

const colors = [
  { color: "#f56c6c", percentage: 20 },
  { color: "#e6a23c", percentage: 40 },
  { color: "#5cb87a", percentage: 60 },
  { color: "#1989fa", percentage: 80 },
  { color: "#6f7ad3", percentage: 100 },
];

onMounted(() => {
  setInterval(() => {
    per.value = (per.value % 100) + 10;
  }, 500);
});
</script>
<style scoped>
.demo-progress .el-progress--circle {
  margin-right: 15px;
}
</style>
