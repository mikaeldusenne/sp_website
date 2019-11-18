module.exports = {
    assetsDir: './static',
    devServer: {
		host: '0.0.0.0',
		port: 8080,
		proxy: 'http://127.0.0.1:5000'
    }
};
