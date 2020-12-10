import fs from 'fs'

const year = process.argv[3]
const day = process.argv[5]

const data = fs.readFileSync(process.stdin.fd, 'utf-8')

import(`./${year}/${day}`).then(({ run }) => run(data.split('\n')))
