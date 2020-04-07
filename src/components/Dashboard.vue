<template>
  <div style="width: 100%;">
    <div class="row">
      <h1 class="Title">Dashboard</h1>
      <div>
        <!-- Button trigger modal -->
        <button
          type="button"
          class="btn btn-primary"
          data-toggle="modal"
          data-target="#exampleModalCenter"
        >
          Launch demo modal
        </button>

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
                        <label for="productName">Product Name</label>
                        <input
                          v-model ="productName"
                          id="productName"
                          class="form-control"
                          type="text"
                          placeholder="Default input"
                        />
                      </div>
                    </div>
                    <div class="col">
                      <div class="form-group">
                        <label for="exampleInputPassword1">Price</label>
                        <input v-model ="productPrice" class="form-control" type="number" step="0.10" />
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="description">Description</label>
                    <textarea
                      v-model = "productDescription"
                      class="form-control"
                      id="description"
                      rows="3"
                      maxlength = "200"
                    ></textarea>
                  </div>
                  <button type="submit" class="btn btn-primary">Submit</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  data: function() {
    return {
    productName: '',
    productPrice: '',
    productDescription: ''
    }
    
  }
};
</script>

<style>
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
.row {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  width: 100%;
}
</style>
