[void][Windows.Media.Ocr.OcrEngine, Windows.Media.Ocr, ContentType=WindowsRuntime]
[void][Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType=WindowsRuntime]
[void][Windows.Storage.StorageFile, Windows.Storage, ContentType=WindowsRuntime]

$imagesDir = "C:\Users\Dell\Desktop\Saurabh\Madam-20260608T082228Z-3-001\Madam"
$outputFile = "C:\Users\Dell\Desktop\Saurabh\ocr_results_native.txt"

$files = Get-ChildItem -Path $imagesDir -Filter "*.png"

$output = "OCR Results Native`n====================`n"

foreach ($file in $files) {
    $filePath = $file.FullName
    $output += "`n========================================`n"
    $output += "FILE: $($file.Name)`n"
    $output += "========================================`n"
    
    try {
        $storageFile = [Windows.Storage.StorageFile]::GetFileFromPathAsync($filePath).GetResults()
        $stream = $storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read).GetResults()
        $decoder = [Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream).GetResults()
        $bitmap = $decoder.GetSoftwareBitmapAsync().GetResults()
        $engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
        
        if ($null -eq $engine) {
            $output += "[Error: Could not create OCR Engine]`n"
        } else {
            $result = $engine.RecognizeAsync($bitmap).GetResults()
            if ([string]::IsNullOrWhiteSpace($result.Text)) {
                $output += "[No Text Found]`n"
            } else {
                $output += $result.Text + "`n"
            }
        }
    } catch {
        $output += "[Error processing: $_]`n"
    }
}

Set-Content -Path $outputFile -Value $output -Encoding Utf8
Write-Output "OCR Done! Results saved to $outputFile"
