<template>
  <!-- <div class="book-wrapper"> -->
    <div
      class="column is-multiline"
    >
      <div class="card">
        <div class="card-image">
          <figure class="image is-2by3">
            <img
              v-bind:src="book.get_thumbnail"
              v-bind:alt="book.name"
              srcset=""
            />
          </figure>
        </div>
        <div class="card-content">
          <p class="tittle">
            {{ book.name }}
          </p>
          <p class="subtitle">
            {{ book.author_name }}
          </p>
        </div>
        <div class="card-footer">
          <div class="card-footer-item">
            <router-link v-bind:to="book.get_absolute_url">
              <button class="button is-light">View Details</button></router-link
            >
          </div>

          <p class="card-footer-item">
            <span class="has-text-grey"> Price {{ book.price }} </span>
          </p>
        </div>
      </div>
    </div>
  <!-- </div> -->
</template>

<script>
export default {
  name: "BookCards",
  props: {
    book: Object,
  },
};
</script>