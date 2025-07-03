const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const kill = require('tree-kill');

let backendProcess;

function createWindow() {
    win = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences:{
            nodeIntegration: false,
            contextIsolation: true
        }
    });

    win.loadFile(path.join(__dirname, 'dist', 'index.html'));

    win.on('closed', () => {
        win = null;
    });
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
            shell: true
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


// kills the backend server
function stopBackend() {
    if (backendProcess) {
        kill(backendProcess.pid, 'SIGTERM', (err) => {
            if (err) {
                console.error('Failed to kill backend process:', err);
            } else {
                console.log('Backend process terminated');
            }
        });
        backendProcess = null;
    }
}

// starts the backend and opens the app window
app.whenReady().then(() => {
    startBackend();
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});


// these will ensure the server is killed when the window is closed
app.on('before-quit', stopBackend);

app.on('window-all-closed', () => {
    stopBackend();
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('quit', stopBackend);