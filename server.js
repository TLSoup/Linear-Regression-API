const {spawn} = require('child_process');
const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

app.get("/", (req, res) => {
   
    var largeDataSet = [];
    // spawn new child process to call the python script
    const python = spawn('python', ['linear-regression.py']);
    // collect data from script
    python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    largeDataSet.push(data);
    });
    // in close event we are sure that stream is from child process is closed
    python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    // send data to browser
    res.send(largeDataSet.join(""))
    });
})

app.listen(PORT, () => {
    console.log(`Server is running on port:${PORT}...`);
});