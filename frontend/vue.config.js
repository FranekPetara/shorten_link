const path = require('path');

module.exports = {
  transpileDependencies: true,
  css: {
    loaderOptions: {
      sass: {
        implementation: require('sass'),
        sassOptions: {
          includePaths: [path.resolve(__dirname, './src/styles')]
        },
      },
    },
  },
};
