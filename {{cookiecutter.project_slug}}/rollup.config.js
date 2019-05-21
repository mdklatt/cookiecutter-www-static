import fs from 'fs-extra';
import path from 'path';
import resolve from 'rollup-plugin-node-resolve'
import { terser } from 'rollup-plugin-terser'
import typescript from 'rollup-plugin-typescript'


const develop = process.env.ROLLUP_WATCH


/**
 * Plugin for copying static files to their output directory.
 *
 * @param options copy options
 * @returns
 */
const copy = function(options) {
    return {
        generateBundle() {
            const root = path.dirname(options.dest)
            fs.ensureDirSync(root)
            fs.copy(options.src, options.dest)
        }
    }
}


export default {
	input: 'src/script/main.ts',
	output: {
		file: 'static/script/main.js',
		format: 'esm',
		sourcemap: true
	},
	plugins: [
        copy({
            src:  'src/style/',
            dest: 'static/style/'
        }),
		typescript(),
		resolve(),  // locate packages in node_modules
		!develop && terser(),  // minify in production
	]
}
