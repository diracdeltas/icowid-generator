const fs = require('fs')

const tweets = JSON.parse(fs.readFileSync('trump.json'))
const tweets2 = JSON.parse(fs.readFileSync('trump2021.json'))

const all = tweets.concat(tweets2)
console.log(`parsed ${all.length} tweets`)

const text = all.map((t) => {
  return t.text.replace(/(?:https?):\/\/[\n\S]+/g, '').replace(/\.{2,}/g, '.')
})
fs.writeFile('trump.txt', text.join(' '), (err) => {
  if (err) {
    console.log(err)
  }
  console.log('wrote trump.txt')
})
