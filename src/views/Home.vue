<template>
  <div class="home">
    <Dashboard/>
    <!-- <Table v-bind:todos="todos" v-on:del-todo="deleteTodo" />
    <Products/> -->
  </div>
</template>

<script>
// @ is an alias to /src
// import Table from "@/components/Table.vue";
import Dashboard from "@/components/Dashboard.vue";
// import Products from "@/views/Products.vue";


export default {
  name: "Home",
  components: {
    // Table,
    Dashboard,
    // Products
  },
  data: function() {
    return {
      todos: [
        { id: 1, title: "One", quantity: 3, price: 10.0 },
        { id: 2, title: "Two", quantity: 3, price: 10.0 },
        { id: 3, title: "Three", quantity: 3, price: 10.0 }
      ]
    };
  },
  methods: {
    deleteTodo(id){
      this.todos = this.todos.filter(todo => todo.id !== id);
    }
  }
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
}
</style>

