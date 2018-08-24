import datetime

test_file = open('test.txt', 'a')
test_file.write('\ntest ' +  str(datetime.datetime.now()))
test_File.write(' ')
test_file.close()
