<template>
  <div class="chat-box">
    <div class="chat-container">
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="{
          'user-message': message.type === 'user',
          'bot-message': message.type === 'bot',
        }"
        class="message"
      >
        {{ message.text }}
      </div>
      <!-- 使用 Progress 组件 -->
      <Progress v-if="showProgressBar" />
    </div>
    <div class="input-container">
      <input
        type="text"
        v-model="newMessage"
        @keyup.enter="sendMessage"
        placeholder="请输入您的诉求..."
      />
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Progress from "@/components/Progress.vue"; // 导入 Progress 组件

export default {
  components: {
    Progress, // 注册 Progress 组件
  },
  data() {
    return {
      messages: [],
      newMessage: "",
      showProgressBar: false, // 控制进度条显示
    };
  },
  methods: {
    async sendMessage() {
      if (this.newMessage.trim() === "") return;

      // Push the user's message to the chat UI
      this.messages.push({ text: this.newMessage, type: "user" });

      // 显示进度条
      this.showProgressBar = true;

      try {
        // Send the message to the FastAPI endpoint
        const response = await axios.post("http://localhost:8000/test/", {
          text: this.newMessage, // Send the message text
        });

        // Handle the response from the server
        if (response.data && response.data.message) {
          // Push the bot's reply to the chat UI
          setTimeout(() => {
            this.messages.push({ text: response.data.message, type: "bot" });
            //隐藏进度条
            this.showProgressBar = false;
          }, 5000);
        } else {
          console.error("Invalid response format from server");
          //隐藏进度条
          this.showProgressBar = false;
        }
      } catch (error) {
        console.error("Error sending message:", error.message);
        // Handle error, show error message in chat UI, etc.
      }

      // Clear the input field after sending the message
      this.newMessage = "";
    },
  },
};
</script>


<style>
.chat-box {
  width: 160vh;
  height: 80vh;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 15px;
}

.chat-container {
  height: 75vh;
  margin: 0 auto;
  overflow-y: auto;
  padding: 10px;
  /* border: 1px solid #ccc; */
  border-radius: 5px;
}

.message {
  margin-bottom: 10px;
  padding: 5px 10px;
  border-radius: 5px;
}

.user-message {
  background-color: #dcf8c6;
  align-self: flex-end;
}

.bot-message {
  background-color: #eaeaea;
}

.input-container {
  margin-top: 10px;
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.input-container input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;

}

.input-container button {
  padding: 8px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.input-container button:hover {
  background-color: #0056b3;
}
</style>
