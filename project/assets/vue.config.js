function WebpackHooksPlugin(hooks) {
    this.hooks = hooks;
    this.options = {
        name: 'Webpack hooks plugin',
    };
}

WebpackHooksPlugin.prototype.apply = function (compiler) {
    let len = this.hooks.length;

    for (let i = 0; i < len; i++) {
        let hook = this.hooks[i];

        compiler.plugin(hook.name, hook.action);
    }
};

module.exports = {
    productionSourceMap: true,
    baseUrl: '/static/',
    outputDir: 'dist',
    assetsDir: undefined,
    runtimeCompiler: true,
    parallel: true,
    css: undefined,
    configureWebpack: config => {
        if (process.env.NODE_ENV === 'development') {
            let LiveReloadPlugin = require('webpack-livereload-plugin');

            if (!config.plugins)
                config.plugins = [];

            config.plugins.push(
                new WebpackHooksPlugin([
                    {
                        name: 'done',
                        action: (compiled) => {
                            console.log('\nHas been done');
                            let exec = require('child_process').exec;

                            exec("cd ../.. && ./django collectstatic --no-input", function (err, stdout, stderr) {
                                if (err) {
                                    console.log(`Collecting error: ${err}`);
                                    return;
                                }

                                let output = stdout.split('\n').filter(str => !!str);
                                console.log(output.pop());
                            });
                        }
                    }
                ]),
                new LiveReloadPlugin({
                    host: '127.0.0.1',
                    appendScriptTag: true,
                    delay: 1000,
                }),
            );
        }
    }
};