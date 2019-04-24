import { terser } from 'rollup-plugin-terser';
import typescript from "rollup-plugin-typescript";

const develop = process.env.ROLLUP_WATCH;

export default {
	input: 'src/main.ts',
	output: {
		file: 'static/script/main.min.js',
		format: 'esm',
		sourcemap: true
	},
	plugins: [
		typescript({removeComments: true}),
		!develop && terser(),  // minify in production
	]
};
