<template>
  <div>
    <form @submit.prevent="addTask">
      <input v-model="newTask.name" placeholder="Enter a task" required />
      <input v-model.number="newTask.priority" type="number" placeholder="Priority (1-10)" min="1" max="10" required />
      <input v-model.number="newTask.time" type="number" placeholder="Estimated time (hours)" step="0.1" required />
      <button type="submit">Add Task</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: { name: '', priority: 1, time: 0.0 },
    };
  },
  methods: {
    addTask() {
      this.$emit('add-task', { ...this.newTask });
      this.newTask = { name: '', priority: 1, time: 0.0 };
    },
  },
};
</script>