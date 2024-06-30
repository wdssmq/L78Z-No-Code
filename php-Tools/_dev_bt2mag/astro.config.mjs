import { defineConfig } from 'astro/config'

import tailwind from '@astrojs/tailwind'

import curEnv from './env.config.mjs'

// https://astro.build/config
export default defineConfig({
    base: curEnv.base || '/',
    trailingSlash: 'never',
    outDir: curEnv.outDir || 'dist',
    integrations: [
        tailwind(),
    ],
})
