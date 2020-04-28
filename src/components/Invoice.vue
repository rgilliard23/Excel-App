<template>
  <div>
    <div class="col">
      <div class="row justify-content-between">
        <h1>Invoice</h1>
        <button
          type="button"
          class="btn btn-success"
          data-toggle="modal"
          data-target="#exampleModalCenter"
        >
          Add Products
        </button>
        <div class="dropdown">
          <div
            class="btn dropdown-toggle"
            type="button"
            id="dropdownMenu2"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            {{ customer.name }}
          </div>
          <div class="dropdown-menu" aria-labelledby="dropdownMenu2">
            <input
              type="text"
              class="dropdown-item form-control"
              placeholder="Search"
              v-model="searchCustomer"
              name="Search"
              id="dropDownSearch"
            />
            <div v-for="customer in filterCustomerList" :key="customer.id">
              <option @click="selectedCustomer(customer)" value="customer.id">
                {{ customer.name }}
              </option>
            </div>
          </div>
        </div>
      </div>

      <!--Table-->
      <table class="table table-hover" style="width:100%">
        <thead>
          <tr>
            <th>Items</th>
            <th>Quantity</th>
            <th>Total</th>
            <th></th>
          </tr>
        </thead>
        <tbody class="striped">
          <tr
            class="tableRow"
            v-for="(item, index) in invoice.items"
            :key="item.product.id"
          >
            <td>{{ item.product.name }}</td>
            <td>{{ item.quantity }}</td>
            <td>{{ item.quantity * item.product.price }}</td>
            <td>
              <button
                type="button"
                @click="deleteItem(index)"
                class="btn btn-danger"
              >
                Delete
              </button>
              <button
                type="button"
                class="btn btn-warning"
                data-toggle="modal"
                data-target="#exampleModalCenter"
              >
                Edit
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="row">
        <button class="btn btn-primary" @click="createInvoice">
          Create Invoice
        </button>
        <button>
          <json-excel :fields="fields" :data="invoice.items"></json-excel>
        </button>
      </div>

      <!-- //*Add Product Modal -->
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
                Add Products
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
                <div class="col">
                  <div class="form-group">
                    <label for="exampleFormControlSelect1"
                      >Search Products</label
                    >
                    <input
                      id="customerName"
                      class="form-control"
                      type="text"
                      placeholder="Search"
                      v-model="searchProduct"
                    />
                    <label for="exampleFormControlSelect1">Products</label>
                    <div class="mh-50 overflow-auto">
                      <table class="table table-striped ">
                        <thead>
                          <tr>
                            <th scope="col">Name</th>
                            <th scope="col">Price</th>
                            <th>Quantity</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr
                            class=""
                            v-for="product in filterProductList"
                            :key="product.id"
                          >
                            <td>{{ product.name }}</td>
                            <td>{{ product.price }}</td>
                            <td>
                              <button
                                type="button"
                                class="btn btn-primary"
                                data-toggle="modal"
                                data-target="#addProductModal"
                                @click="selectedProduct(product)"
                              >
                                Select Quantity
                              </button>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>

                  <!-- //* End of Table -->
                  <div class="row">
                    <button
                      type="button"
                      class="btn"
                      data-toggle="modal"
                      data-target="#addProductList"
                    >
                      View Product List
                    </button>
                  </div>
                </div>

                <!-- <button type="submit" value="submit" class="btn btn-primary" @click="addProducts">
                  Add Products
                </button> -->
              </form>
              <button v-on:click="addProducts">
                add
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- //* Add Quantity Modal -->

      <div
        class="modal fade"
        id="addProductModal"
        tabindex="-1"
        role="dialog"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
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
              <div class="form-group">
                <label for="productQuantity">Quantity</label>
                <input
                  v-model.number="quantity"
                  id="productQuantity"
                  class="form-control"
                  type="number"
                  step="1.0"
                  placeholder="1"
                  min="1"
                />
              </div>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                v-on:click="addProductToList"
              >
                Add Product To List
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- //*Add Product List -->
      <div
        class="modal fade"
        id="addProductList"
        tabindex="-1"
        role="dialog"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog modal-dialog-centered" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
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
              <ul>
                <li
                  class="list-group-item "
                  v-for="item in items"
                  :key="item.product.id"
                >
                  Product: {{ item.product.name }} | Quantity:
                  {{ item.quantity }}
                </li>
              </ul>
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-dismiss="modal"
              >
                Close
              </button>
              <button
                type="button"
                class="btn btn-primary"
                @click="addProductToList(product)"
              >
                Add Product To List
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import JsonExcel from "vue-json-excel";

