const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let backendProcess;

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences:{
            nodeIntegration: false
        }
    });

    console.log('Loading file from:', path.join(__dirname, 'dist', 'index.html'));
    win.loadFile(path.join(__dirname, 'dist', 'index.html'));
}

// runs the backend server
function startBackend() {
    const backendPath = path.join(__dirname, '..', 'backend');

    // Start backend server using Poetry
    backendProcess = spawn(
        'poetry', 
        ['run', 'uvicorn', 'src.app:app', '--host', '127.0.0.1', '--port', '8000'],
        {
            cwd: backendPath,
            shell: true,
        }
    );

    backendProcess.stdout.on('data', (data) => {
        console.log(`[FastAPI]: ${data}`);
    });

    backendProcess.stderr.on('data', (data) => {
        console.log(`[FastAPI]: ${data}`);
    });

    backendProcess.on('close', (code) => {
        console.log(`[FastAPI]: process exited with code ${code}`);
    });

}

app.whenReady().then(() => {
    startBackend();
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('before-quit', () => {
    if (backendProcess){
        backendProcess.kill('SIGTERM');
    }
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        if(backendProcess) {
            backendProcess.kill('SIGTERM');
        }
        app.quit();
    }
});