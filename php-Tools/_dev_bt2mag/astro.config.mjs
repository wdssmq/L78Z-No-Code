import { defineConfig } from 'astro/config'

import tailwind from '@astrojs/tailwind'

// https://astro.build/config
export default defineConfig({
    base: '/tools/bt2mag',
    trailingSlash: 'never',
    integrations: [
        tailwind(),
    ],
})
