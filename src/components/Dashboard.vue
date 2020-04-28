<template>
  <div style="width: 100%;" id="Dashboard">
    <div class="row">
      <!-- Sidebar -->
      <div class="col-2 sidebar">
        <h2>Dashboard</h2>
        <ul v-for="tab in tabs" v-bind:key="tab">
          <li v-on:click="currentTab = tab">{{ tab }}</li>
        </ul>
      </div>
      <!-- Main Content -->
      <div class="col-9">
        <keep-alive include="Products,Customer">
        <component v-bind:is="currentTabComponent"></component
        ></keep-alive>
      </div>
    </div>
  </div>
</template>

<script>
import Customer from "@/components/Customer.vue";
import Invoice from "@/components/Invoice.vue";
import Products from "@/views/Products.vue";

const axios = require("axios");
const path = "http://127.0.0.1:5000/product";
export default {
  name: "Dashboard",
  components: {
    Customer,
    Products,
    Invoice
  },
  data: function() {
    return {
      // showCustomers: true,
      // showProducts: true,
      currentTab: "Customer",
      tabs: ["Customer", "Products", "Invoice"],
      product: {
        name: "",
        price: 0,
        description: ""
      }
    };
  },
  created() {
    this.currentTabComponent();
  },
  computed: {
    currentTabComponent: function() {
      return this.currentTab;
    }
  },
  methods: {
    submitProduct() {
      axios
        .post(path, this.product)
        .then(res => {
          console.log(res.data);
        })
        .catch(error => {
          console.log(error.data);
        });
      console.log("Submitted Product");
    }
    // shopComponents(num){
    //     switch(num){
    //       case 1:
    //         showProducts: true;
    //         showCustomers: false;
    //         break;
    //       case 2:
    //         showCustomers: true;
    //         showProducts: false;
    //     }
    // }
  }
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
}

.Title {
  display: flex;
}
.addProduct {
  display: flex;
}
.sidebar {
  height: 100vh;
  background-color: #42b983;
  font-size: 12px;
}
</style>
