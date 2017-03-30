: The script assumes nothing already installed other than Anaconda 3
: "snakepit" - Installs: tensorflow, keras, scikit-learn, jupyter


conda create -n snakepit python=3.5 --y
call activate snakepit

pip install --upgrade tensorflow
:: Install keras 2.0.2 see 
:: use " anaconda search -t conda keras " to find other versions
pip install scikit-learn
pip install matplotlib
pip install jupyter


@echo off

set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\snakepit.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "python" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%

call deactivate snakepit
ECHO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ECHO Set desktop shortcut "snakepit" as python interpreter in your Python IDE
PAUSE