#Chase Tullar
#Estate Scraper
#This program searches through estates CVS and prints the desired url

import os

print('Starting Scrape...')

rootdir = '/Users/chase/Desktop/QuantAccountability/crediqDocs/ProsupTop15Loans'
listf = []

for subdir, dirs, files in os.walk(rootdir):
  for file in files:
   # prints clean
    f = file.split(' - ')

    #print('Name : ', f[0])

    try:
        #print('Num : ', f[1])
        #print('Addr : ', f[2])

        fName = f[0].split(' ')
        fName1 = fName[0]
        fName2 = fName[1]
        fNames = fName1 + fName2



        fsub = f[2].split('.')[0]
        #fsub.split(' ')
        #print('Addr : ', fsub)

        curr_url = fNames + f[1] + fsub

        print('File : ', f)
        print('URL : ', curr_url)

        listf.append(curr_url)

    except:
        print('NOT FOUND')


    #furl = faddr[0]

    #listf = []
    #listf.append(furl)
    #print(listf)

#prints consolidated
#print(os.listdir(rootdir))

#for fs in listf:
#    print(fs)

print('Done')
