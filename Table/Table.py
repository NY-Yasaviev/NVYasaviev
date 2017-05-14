file = open('table.html', 'w')
file.write('<html>' + '\n' + '<head>' + '\n' + '<style>table, td, tr{ border:1px solid black;border-collapse: collapse;}</style>' + '\n' + '</head>' + '\n' + '<body>' + '\n' + '<table>' + '\n')

for i in range(1, 10):
    file.write('<tr>' + '\n')
    for j in range(1,10):
        file.write('<td>' + str(i*j) + '</td>' + '\n')
    file.write('</tr>' + '\n')

file.write('</table>' + '\n' + '</body>' + '\n' + '</head>' + '\n' + '</html>')
file.close()