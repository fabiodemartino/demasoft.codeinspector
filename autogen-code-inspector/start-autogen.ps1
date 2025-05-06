# Step 1: Load environment variables from .env
Set-Location $PSScriptRoot
$envFile = ".env"

if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        $line = $_.Trim()
        if ($line -and !$line.StartsWith('#')) {
            $parts = $line -split '=', 2
            if ($parts.Length -eq 2) {
                $envName = $parts[0].Trim()
                $envValue = $parts[1].Trim()
                [System.Environment]::SetEnvironmentVariable($envName, $envValue, [System.EnvironmentVariableTarget]::Process)
            }
        }
    }
    Write-Host "Environment variables loaded successfully from .env file.`n"
} else {
    Write-Host "The .env file does not exist at path $envFile"
    exit 1
}
 
# Step 2: Start Docker Compose stack
Write-Host "Starting Docker Compose stack..."
docker compose --env-file .env up -d 

Write-Host "autogen-code-inspector stack is running."
