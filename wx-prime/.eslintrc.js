/*
 * Eslint config file
 * Documentation: https://eslint.org/docs/user-guide/configuring/
 * Install the Eslint extension before using this feature.
 */
module.exports = {
  env: {
    es6: true,
    browser: true,
    node: true,
  },
  ecmaFeatures: {
    modules: true,
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: "module",
  },
  globals: {
    wx: true,
    App: true,
    Page: true,
    getCurrentPages: true,
    getApp: true,
    Component: true,
    requirePlugin: true,
    requireMiniProgram: true,
  },
  // extends: 'eslint:recommended',
  rules: {
    "arrow-parens": 0,
    "generator-star-spacing": 0,
    "space-before-function-paren": 0,
    "comma-dangle": [1, "always-multiline"],
    "no-unused-vars": [1, { "args": "none" }],
    "spaced-comment": [2, "always"],
    "semi": [2, "always", { "omitLastInOneLineBlock": true }],
    "quotes": [2, "double"],
    // "no-debugger": process.env.NODE_ENV === "production" ? 2 : 0,},
  },
};
