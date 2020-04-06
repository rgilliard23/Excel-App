<template>
  <div style="width: 100%;">
    <div class="row">
      <h1 class="Title">Dashboard</h1>
      <b-button v-b-modal.modal-1>Launch demo modal</b-button>
      <b-modal id="modal-1" title="BootstrapVue">
        <p class="my-4">Hello from modal!</p>
      </b-modal>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
  el: "#showModal",
  data: function() {},
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.Title {
  display: flex;
}
.addProduct {
  display: flex;
}
.row {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
</style>
