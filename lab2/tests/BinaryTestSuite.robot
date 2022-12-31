*** Settings ***
Documentation     A test suite for valid login.
...
...               Keywords are imported from the resource file
Resource          BinaryKeywords.resource
Resource          DirectoryKeywords.resource

*** Test Cases ***
User can create an new binary file with valid name
    Create Directory    root    Cute Animals    100
    Create Binary File     Kitten    root/Cute Animals    Mrrrrr
    Binary File Has Content Equal To    root/Cute Animals/Kitten    Mrrrrr

User should not be able to create a new binary file in the directory that does not exist
    Create Binary File     Kitten    root/Lizzards    Mrrrrr
    Binary Status Should Be    404

User should be able to find binary file
    Create Directory    root    Cute Birds    100
    Create Binary File     Penguines    root/Cute Birds    Tip Top
    Binary File Has Content Equal To    root/Cute Birds/Penguines    Tip Top

User should not be able to find binary files that do not exist
    Create Directory    root    Cute Spiders    100
    Find Existing Binary File    root/Cute Spiders/Tarantul
    Binary Status Should Be    404

User should be able to move file to a different location
    Create Directory    root    Cute Lizzards    100
    Create Directory    root    Terrible Monsters    100
    Create Binary File     Varan    root/Cute Lizzards    Shhhhh
    Binary Status Should Be    200
    Move Binary File    root/Cute Lizzards/Varan    root/Terrible Monsters
    Binary Status Should Be    200
    Find Existing Binary File    root/Cute Lizzards/Varan
    Binary Status Should Be    404
    Find Existing Binary File    root/Terrible Monsters/Varan
    Binary Status Should Be    200

User should be able to delete an existing file
    Create Binary File    Doggo    root    Bark
    Binary Status Should Be    200
    Find Existing Binary File    root/Doggo
    Binary Status Should Be    200
    Delete Existing Binary File    root/Doggo
    Binary Status Should Be    200
    Find Existing Binary File    root/Doggo
    Binary Status Should Be    404

