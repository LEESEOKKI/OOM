<template>
  <div>
    <span>
    <h5>{{ article.id }}</h5>
    <p> 작성자 : {{ article.username }}</p>
    <p> 제목 : {{ article.title }}</p>
    <router-link :to="{ name: 'ArticleDetailView', params: { id: article.id } }">
      [상세보기]
    </router-link>
    </span>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object
  },
}
</script>

<style>

</style>