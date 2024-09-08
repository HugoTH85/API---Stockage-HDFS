from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS
from pyspark_job import read_csv_from_hdfs

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Endpoint to trigger the PySpark job
@app.route('/read-csv.csv', methods=['GET'])
def get_csv_data():
    try:
        # Path to your file on HDFS
        hdfs_file_path = "student.csv"
        
        # Call the PySpark job to read CSV from HDFS
        result = read_csv_from_hdfs(hdfs_file_path)

        # Return the result as JSON
        return result

    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
