const path = require('path');

module.exports = {
  entry: path.join(__dirname, 'src', 'javascript', 'app.js'),
  output: {
    path: path.join(__dirname, 'public', 'js'),
    filename: 'main.js',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.s[ac]ss$/i,
        use: ['style-loader', 'css-loader', 'sass-loader'],
      },
    ],
  },
};
