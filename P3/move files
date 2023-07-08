$sourcePath = 'D:\DCIM\100OLYMP'
$destinationPath = 'C:\Users\cdreh\OneDrive\Desktop\camera'

# Check if the source folder exists
while (-not (Test-Path $sourcePath -PathType Container)) {
    # Wait for the source folder to become available
    Start-Sleep -Seconds 5
}

# Get the current date
$today = Get-Date -Format "yyyy-MM-dd"

# Create the destination folder if it doesn't exist
$destinationFolder = Join-Path $destinationPath $today
if (-not (Test-Path $destinationFolder -PathType Container)) {
    New-Item -ItemType Directory -Path $destinationFolder | Out-Null
}

# Move files from the source to the destination folder
Get-ChildItem $sourcePath | Move-Item -Destination $destinationFolder
