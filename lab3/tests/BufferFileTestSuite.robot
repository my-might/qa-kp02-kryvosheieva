*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Library    Process
Library    OperatingSystem

*** Variables ***
${path}    /Users/valeria/Documents/qa/qa-kp02-kryvosheieva/lab3/cli.py

*** Test Cases ***

User can create an new buffer with valid name
    ${result} =    Run Process    python3    ${path}    post    bufferfile    root    AwesomeAnimals    100
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to create buffer inside directory that does not exists
    ${result} =    Run Process    python3    ${path}    post    bufferfile    root/unexpected    CuteAnimals    100
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to create buffer with negative max size parameters
    ${result} =    Run Process    python3    ${path}    post    bufferfile    root    CuteAnimals    -1
    Should Contain    ${result.stdout}   Status code: 400

User should be able to delete buffer that exists
    Run Process    python3    ${path}    post    bufferfile    root    Spiders    100
    ${result} =    Run Process    python3    ${path}    delete    bufferfile    path\=root/Spiders
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to delete directory that does not exists
    ${result} =    Run Process    python3    ${path}    delete    bufferfile    path\=root/unexisting
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to consume element of the empty file
    Run Process    python3    ${path}    post    bufferfile    root    CuteAnimals    100
    ${result} =    Run Process    python3    ${path}    get    bufferfile    path\=root/CuteAnimals
    Should Contain    ${result.stdout}   Status code: 404

User should be able to move buffer to a different location:
    Run Process    python3    ${path}    post    directory    root    CuteLizzards    100
    Run Process    python3    ${path}    post    directory    root    TerribleMonsters    100
    ${result} =    Run Process    python3    ${path}    post    bufferfile    root/CuteLizzards    Varan    100
    Should Contain    ${result.stdout}   Status code: 200
    
    ${result} =    Run Process    python3    ${path}    patch    bufferfile    move_from\=root/CuteLizzards/Varan    move_to\=root/TerribleMonsters
    Should Contain    ${result.stdout}   Status code: 200

User should be able to consume element of the filled file
    Run Process    python3    ${path}    post    bufferfile    root    BeautifulAnimals    100
    Run Process    python3    ${path}    put    bufferfile    root/BeautifulAnimals    'info to put'
    ${result} =    Run Process    python3    ${path}    get    bufferfile    path\=root/BeautifulAnimals
    Should Contain    ${result.stdout}   info to put