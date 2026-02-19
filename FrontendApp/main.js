const { app, BrowserWindow } = require('electron');

function createWindow () {
  // Membuat jendela browser (desktop window)
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  // Memuat file index.html ke dalam jendela
  win.loadFile('index.html');
}

// Saat Electron siap, jalankan fungsi createWindow
app.whenReady().then(createWindow);

// Menutup aplikasi sepenuhnya jika semua jendela disilang (X)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});