const axios = require("axios");

const customerPath = "http://localhost:5000/api/customer";
const productPath = "http://localhost:5000/api/product";

export default {
  name: "Invoice",
  components: {
    JsonExcel
  },
  data: function() {
    return {
      fields: {
        Item: "product.name",
        Quantity: "quantity",
        "Unit Price": "product.price"
      },
      searchCustomer: "",
      searchProduct: "",
      customerId: "",
      quantity: 0,
      customers: [],
      products: [],
      items: [],
      invoices: [],
      product: {
        name: "",
        id: 0,
        price: "",
        description: ""
      },
      transaction: {
        quantity: 0,
        invoice_id: 0,
        product_id: 0
      },
      customer: {
        name: "Select Customer",
        id: 0,
        address: ""
      },

      invoice: {
        items: []
      },
      inv: {
        customer_id: 0,
        total: 0
      }
    };
  },
  methods: {
    date() {
      return new Date()
        .toJSON()
        .slice(0, 10)
        .replace(/-/g, "/");
    },
    getCustomers() {
      axios
        .get(customerPath)
        .then(res => {
          this.customers = res.data.customers;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    selectedCustomer(customer) {
      this.customer = customer;
    },
    selectedProduct(product) {
      this.product = product;
    },
    getProducts() {
      axios
        .get(productPath)
        .then(res => {
          this.products = res.data.products;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addProducts() {
      this.items.forEach(element => {
        if (this.invoice.items.length > 0) {
          this.invoice.items.forEach(invoiceItem => {
            if (invoiceItem.product.id === element.product.id) {
              invoiceItem.quantity += element.quantity;
            } else {
              this.invoice.items.push({
                product: element.product,
                quantity: element.quantity
              });
            }
          });
        } else {
          this.invoice.items.push({
            product: element.product,
            quantity: element.quantity
          });
        }
      });
    },
    addProductToList() {
      if (this.items.length > 0) {
        this.items.forEach(element => {
          if (this.product.id === element.product.id) {
            element.quantity += this.quantity;
            this.quantity = 0;
          } else {
            this.items.push({ product: this.product, quantity: this.quantity });
            this.quantity = 0;
          }
        });
      } else {
        this.items.push({ product: this.product, quantity: this.quantity });
        this.quantity = 0;
      }
    },
    deleteItem: function(index) {
      this.invoice.items.splice(index, 1);
    },
    createInvoice() {
      const invoicePath = "http://localhost:5000/api/invoice";
      const transactionPath = "http://localhost:5000/api/transaction";
      var invoiceID = 0;

      //let invoiceId = 0;
      var total = 0;
      this.inv.customer_id = this.customer.id;
      this.invoice.items.forEach(element => {
        total += element.quantity * element.product.price;
      });
      this.inv.total = total;
      axios
        .post(invoicePath, this.inv)
        .then(res => {
          console.log(res.data);
          this.getInvoices();
        })
        .catch(err => {
          console.log(err.data);
        });

      invoiceID = this.getInvoiceId();

      this.invoice.items.forEach(element => {
        this.transaction.quantity = element.quantity;
        this.transaction.product_id = element.product.id;
        this.transaction.invoice_id = invoiceID;

        axios
          .post(transactionPath, this.transaction)
          .then(res => {
            console.log(res.data);
          })
          .catch(err => {
            console.log(err.data);
          });
      });
    },
    getInvoiceId() {
      var temp = this.invoices.length - 1;
      var temp2 = this.invoices[temp].id;
      return temp2;
    },
    getInvoices() {
      const invoicePath = "http://localhost:5000/api/invoice";
      axios
        .get(invoicePath)
        .then(res => {
          this.invoices = res.data.invoices;
          console.log(res.data);
        })
        .catch(err => {
          console.log(err.data);
        });
    }
  },
  created() {
    this.getCustomers();
    this.getProducts();
    this.getInvoices();
  },

  computed: {
    getCustomerId() {
      return this.customer.id;
    },

    filterCustomerList() {
      return this.customers.filter(item => {
        return this.searchCustomer
          .toLowerCase()
          .split(" ")
          .every(v => item.name.toLowerCase().includes(v));
      });
    },
    filterProductList() {
      return this.products.filter(item => {
        return this.searchProduct
          .toLowerCase()
          .split(" ")
          .every(v => item.name.toLowerCase().includes(v));
      });
    }
  }
};
</script>

<style lang="stylus" scoped></style>
