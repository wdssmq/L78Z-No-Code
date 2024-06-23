import { defineConfig } from 'astro/config'

import tailwind from '@astrojs/tailwind'

// https://astro.build/config
export default defineConfig({
    base: '/test/bt2mag',
    trailingSlash: 'never',
    integrations: [
        tailwind(),
    ],
})
