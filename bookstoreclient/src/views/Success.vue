<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>

        <p>Your order will be processed within 48 hours</p>
      </div>
    </div>
  </div>
</template>

<script>
import party from 'party-js'
export default {
  name: "Success",
  mounted() {
    party.screen()
    document.title = "Success | BookStore";
  },
};
</script>