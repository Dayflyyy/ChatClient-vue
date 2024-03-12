<template>
  <div class="common-layout">
    <el-container>
      <el-header height="80px" class="header">
        <el-row class="header-content">
          <el-col :span="1"> <img src="/favicon.ico" /></el-col>
          <el-col class="text" :span="1"> ChatClient</el-col>
        </el-row>
      </el-header>
      <el-container>
        <el-aside class="aside">
          <ul>
            <li>
              <el-upload
                v-model:file-list="fileList"
                class="upload-demo"
                action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
                multiple
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :before-remove="beforeRemove"
                :limit="3"
                :on-exceed="handleExceed"
              >
                <el-button type="primary">上传图像</el-button>
                <template #tip>
                  <div class="el-upload__tip">
                    支持.jpg/.png/.dcm
                  </div>
                </template>
              </el-upload>
            </li>
            <li><el-button>医生咨询</el-button></li>
          </ul>
        </el-aside>
        <el-main><Main /></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
import Main from "./views/pages/Main.vue";
import { ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";

import type { UploadProps, UploadUserFile } from "element-plus";

const fileList = ref<UploadUserFile[]>([
  {
    name: "element-plus-logo.svg",
    url: "https://element-plus.org/images/element-plus-logo.svg",
  },
  {
    name: "element-plus-logo2.svg",
    url: "https://element-plus.org/images/element-plus-logo.svg",
  },
]);

const handleRemove: UploadProps["onRemove"] = (file, uploadFiles) => {
  console.log(file, uploadFiles);
};

const handlePreview: UploadProps["onPreview"] = (uploadFile) => {
  console.log(uploadFile);
};

const handleExceed: UploadProps["onExceed"] = (files, uploadFiles) => {
  ElMessage.warning(
    `The limit is 3, you selected ${files.length} files this time, add up to ${
      files.length + uploadFiles.length
    } totally`
  );
};

const beforeRemove: UploadProps["beforeRemove"] = (uploadFile, uploadFiles) => {
  return ElMessageBox.confirm(`Cancel the transfer of ${uploadFile.name} ?`).then(
    () => true,
    () => false
  );
};
</script>

<style scoped>
.header {
  margin-bottom: 10px;
  background-color: #333333;
}
.header-content {
  margin-top: 25px;
  margin-left: 20px;
  font-family: "Roboto", sans-serif;
  font-weight: 700;
}
li {
  margin-bottom: 20px;
}

.text {
  font-family: "Roboto", sans-serif;
  font-weight: 700;
  color: #ddd;
  scale: 200%;
  margin-top: 10px;
}
.aside {
  width: 220px;
  background-color: #ddd;
  box-shadow: 0 0 10px;
  border-radius: 10px;
  padding: 20px;
  margin: 20px 0px 20px 30px;

  height: 84vh;
  /* 高度填满页面 */
}
</style>
