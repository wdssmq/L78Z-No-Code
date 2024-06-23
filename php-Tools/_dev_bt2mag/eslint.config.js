import globals from 'globals'
import pluginJs from '@eslint/js'
import tseslint from 'typescript-eslint'

import eslintPluginAstro from 'eslint-plugin-astro'

export default [
    {
        languageOptions: {
            globals: {
                ...globals.browser,
                ...globals.node,
            },
        },
    },
    pluginJs.configs.recommended,
    ...tseslint.configs.recommended,
    ...eslintPluginAstro.configs.recommended,
    {
        // 规则定义，按实际需要修改
        'rules': {
            // 缩进
            'indent': [
                'error',
                4,
                {
                    'SwitchCase': 1,
                },
            ],
            // 换行符
            'linebreak-style': [
                'error',
                'unix',
            ],
            // 引号
            'quotes': [
                'error',
                'single',
            ],
            // 分号
            'semi': [
                'error',
                'never',
            ],
            // 单行注释的空格
            'spaced-comment': [
                'error',
                'always',
                {
                    'line': {
                        // 继下述字符后再加空格
                        'markers': ['!', '#', '/'],
                    },
                },
            ],

            /* ---------------- */

            // 对象或数组的拖尾逗号
            // always-multiline 表示只有在多行时才需要拖尾逗号
            'comma-dangle': [
                1,
                'always-multiline',
            ],
            // 箭头函数参数括号
            // as-needed 表示只有在需要时才添加括号
            'arrow-parens': [
                1,
                'as-needed',
                {
                    // requireForBlockBody 表示在块体中需要括号
                    'requireForBlockBody': true,
                },
            ],
            // 变量声明后未使用
            // args: "none" 表示不检查函数参数是否被使用
            'no-unused-vars': [
                1,
                {
                    'args': 'none',
                },
            ],
            // 函数圆括号之前的空格
            // 分别对匿名函数、异步箭头函数、命名函数设置
            'space-before-function-paren': [
                1,
                {
                    'anonymous': 'never',
                    'asyncArrow': 'always',
                    'named': 'never',
                },
            ],

        },
    },
]
