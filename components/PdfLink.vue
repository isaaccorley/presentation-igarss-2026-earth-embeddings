<script setup>
// Quiet "View as PDF" button for the title slide. Links to the static
// PDF shipped in public/; hidden in the PDF export itself.
const base = import.meta.env.BASE_URL
const isPrint =
  typeof window !== 'undefined' && window.location.search.includes('print')
</script>

<template>
  <a
    v-if="!isPrint"
    :href="`${base}earth-embeddings-igarss2026.pdf`"
    class="pdf-link"
  >
    View as PDF
  </a>
</template>
