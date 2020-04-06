<template>
  <div>
    <h1 id="example">{{ hello }}</h1>
     <b-table  striped hover :items="data" :fields="fields"></b-table>
    <table class="table table-striped table-hover" style="width:100%">
      <thead>
        <tr>
          <th>Product Name</th>
          <th>Quantity</th>
          <th>Price</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody class="striped">
        <tr class="tableRow" v-bind:key="todo.id" v-for="todo in todos">
          <td>{{ todo.title }}</td>
          <td>{{ todo.quantity }}</td>
          <td>{{ todo.price }}</td>
          <td>
            <button
              class="deleteButton btn btn-danger"
              @click="$emit('del-todo', todo.id)"
            >
              Delete
            </button>
          </td>
        </tr>
        <tr class="tableRow"  v-for="customer in data" :key="customer.id">
          <td>{{customer.id}}</td>
          <td>{{customer.name}}</td>
          <td>{{customer.address}}</td>
          <td>
            <button
              class="deleteButton btn btn-danger"
              @click="$emit('del-todo', todo.id)"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
const axios = require("axios");

export default {
  name: "Table",
  el: "#example",
  methods: {
    //* gets all customers
    getCustomers() {
      const path = "http://localhost:5000/customer";
      axios
        .get(path)
        .then((res) => {
          this.data = res.data.customers;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  //* Calls function on load
  created() {
    this.getCustomers();  
  },
  data: function() {
    return {
      fields: [
        'name', 'address', 'id'],
      data: [],
      hello: "Hello World!",
    };
  },
  props: ["todos"],
};
</script>

<style>
.deleteButton {
  opacity: 0;
}

.tableRow:hover .deleteButton {
  opacity: 100;
}
</style>
