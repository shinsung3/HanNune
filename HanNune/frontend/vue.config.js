const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ]
})

module.exports = {
  configureWebpack: {
    output: {
      libraryExport: 'default'
    }
  }
}