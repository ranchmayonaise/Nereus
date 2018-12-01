const electron = require("electron")  
const {app, BrowserWindow} = electron 

app.on("ready", () => {
  const {width, height} = electron.screen.getPrimaryDisplay().workAreaSize
  win = new BrowserWindow({
  	titleBarStyle: "hiddenInset", 
  	width: width/1.2,
  	height: height/1.3,
  })
  win.loadFile("index.html")
})
