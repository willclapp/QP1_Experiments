import csv

def csv_phones(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            data.append(line)
    data_length = len(data)
    indices = list(range(12543208, (12543208+data_length), 1))
    print(str(12543208+data_length) + " lines total")
    for x in data:
        x.insert(0, x)
    data[0][0] = "index"
    print("adding indices")
    for x in indices:
        if data[x-12543208][0] != "index":
            data[x-12543208][0] = 12543208+x
    file = open(filename, 'w+')
    print('saving')
    with file:
        write = csv.writer(file)
        write.writerows(data)



def trial_time(filename, output_file):
    data = []
    print('opening file')
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            data.append(line)
        num_list = []
        for x in range(len(data)):
            num_list.append(x)
        for x in num_list:
            if data[x][0] == "slide_order":
                data[x].append("trial_time")
            elif data[x][0] == '100':
                data[x].append("NA")
            elif data[x][0] == '221':
                data[x].append("NA")
            elif data[x][0] == '342':
                data[x].append("NA")
            elif data[x][0] == '463':
                data[x].append("NA")
            else:
                try:
                    start_time = int(data[x][3])
                    end_time = int(data[x+1][3])
                    time_seconds = ((end_time - start_time)/60000)*60
                    data[x].append(time_seconds)
                except ValueError: 
                    data[x].append("NA")
    file = open(output_file, 'w+')
    print('saving')
    with file:
        write = csv.writer(file)
        write.writerows(data)
    print('done saving')



data_file4 = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_2/Analysis/raw/Exp_2_first.csv"
output4 = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_2/Analysis/raw/Exp_2_first_times.csv"

data_file5 = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_2/Analysis/raw/Exp_2_second.csv"
output5 = "/Users/willclapp/Desktop/QP1/QP1_Experiments/Exp_2/Analysis/raw/Exp_2_second_times.csv"

# trial_time(data_file1, output1)
# trial_time(data_file2, output2)
# trial_time(data_file3, output3)
trial_time(data_file4, output4)
trial_time(data_file5, output5)