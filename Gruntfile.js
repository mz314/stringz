var
        js_src_files = [
            'static_files/src/js/*.js'
        ],
        less_files = [
            'static_files/src/less/*.less'
        ],
        js_tasks = [
            'jshint', 'concat', 'less'
        ];
        
        less_tasks = [
           'less'  
        ];

module.exports = function (grunt) {
    require('jit-grunt')(grunt);
    grunt.loadNpmTasks('grunt-contrib-jshint');

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        jshint: {
            files: {
                src: js_src_files
            }
        },
        less: {
            development: {
                files: {
                    "static_files/static/main.css": less_files
                }
            }
        },
        concat: {
            js: {
                options: {
                    separator: ';\n',
                    sourceMap: true
                },
                files: [
                    {
                        src: js_src_files,
                        dest: 'static_files/static/main.js'
                    }
                ]
            }
        },
        watch: {
            js: {
                files: js_src_files,
                tasks: js_tasks
            },
            less: {
                files: less_files,
                tasks: less_tasks
            }
        }
    });

    grunt.registerTask('default', js_tasks.concat(less_tasks));
};
