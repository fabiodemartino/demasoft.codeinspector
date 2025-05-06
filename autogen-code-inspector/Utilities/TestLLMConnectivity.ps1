# Update backend URL with the correct IP address of your server
$apiUrl = "http://10.0.0.135:5000/api/generate"  # Replace with your server's IP address

# Sample prompt to send to the LLM
$prompt = "Explain this code: function calculateSum(a, b) { return a + b; }"

# Prepare request body
$requestBody = @{
    model = "mistral"
    prompt = $prompt
    stream = $false
} | ConvertTo-Json

# Send request
$response = Invoke-RestMethod -Uri $apiUrl -Method Post -Body $requestBody -ContentType "application/json"

# Display the response
Write-Host "LLM Response: $($response.response)"
