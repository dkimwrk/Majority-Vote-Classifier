import csv
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as file:     
        train_df= list(csv.reader(file, delimiter="\t"))

    train_features= train_df[0]
    train_df= train_df[1:]
    train_Y=[]
    for line in train_df:
        train_Y.append(line[-1])

    trainlabel_count={}
    for num in train_Y:
        trainlabel_count[num]= trainlabel_count.get(num,0)+1

    train_majority=[key for key, value in trainlabel_count.items() if value == max(trainlabel_count.values())]
    majority_elem= max(train_majority)
    train_labels= len(train_Y)*[majority_elem]

    error=0
    for key,val in trainlabel_count.items():
        if int(key)!=int(majority_elem):
            error+=int(val)
    trainerror= error/len(train_Y)


    with open(sys.argv[2]) as file2:     
        test_df= list(csv.reader(file2, delimiter="\t"))

    test_features= test_df[0]
    test_df= test_df[1:]
    test_Y=[]

    for line in test_df:
        test_Y.append(line[-1])

    testlabel_count={}
    for num in test_Y:
        testlabel_count[num]= testlabel_count.get(num,0)+1

    test_labels= len(test_Y)*[majority_elem]

    error2=0
    for key,val in testlabel_count.items():
        if int(key)!=int(majority_elem):
            error2+=int(val)
    testerror= error2/len(test_Y)


    '''writing into the text files'''
    predicted_train = open(sys.argv[3], 'w')

    for i in train_labels:
        predicted_train.write(i)
        predicted_train.write("\n")

    predicted_train.close()

    predicted_test = open(sys.argv[4], 'w')

    for i in test_labels:
        predicted_test.write(i)
        predicted_test.write("\n")
    predicted_test.close()

    metrics = open(sys.argv[5], 'w')

    metrics.write("error(train): ")
    metrics.write(str(trainerror))
    metrics.write('\n')

    metrics.write("error(test): ")
    metrics.write(str(testerror))
    metrics.write('\n')

    metrics.close()

    """file1 = open(sys.argv[3], 'r')
    print(file1.read())
    file1.close()

    file2 = open(sys.argv[4], 'r')
    print(file2.read())
    file2.close()

    file3 = open(sys.argv[5], 'r')
    print(file3.read())
    file3.close()"""

