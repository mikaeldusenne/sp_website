module.exports = {
    assetsDir: './static',
    devServer: {
		proxy: 'http://sp_website_app_1:5000' // fill in flask docker image name !
    }
};
