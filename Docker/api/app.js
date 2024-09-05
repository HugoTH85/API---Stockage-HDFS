const express = require('express');
const WebHDFS = require('webhdfs');

const app = express();
const port = 3000;

app.use((req, res, next) => {
    res.removeHeader('Content-Security-Policy');
    next();
});

// Configure WebHDFS client
const hdfs = WebHDFS.createClient({
    user: 'hdfs',
    host: '0.0.0.0',  // Adresse du NameNode 172.23.0.0/16 et 172.23.0.3 pour le master
    port: 9870, // Replace with actual WebHDFS port
    path: '/webhdfs/v1'
});

// Route to fetch and serve the raw CSV file
app.get('/get-csv', (req, res) => {
    // Create a read stream for the file in HDFS
    const remoteFileStream = hdfs.createReadStream('/user/hadoop/student.csv');

    // Handle errors in the file stream
    remoteFileStream.on('error', (err) => {
        console.error('Error reading file:', err);
        res.status(500).send('Error retrieving CSV file');
    });

    // Set the appropriate Content-Type header for CSV files
    res.setHeader('Content-Type', 'text/csv');

    // Pipe the HDFS file stream directly to the HTTP response
    remoteFileStream.pipe(res);
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});