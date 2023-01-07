*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Library    Process
Library    OperatingSystem

*** Variables ***
${path}    /Users/valeria/Documents/qa/qa-kp02-kryvosheieva/lab3/cli.py

*** Test Cases ***

User can create an new directory with valid name
    ${result} =    Run Process    python3    ${path}    post    directory    root    CuteAnimals    100
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to create directory inside directory that does not exists
    ${result} =    Run Process    python3    ${path}    post    directory    root/unexpected    CuteAnimals    100
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to create directory with negative max elements parameters
    ${result} =    Run Process    python3    ${path}    post    directory    root    CuteAnimals    -1
    Should Contain    ${result.stdout}   Status code: 400

User should be able to delete directory that exists
    Run Process    python3    ${path}    post    directory    root    Spiders    100
    ${result} =    Run Process    python3    ${path}    delete    directory    path\=root/Spiders
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to delete directory that does not exists
    ${result} =    Run Process    python3    ${path}    delete    directory    path\=root/unexisting
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to list files and subdirectories of the file that does not exist
    Run Process    python3    ${path}    post    directory    root    CuteAnimals    100
    ${result} =    Run Process    python3    ${path}    get    directory    path\=root/Spiders
    Should Contain    ${result.stdout}   Status code: 404

User should be able to move directory to a different location:
    Run Process    python3    ${path}    post    directory    root    CuteAnimals    100
    Run Process    python3    ${path}    post    directory    root    SchotishFold    100
    ${result} =    Run Process    python3    ${path}    patch    directory    move_from\=root/SchotishFold    move_to\=root/CuteAnimals
    Should Contain    ${result.stdout}   Status code: 200

User should not be able to move directory to a location that does not exist:
    Run Process    python3    ${path}    post    directory    root    SchotishFold    100
    ${result} =    Run Process    python3    ${path}    patch    directory    move_from\=root/SchotishFold    move_to\=root/Snakes
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to move not existing directory to a new location:
    Run Process    python3    ${path}    post    directory    root    SchotishFold    100
    ${result} =    Run Process    python3    ${path}    patch    directory    move_from\=root/Snakes    move_to\=root/SchotishFold
    Should Contain    ${result.stdout}   Status code: 404

User should be able to list files and subdirectories of the existing directory and directory should include only files inside this directory:
    Run Process    python3    ${path}    post    directory    root    AwesomeAnimals    100
    Run Process    python3    ${path}    post    directory    root/AwesomeAnimals    Cats    100
    Run Process    python3    ${path}    post    directory    root/AwesomeAnimals    BritishShorthair    100
    Run Process    python3    ${path}    post    directory    root/AwesomeAnimals    CuteAnimals    100
    ${result} =    Run Process    python3    ${path}    get    directory    path\=root/AwesomeAnimals
    Should Contain    ${result.stdout}   Status code: 200