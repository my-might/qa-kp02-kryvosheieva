*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Resource          DirectoryKeywords.resource

*** Settings ***
Suite Setup       Reset
Test Teardown     Reset

*** Test Cases ***

User can create an new directory with valid name
    Create Directory    root    Cute Animals    100
    Status Should Be    200

User should not be able to create directory inside directory that does not exists
    Create Directory    root/unexpected    Cute Animals    100
    Status Should Be    404

User should not be able to create directory with negative max elements parameters
    Create Directory    root    Cute Animals    -1
    Status Should Be    400

User should be able to delete directory that exists
    Create Directory    root    Spiders    100
    Delete Directory    root/Spiders
    Status Should Be    200

User should not be able to delete directory that does not exists
    Delete Directory    root/unexisting
    Status Should Be    404

User should not be able to list files and subdirectories of the file that does not exist
    Create Directory    root    Cute Animals    100
    List Existing Directory    ${BASE_URL}    root/Spiders
    Status Should Be    404

User should be able to move directory to a different location:
    Create Directory    root    Cute Animals    100
    Create Directory    root    Schotish Fold    100
    Move Directory To New Folder    ${BASE_URL}    root/Schotish Fold    root/Cute Animals
    Status Should Be    200

User should not be able to move directory to a location that does not exist:
    Create Directory    root    Schotish Fold    100
    Move Directory To New Folder    ${BASE_URL}    root/Schotish Fold    root/Snakes
    Status Should Be    404

User should not be able to move not existing directory to a new location:
    Create Directory    root    Schotish Fold    100
    Move Directory To New Folder    ${BASE_URL}    root/Snakes    root/Schotish Fold
    Status Should Be    404

User should be able to list files and subdirectories of the existing directory and directory should include only files inside this directory:
    Create Directory    root    Awesome Animals    100
    Create Directory    root/Awesome Animals    Cats    100
    Create Directory    root/Awesome Animals    British Shorthair    100
    Create Directory    root/Awesome Animals    Snakes    100
    Expect Directory Content    root/Awesome Animals    ['Cats', 'British Shorthair', 'Snakes']
