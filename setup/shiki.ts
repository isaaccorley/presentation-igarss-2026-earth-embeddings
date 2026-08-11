import { defineShikiSetup } from '@slidev/types'

// The deck is white-paper everywhere (style.css forces --paper backgrounds),
// so always highlight with the light palette — even if the html element ends
// up with the `dark` class, vitesse-dark's pale ink is unreadable on cream.
export default defineShikiSetup(() => {
  return {
    themes: {
      dark: 'vitesse-light',
      light: 'vitesse-light',
    },
  }
})
