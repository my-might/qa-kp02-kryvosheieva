*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Library    Process
Library    OperatingSystem

*** Variables ***
${path}    /Users/valeria/Documents/qa/qa-kp02-kryvosheieva/lab3/cli.py

*** Test Cases ***

User can create an new binary file with valid name
    Run Process    python3    ${path}    post    directory    root    CuteAnimals    100
    ${result} =    Run Process    python3    ${path}    post    binaryfile    root/CuteAnimals    Kitten    Mrrrrr
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to create a new binary file in the directory that does not exist
    ${result} =    Run Process    python3    ${path}    post    binaryfile    root/Lizzards    Kitten    Mrrrrr
    Should Contain    ${result.stdout}   Status code: 404

User should be able to find binary file
    Run Process    python3    ${path}    post    directory    root    CuteBirds    100
    ${result} =    Run Process    python3    ${path}    post    binaryfile    root/CuteBirds    Penguines    TipTop
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to find binary files that do not exist
    Run Process    python3    ${path}    post    directory    root    CuteSpiders    100
    ${result} =    Run Process    python3    ${path}    get    binaryfile    path\=root/CuteSpiders/Tarantul
    Should Contain    ${result.stdout}   Status code: 404

User should be able to move file to a different location
    Run Process    python3    ${path}    post    directory    root    CuteLizzards    100
    Run Process    python3    ${path}    post    directory    root    TerribleMonsters    100
    ${result} =    Run Process    python3    ${path}    post    binaryfile    root/CuteLizzards    Varan    Shhhhh
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    patch    binaryfile    move_from\=root/CuteLizzards/Varan    move_to\=root/TerribleMonsters
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    get    binaryfile    path\=root/CuteLizzards/Varan
    Should Contain    ${result.stdout}   Status code: 404

    ${result} =    Run Process    python3    ${path}    get    binaryfile    path\=root/TerribleMonsters/Varan
    Should Contain    ${result.stdout}   Status code: 200

User should be able to delete an existing file
    ${result} =    Run Process    python3    ${path}    post    binaryfile    root    Doggo    Bark
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    get    binaryfile    path\=root/Doggo
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    delete    binaryfile    path\=root/Doggo
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    get    binaryfile    path\=root/Doggo
    Should Contain    ${result.stdout}   Status code: 404