.<template>
  <div id="table">
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
          <tr class="tableRow" v-for="data in data" :key="data.id">
            <td>{{ data.id }}</td>
            <td>{{ data.name }}</td>
            <td>{{ data.address }}</td>
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

export default {
  el: "#table",
  data: function() {
    return {
        hello: "Hello",
    };
  },
  props: {
      data: [],

  }
};
</script>

<style></style>
