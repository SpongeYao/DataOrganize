import os
import sys 
inputFile= sys.argv[1]
outputFile= sys.argv[2]
#atomList= sys.argv[3]

type_name= inputFile.split('_')[0]
f = open(inputFile,"r")
#af= open(atomList, 'r')
index=1 
list_all=[]
for line in f:
    '''
    if index> 20:
        break 
    '''
    list_file=[]
    filename= line.strip()
    print '{0} {1}'.format(index, filename)
    data= open(type_name+'_xyz/'+filename, 'r')
    atomIndex=0
    for xyz in data:
        atomIndex= atomIndex+1
        #print 'atomIndex: ', atomIndex
        if atomIndex<=2:
            continue 
        if atomIndex>56+2:
            break 
        print xyz.strip() 
        #list_file.append(xyz.strip())
        list_file.append(xyz)

    list_all.append(list_file)
    index= index+1

print 'len(list_all): ',len(list_all)
print 'len(list_all[0]): ',len(list_all[0])
atomIndex=1
for col_idx in range(0, len(list_all[0])):
    savefile= '{0}_{1}_{2}.dat'.format(type_name, atomIndex, list_all[0][col_idx][0:4].strip())
    print '### ',savefile ,'###'
    s= open(type_name+'_result/'+savefile, 'w')
    for row_idx in range(0,len(list_all)):
        
        #xyz= list_all[row_idx][col_idx][7:].split('     ')
        tmp= list_all[row_idx][col_idx]
        xyz= tmp[8:len(tmp)].strip().split('   ')
        print xyz 
        s.write('{0} {1} {2} \n'.format(xyz[0].strip(), xyz[1].strip(), xyz[2].strip()))
    s.close()
    atomIndex= atomIndex+1 
       

