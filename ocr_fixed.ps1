# Load runtime assemblies
Add-Type -AssemblyName System.Runtime.WindowsRuntime

# Find the generic AsTask method for IAsyncOperation<T>
# Signature: public static Task<TResult> AsTask<TResult>(this IAsyncOperation<TResult> source)
$asTaskGeneric = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and 
    $_.IsGenericMethod -and 
    $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -match 'IAsyncOperation'
} | Select-Object -First 1

if ($null -eq $asTaskGeneric) {
    Write-Error "Could not find generic AsTask method!"
    exit 1
}

function Get-WinRTResult {
    param(
        $AsyncOp,
        $ResultType
    )
    
    # Create the generic method for the specific ResultType
    $concreteMethod = $asTaskGeneric.MakeGenericMethod($ResultType)
    
    # Invoke AsTask(AsyncOp) to get a Task
    $netTask = $concreteMethod.Invoke($null, @($AsyncOp))
    
    # Wait for completion (-1 means infinite timeout)
    $netTask.Wait(-1) | Out-Null
    
    # Return the Result property of the Task
    return $netTask.Result
}

# WinRT types
[void][Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]

$imagesDir = "C:\Users\Dell\Desktop\Saurabh\Madam-20260608T082228Z-3-001\Madam"
$outputFile = "C:\Users\Dell\Desktop\Saurabh\ocr_readable.txt"

$files = Get-ChildItem -Path $imagesDir -Filter "*.png"
$output = "OCR Results Native Fixed`n====================`n"

foreach ($file in $files) {
    $filePath = $file.FullName
    $output += "`n========================================`n"
    $output += "FILE: $($file.Name)`n"
    $output += "========================================`n"
    Write-Host "Processing $($file.Name)..."
    
    try {
        # 1. Get storage file async
        $asyncOpFile = [Windows.Storage.StorageFile]::GetFileFromPathAsync($filePath)
        $storageFile = Get-WinRTResult -AsyncOp $asyncOpFile -ResultType ([Windows.Storage.StorageFile])
        
        # 2. Open stream async
        $asyncOpStream = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read)
        $stream = Get-WinRTResult -AsyncOp $asyncOpStream -ResultType ([Windows.Storage.Streams.IRandomAccessStream])
        
        # 3. Create bitmap decoder async
        $asyncOpDecoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)
        $decoder = Get-WinRTResult -AsyncOp $asyncOpDecoder -ResultType ([Windows.Graphics.Imaging.BitmapDecoder])
        
        # 4. Get software bitmap async
        $asyncOpBitmap = $decoder.GetSoftwareBitmapAsync()
        $bitmap = Get-WinRTResult -AsyncOp $asyncOpBitmap -ResultType ([Windows.Graphics.Imaging.SoftwareBitmap])
        
        # 5. Recognize OCR
        $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
        if ($null -eq $engine) {
            $output += "[Error: Could not create OCR Engine]`n"
        } else {
            $asyncOpResult = $engine.RecognizeAsync($bitmap)
            $result = Get-WinRTResult -AsyncOp $asyncOpResult -ResultType ([Windows.Media.Ocr.OcrResult])
            
            if ([string]::IsNullOrWhiteSpace($result.Text)) {
                $output += "[No Text Found]`n"
            } else {
                $output += $result.Text + "`n"
            }
        }
    } catch {
        $output += "[Error processing: $_]`n"
        $output += "Stack: $($_.ScriptStackTrace)`n"
    }
}

Set-Content -Path $outputFile -Value $output -Encoding Utf8
Write-Host "Done! Results saved to $outputFile"
