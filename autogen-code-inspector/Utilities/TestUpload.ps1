# Define the path to the file you want to upload
$filePath = "C:\temp\test.txt"  # Path to the test.txt file

# Define the URL for the Flask backend upload endpoint
$url = "http://10.0.0.135:5000/upload"

# Check if the file exists before attempting to upload
if (Test-Path $filePath) {
    # Run the curl command to upload the file
    curl.exe -X POST -F "file=@$filePath" $url
} else {
    Write-Host "The file does not exist at the specified path: $filePath"
}
