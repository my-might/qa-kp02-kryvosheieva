*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Library    Process
Library    OperatingSystem

*** Variables ***
${path}    /Users/valeria/Documents/qa/qa-kp02-kryvosheieva/lab3/cli.py

*** Test Cases ***

User should be able to create log text file
    ${result} =    Run Process    python3    ${path}    post    logtextfile    root    LogtextTestCreate
    Should Contain    ${result.stdout}   Status code: 200

User should be able to move file
    Run Process    python3    ${path}    post    directory    root    DirLogtextTestMove    100
    Run Process    python3    ${path}    post    logtextfile    root    LogtextTestMove
    ${result} =    Run Process    python3    ${path}    patch    logtextfile    move_from\=root/LogtextTestMove    move_to\=root/DirLogtextTestMove
    Should Contain    ${result.stdout}   Status code: 200
    
    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextTestMove
    Should Contain    ${result.stdout}   Status code: 404

    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/DirLogtextTestMove/LogtextTestMove
    Should Contain    ${result.stdout}   Status code: 200

User should be abble to append a line to the end of the file
    ${result} =    Run Process    python3    ${path}    post    logtextfile    root    LogtextTestAppend
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    put    logtextfile    root/LogtextTestAppend    TestAppend

    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextTestAppend
    Should Contain    ${result.stdout}   Status code: 200
    Should Contain    ${result.stdout}   TestAppend

User should be able to delete file
    ${result} =    Run Process    python3    ${path}    post    logtextfile    root    LogtextTestDelete
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextTestDelete
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    delete    logtextfile    path\=root/LogtextTestDelete
    Should Contain    ${result.stdout}   Status code: 200

    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextTestDelete
    Should Contain    ${result.stdout}   Status code: 404

User should not be able to delete not existing file
    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextTestDeleteNotExisting
    Should Contain    ${result.stdout}   Status code: 404

    ${result} =    Run Process    python3    ${path}    delete    logtextfile    path\=root/LogtextTestDeleteNotExisting
    Should Contain    ${result.stdout}   Status code: 404

User should be able to find log text file
    Run Process    python3    ${path}    post    logtextfile    root    LogtextReadTest
    ${result} =    Run Process    python3    ${path}    get    logtextfile    path\=root/LogtextReadTest
    Should Contain    ${result.stdout}   Status code: 200