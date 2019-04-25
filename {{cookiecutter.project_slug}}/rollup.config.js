import { terser } from 'rollup-plugin-terser'
import typescript from 'rollup-plugin-typescript'
import resolve from 'rollup-plugin-node-resolve'

const develop = process.env.ROLLUP_WATCH

export default {
	input: 'src/main.ts',
	output: {
		file: 'static/script/main.min.js',
		format: 'esm',
		sourcemap: true
	},
	plugins: [
		typescript(),
		resolve(),  // locate packages in node_modules
		!develop && terser(),  // minify in production
	]
};
