import csv


class RootFind:
    def __init__(self):
        pass

    def rootFinding(self, input, predefined_root_word):
        try:

            rooted_dict = {}

            '''Here open the input word file. Here every word stored in one line'''
            input_data = open(input+".txt", 'r')

            '''The reference or predefined root word and parts of speech store in dictionary (rooted_dict).'''
            with open(predefined_root_word+'.csv', 'r') as rooted_data:
                rooted_data = csv.reader(rooted_data)
                for data in rooted_data:
                    rooted_dict.update({data[2]: data[1]})

            '''Store the result main word, root word, root word's parts of speech and the suffix'''
            with open('result.csv', 'w+', newline='') as csvfile:
                rooted_word_result = csv.writer(csvfile)
                rooted_word_result.writerow(['Word', 'Root', 'Parts of speech', 'Suffix'])
                for data in input_data:
                    for i in range(0, data.__len__(), 1):
                        if data[:i] in rooted_dict:
                            rooted_word_result.writerow([data, data[:i], rooted_dict[data[:i]], data[i:], ''])

        except Exception as msg:
            print("From Root Find in rootFinding Method: "+str(msg))


def main():
    try:
       root_finding = RootFind()

       '''rootFinding method need two file one is input file which contains row words and second file is reference rooted words file'''

       root_finding.rootFinding("input", "reference_root_words")
    except Exception as msg:
        print(msg)


if __name__ == "__main__":
    main()