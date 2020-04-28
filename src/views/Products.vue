<template>
  <div id="productTable">
    <div class="col">
      <div class="row justify-content-between">
        <h1>Products</h1>
        <button
          type="button"
          class="btn btn-info"
          data-toggle="modal"
          data-target="#exampleModalCenter"
        >
          Add Product
        </button>
      </div>
      <table class="table table-striped table-hover" style="width: 100;">
        <thead>
          <tr>
            <th>Product ID</th>
            <th>Product Name</th>
            <th>Product Description</th>
            <th>Product Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody class="striped">
          <tr class="tableRow" v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.description }}</td>
            <td>{{ product.price }}</td>
            <td>
              <button
                class="deleteButton btn btn-danger"
                @click="deleteProduct(product.id)"
              >
                Delete
              </button>
              <button
                type="button"
                class="btn btn-warning"
                data-toggle="modal"
                data-target="#exampleModalCenter"
                @click="editProduct(product)"
              >
                Edit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="modal fade" id="exampleModalCenter">
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title">
                Add New Product
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
                      <label for="customerName">Product Name</label>
                      <input
                        v-model="product.name"
                        id="customerName"
                        class="form-control"
                        type="text"
                        placeholder="Name"
                      />
                    </div>
                  </div>
                  <div class="col">
                    <div class="form-group">
                      <label for="customerAddress">Product Price</label>
                      <input
                        v-model="product.price"
                        class="form-control"
                        type="number"
                        step="0.10"
                        name="productName"
                        id="productName"
                        placeholder="0"
                      />
                    </div>
                  </div>
                </div>
                <div class="form-group">
                  <label for="exampleFormControlTextarea1"
                    >Example textarea</label
                  >
                  <textarea
                    v-model="product.description"
                    class="form-control"
                    id="exampleFormControlTextarea1"
                    rows="3"
                  ></textarea>
                </div>
                <button
                  type="submit"
                  v-on:click="submitProduct"
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
const path = "http://localhost:5000/api/product";

export default {
  name: "product",
  methods: {
    //* gets all products
    getProducts() {
      axios
        .get(path)
        .then(res => {
          this.products = res.data.products;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submitProduct() {
        if(this.edit){
        axios
        .put(path + "/" + this.product.id, this.product)
        .then(res => {
          console.log(res.data);
        })
        .catch(error => {
          console.log(error.data);
        });
      this.$emit("currentTab", "Product");
      console.log("Submitted Product");
      this.edit = false;
        }else{
            axios
        .post(path, this.product)
        .then(res => {
          console.log(res.data);
        })
        .catch(error => {
          console.log(error.data);
        });
      this.$emit("currentTab", "Product");
      console.log("Submitted Product");
        }
      
    },
    editProduct(product) {
      this.product = product;
      this.edit = true;
    },
    deleteProduct: function(productID) {
      axios
        .delete(path + "/" + productID)
        .then(res => {
          console.log(res.data);
          this.getProducts();
        })
        .catch(error => {
          console.log(error.data);
        });
    }
  },

  data: function() {
    return {
      edit: false,
      products: [],
      product: {
        id: 0,
        name: "",
        price: 0,
        description: ""
      }
    };
  },
  created() {
    this.getProducts();
  }
};
</script>

<style>
* {
  padding: 0;
  margin: 0;
}
</style>
