const fs = require('fs')

const tweets = JSON.parse(fs.readFileSync('trump.json'))
console.log(`parsed ${tweets.length} tweets`)

const text = tweets.map((t) => {
  return t.text.replace(/(?:https?):\/\/[\n\S]+/g, '').replace(/\.{2,}/g,'.')
})
fs.writeFile('trump.txt', text.join(' '), (err) => {
  if (err) {
    console.log(err)
  }
  console.log('wrote trump.txt')
})
