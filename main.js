const { app, BrowserWindow } = require("electron/main");
const { menubar } = require('menubar');
const path = require("node:path");

function createWindow() {
    const window = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, "preload.js"),
        },
    });

    window.loadFile("index.html");
    
}

const mb = menubar({
    browserWindow: {
        width: 400,
        height: 200,
        webPreferences: {
            preload: path.join(__dirname, "preload.js"),
        },
    },
    icon: path.resolve(__dirname, "menubarIconTemplate.png")
});

mb.on('ready', () => {
  console.log('app is ready');
  // your app code here
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") {
        app.quit();
    }
});
