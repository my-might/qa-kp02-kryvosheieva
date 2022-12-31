*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Resource          DirectoryKeywords.resource
Resource          LogTextKeywords.resource

*** Test Cases ***
User should be able to create log text file
    Create Logtext File    root    LogtextTestCreate
    Logtext Status Should Be    200

User should be able to move file
    Create Directory    root    DirLogtextTestMove    100
    Create Logtext File    root    LogtextTestMove
    Move Logtext File    root/LogtextTestMove    root/DirLogtextTestMove
    Logtext Status Should Be    200
    Find Logtext File    root/LogtextTestMove
    Logtext Status Should Be    404
    Find Logtext File    root/DirLogtextTestMove/LogtextTestMove
    Logtext Status Should Be    200

User should be abble to append a line to the end of the file
    Create Logtext File    root    LogtextTestAppend
    Logtext Status Should Be    200
    Append Line To Logtext File    ${BASE_URL}    root/LogtextTestAppend    TestAppend
    Logtext Status Should Be    200
    Find Logtext File    root/LogtextTestAppend
    Logtext Content Should Be    TestAppend
    Logtext Status Should Be    200
    Append Line To Logtext File    ${BASE_URL}    root/LogtextTestAppend    /TestAppend2
    Find Logtext File    root/LogtextTestAppend
    Logtext Content Should Be    TestAppend/TestAppend2
    Logtext Status Should Be    200

User should be able to delete file
    Create Logtext File    root    LogtextTestDelete
    Logtext Status Should Be    200
    Find Logtext File    root/LogtextTestDelete
    Logtext Status Should Be    200
    Delete Logtext File    root/LogtextTestDelete
    Logtext Status Should Be    200
    Find Logtext File    root/LogtextTestDelete
    Logtext Status Should Be    404


User should not be able to delete not existing file
    Find Logtext File    root/LogtextTestDeleteNotExisting
    Logtext Status Should Be    404
    Delete Logtext File    root/LogtextTestDeleteNotExisting
    Logtext Status Should Be    404

User should be able to find log text file
    Create Logtext File    root    LogtextReadTest
    Find Logtext File    root/LogtextReadTest
    Logtext Status Should Be    200