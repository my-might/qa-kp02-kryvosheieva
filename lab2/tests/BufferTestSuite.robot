*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Resource          BufferKeywords.resource
Resource          DirectoryKeywords.resource

*** Settings ***
Suite Setup       Reset
Test Teardown     Reset

*** Test Cases ***

User can create an new buffer with valid name
    Create Buffer    root    Awesome Animals    100
    Buffer Status Should Be    200

User should not be able to create buffer inside directory that does not exists
    Create Buffer    root/unexpected    Cute Animals    100
    Buffer Status Should Be    404

User should not be able to create buffer with negative max size parameters
    Create Buffer    root    Cute Animals    -1
    Buffer Status Should Be    400

User should be able to delete buffer that exists
    Create Buffer    root    Spiders    100
    Delete Buffer    root/Spiders
    Buffer Status Should Be    200

User should not be able to delete directory that does not exists
    Delete Buffer    root/unexisting
    Buffer Status Should Be    404

User should not be able to consume element of the empty file
    Create Buffer    root    Cute Animals    100
    Consume Existing Buffer    ${BASE_URL}    root/Cute Animals
    Buffer Status Should Be    404

User should be able to move buffer to a different location:
    Create Directory    root    Cute Lizzards    100
    Create Directory    root    Terrible Monsters    100
    Create Buffer     root/Cute Lizzards    Varan    100
    Buffer Status Should Be    200
    Move Buffer File    root/Cute Lizzards/Varan    root/Terrible Monsters
    Buffer Status Should Be    200

User should be able to put info to existing buffer:
    Create Buffer    root    Schotish Fold    100
    Put Existing Buffer    ${BASE_URL}    root/Scotish Fold    'info to put'
    Buffer Status Should Be    404

User should be able to consume element of the filled file
    Create Buffer    root    Beautiful Animals    100
    Put Existing Buffer    ${BASE_URL}    root/Beautiful Animals    'info to put'
    Expect Buffer Content    root/Beautiful Animals    'info to put'