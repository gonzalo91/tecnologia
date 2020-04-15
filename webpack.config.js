const path = require('path');


module.exports = {
    output: {
        path : path.resolve(__dirname, 'static/app/js'),
        filename : 'app.js',        
    },
    entry : {
        main : './resources/js/src/index.js'
    }

}