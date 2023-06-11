const { compile } = require("html-to-text")
const { promises: fsPromise } = require('fs')

const options = {
  wordwrap: 130,
  // ...
};

const compiledConvert = compile(options)


async function main() {
  const files = await fsPromise.readdir("dist/html")
  await Promise.all(files.filter(f => /\.html$/.test(f)).map(async filename => {
    const htmlPath = `dist/html/${filename}`
    const html = await fsPromise.readFile(htmlPath, 'utf8')
    const textPath = htmlPath.replace(/\.html$/, '.txt').replace(/^dist\/html/, 'dist/text')
    const text = compiledConvert(html)
    await fsPromise.writeFile(textPath, text)
    console.error(`finished: ${htmlPath} => ${textPath}`)
  }))
}

main()
