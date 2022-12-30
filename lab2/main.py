from nodes.directory import Directory
from nodes.binary_file import BinaryFile
from nodes.log_text_file import LogTextFile
from nodes.buffer_file import BufferFile

rootDirectory = Directory('root', 10)
directory1 = Directory('directory1', 5, rootDirectory)
directory2 = Directory('directory2', 5, rootDirectory)
print()

binary1 = BinaryFile('binary1', directory1, 'binary1 text')
print('binary1 content: ' + binary1.readFile())
binary2 = BinaryFile('binary2', directory2, 'binary2 text')
print('binary2 content: ' + binary2.readFile() + '\n')

binary1.move(directory2)
print()

logText1 = LogTextFile('logText1', directory1)
logText1.appendLine('line1\n')
logText1.appendLine('line2\n')
print('log text content: ' + logText1.readFile() + '\n')

logText2 = LogTextFile('logText2', directory2)
logText2.appendLine('newLine1\n')
logText2.appendLine('new lineeeee 2\n')
print('log text content: ' + logText2.readFile() + '\n')

buffer1 = BufferFile('buffer1', 5, directory1)
buffer1.pushElement('element 1')
buffer1.pushElement('element 2')
print('buffer element from queue: ' + buffer1.consumeElement() + '\n')

print('root directory content: ', rootDirectory.listContent())
print('directory1 content: ', directory1.listContent())
print('directory2 content: ', directory2.listContent())