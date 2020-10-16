# martingale-sim
Some python martingale simulation scripts



# Software
* [NodeJS](https://nodejs.org/en/)
* [MongoDB](https://www.mongodb.com/try/download/community)
# Code
## Initialization
`npm init`
## Dependencies
### Main
* [Mongoose](https://mongoosejs.com/)
* [Parse5](https://github.com/inikulin/parse5)
* [Typescript](https://www.typescriptlang.org/)
### Installation Commands
`npm install mongoose parse5`

`npm install -D nodemon typescript ts-node @types/mongoose @types/node @types/parse5`

`npm i -g typescript ts-node`

`tsc --init`

## Configuration
### package.json
Edit "main": to point to "src/app.ts"

`"main": "src/app.ts",`

Add "dev" script

`"dev": "nodemon src/app.ts"`

### tsconfig.json

`{
	"compilerOptions": {
		"target": "es6",
		"module": "commonjs",
		"outDir": "./dist",
		"allowSyntheticDefaultImports": true,
		"esModuleInterop": true
	},
	"include": ["src"],
}`

## Run
Run the dev script, which will insert the sessions into the monitor

`npm run dev` 
