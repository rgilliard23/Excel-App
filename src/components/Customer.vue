<template>
  <div id="customerTable">
    <div class="col">
      <div class="row justify-content-between">
        <h1>Customer</h1>
        <button
          type="button"
          class="btn btn-info"
          data-toggle="modal"
          data-target="#exampleModalCenter"
        >
          Add Customer
        </button>
      </div>
      <table class="table table-striped table-hover" style="width:100%">
        <thead>
          <tr>
            <th>Customer ID</th>
            <th>Customer Name</th>
            <th>Address</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody class="striped">
          <tr class="tableRow" v-for="customer in customers" :key="customer.id">
            <td>{{ customer.id }}</td>
            <td>{{ customer.name }}</td>
            <td>{{ customer.address }}</td>
            <td>
              <button
                type="button"
                class="btn btn-danger"
                @click="deleteCustomer(customer)"
              >
                Delete
              </button>
              <button
                type="button"
                class="btn btn-warning"
                data-toggle="modal"
                data-target="#exampleModalCenter"
                @click="editCustomer(customer)"
              >
                Edit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <!-- Modal -->
      <div
        class="modal fade"
        id="exampleModalCenter"
        tabindex="-1"
        role="dialog"
        aria-labelledby="exampleModalCenterTitle"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLongTitle">
                Add New Customer
              </h5>
              <button
                type="button"
                class="close"
                data-dismiss="modal"
                aria-label="Close"
              >
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            <div class="modal-body">
              <form>
                <div class="row">
                  <div class="col">
                    <div class="form-group">
                      <label for="customerName">Customer Name</label>
                      <input
                        v-model="customer.name"
                        id="customerName"
                        class="form-control"
                        type="text"
                        placeholder="Name"
                      />
                    </div>
                  </div>
                  <div class="col">
                    <div class="form-group">
                      <label for="customerAddress">Customer Address</label>
                      <input
                        v-model="customer.address"
                        id="customerAddress"
                        class="form-control"
                        type="text"
                        placeholder="Address"
                      />
                    </div>
                  </div>
                </div>
                <button
                  type="submit"
                  v-on:click="submitCustomer"
                  value="submit"
                  class="btn btn-primary"
                >
                  Submit
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");
const path = "http://localhost:5000/api/customer";

export default {
  name: "Customer",
  methods: {
    //* gets all customers
    getCustomers() {
      axios
        .get(path)
        .then(res => {
          this.customers = res.data.customers;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submitCustomer() {
      if(this.edit){
        axios.put(path + "/" + this.customer.id, this.customer)
        .then(res => {
          console.log(res.data);
        }).catch(err => {
          console.log(err.data);
        });
        this.edit = false;
      }else{
        axios
        .post(path, this.customer)
        .then(res => {
          console.log(res.data);
          this.getCustomers();
        })
        .catch(error => {
          console.log(error.data);
        });
      console.log("Submitted Product");
      }
      
      
    },
    editCustomer(customer){
      this.customer = customer;
      this.edit = true;
      
    },
    deleteCustomer(customer){
      axios.delete(path + "/" + customer.id)
      .then(res => {
        console.log(res.data);
        this.getCustomers();
      }).catch(err => {
        console.log(err.data);
      })
    }
  },
  //* Calls function on load
  created() {
    this.getCustomers();
  },
  data: function() {
    return {
      edit: false,
      customers: [],
      customer: {
        name: "",
        address: ""
      }
    };
  }
};
</script>

<style scoped>
.deleteButton {
  opacity: 0;
}
.row {
  margin-bottom: 1%;
}
.tableRow:hover .deleteButton {
  opacity: 100;
}
</style>
