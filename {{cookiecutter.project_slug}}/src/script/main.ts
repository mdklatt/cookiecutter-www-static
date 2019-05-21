/**
 * Define the greeting text in index.html.
 *
 * @param name - name to use for greeting
 */
export function hello(name="World") {
    document.querySelector("#greeting").innerHTML = "Hello, " + name
    return
}
