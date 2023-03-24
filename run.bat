::cooments
::unzip"./langs/zip/python-3.10.8-embed-amd64" "./langs/python"

set zipPath=%cd%\langs\zips
set pythonPath=%cd%\langs\python\python.exe
set zipExtractor=%cd%\modules\7-Zip\7z.exe

if exist "%zipPath%\*.zip" (
    set /p choice="Zip file found in zips folder. Extract to python folder? (Y/N)"
    if /i "%choice%"=="Y" (
        for %%i in ("%zipPath%\*.zip") do (
            start %zipExtractor% x "%%i" -o"%pythonPath%" -y
            echo "Extraction complete."
        )
    ) else (
        echo "Extraction cancelled."
    )
) else (
    echo "Zip file not found in zips folder."
)

echo "%zipPath%"
echo "%pythonPath%"
echo %cd%
%pythonPath% ./progInit.py