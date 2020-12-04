import csv

students_list, master_list = [], []
speaking_gain, speaking_regress, speaking_same = [], [], []
listening_gain, listening_regress, listening_same = [], [], []
reading_gain, reading_regress, reading_same = [], [], []
writing_gain, writing_regress, writing_same = [], [], []
speaking_delta_list, listening_delta_list, reading_delta_list, writing_delta_list = [], [], [], []

# create dictionary from csv file

with open('/home/ben/access.csv') as access_comp:
    csv_reader = csv.reader(access_comp, delimiter=',')
    i = 1
    while i < 23:
        access_comp.seek(0)
        score_list = []
        for row in csv_reader:
            score_list.append(row[i])
        i += 1
        students_list.append(score_list)

    for student in students_list:
        score_dict = {'name': student[0], 2019: {'composite': student[1], 'comprehension': student[2],
            'listening': student[3], 'literacy': student[4], 'oral': student[5], 'reading': student[6],
            'speaking': student[7], 'writing': student[8]}, 2020: {'composite': student[10],
            'comprehension': student[11], 'listening': student[12], 'literacy': student[13],
            'oral': student[14], 'reading': student[15], 'speaking': student[16], 'writing': student[17]}}
        master_list.append(score_dict)
    # print(master_list)

# filter through dictionaries and sort students into gain/regress/no-change lists

    for student in master_list:
        if student[2019]['speaking'] < student[2020]['speaking']:
            speaking_gain.append(student['name'])
        elif student[2019]['speaking'] > student[2020]['speaking']:
            speaking_regress.append(student['name'])
        else:
            speaking_same.append(student['name'])
    print("\n\nSpeaking results:\n\nGained: {}\n{}\n\nNo change: {}\n{}\n\nRegressed: {}\n{}\n\n".format(len(speaking_gain),
          speaking_gain, len(speaking_same), speaking_same, len(speaking_regress), speaking_regress))

    for student in master_list:
        if student[2019]['listening'] < student[2020]['listening']:
            listening_gain.append(student['name'])
        elif student[2019]['listening'] > student[2020]['listening']:
            listening_regress.append(student['name'])
        else:
            listening_same.append(student['name'])
    print("Listening results:\n\nGained: {}\n{}\n\nNo change: {}\n{}\n\nRegressed: {}\n{}\n\n".format(len(listening_gain),
          listening_gain, len(listening_same), listening_same, len(listening_regress), listening_regress))

    for student in master_list:
        if student[2019]['reading'] < student[2020]['reading']:
            reading_gain.append(student['name'])
        elif student[2019]['reading'] > student[2020]['reading']:
            reading_regress.append(student['name'])
        else:
            reading_same.append(student['name'])
    print("Reading results:\n\nGained: {}\n{}\n\nNo change: {}\n{}\n\nRegressed: {}\n{}\n\n".format(len(reading_gain),
          reading_gain, len(reading_same), reading_same, len(reading_regress), reading_regress))

    for student in master_list:
        if student[2019]['writing'] < student[2020]['writing']:
            writing_gain.append(student['name'])
        elif student[2019]['writing'] > student[2020]['writing']:
            writing_regress.append(student['name'])
        else:
            writing_same.append(student['name'])
    print("Writing results:\n\nGained: {}\n{}\n\nNo change: {}\n{}\n\nRegressed: {}\n{}\n\n".format(len(writing_gain),
          writing_gain, len(writing_same), writing_same, len(writing_regress), writing_regress))

# but how much did students regress

    for student in master_list:
        speaking_delta = float(student[2019]['speaking']) - float(student[2020]['speaking'])
        if speaking_delta > 0:
            neg_speaking_delta = {'name': student['name'], 'loss': speaking_delta}
            speaking_delta_list.append(neg_speaking_delta)
    total_speaking_loss_list = []
    for score in speaking_delta_list:
        total_speaking_loss_list.append(score['loss'])
    total_speaking_loss = sum(total_speaking_loss_list)
    avg_speaking_loss = total_speaking_loss / len(speaking_delta_list)
    print("\n\nSpeaking losers: {}\n{}".format(len(speaking_delta_list), speaking_delta_list))
    print("Average loss: {}".format(avg_speaking_loss))

    for student in master_list:
        listening_delta = float(student[2019]['listening']) - float(student[2020]['listening'])
        if listening_delta > 0:
            neg_listening_delta = {'name': student['name'], 'loss': listening_delta}
            listening_delta_list.append(neg_listening_delta)
    total_listening_loss_list = []
    for score in listening_delta_list:
        total_listening_loss_list.append(score['loss'])
    total_listening_loss = sum(total_listening_loss_list)
    avg_listening_loss = total_listening_loss / len(listening_delta_list)
    print("\n\nListening losers: {}\n{}".format(len(listening_delta_list), listening_delta_list))
    print("Average loss: {}".format(avg_listening_loss))

    for student in master_list:
        reading_delta = float(student[2019]['reading']) - float(student[2020]['reading'])
        if reading_delta > 0:
            neg_reading_delta = {'name': student['name'], 'loss': reading_delta}
            reading_delta_list.append(neg_reading_delta)
    total_reading_loss_list = []
    for score in reading_delta_list:
        total_reading_loss_list.append(score['loss'])
    total_reading_loss = sum(total_reading_loss_list)
    avg_reading_loss = total_reading_loss / len(reading_delta_list)
    print("\n\nReading losers: {}\n{}".format(len(reading_delta_list), reading_delta_list))
    print("Average loss: {}".format(avg_reading_loss))

    for student in master_list:
        writing_delta = float(student[2019]['writing']) - float(student[2020]['writing'])
        if writing_delta > 0:
            neg_writing_delta = {'name': student['name'], 'loss': writing_delta}
            writing_delta_list.append(neg_writing_delta)
    total_writing_loss_list = []
    for score in writing_delta_list:
        total_writing_loss_list.append(score['loss'])
    total_writing_loss = sum(total_writing_loss_list)
    avg_writing_loss = total_writing_loss / len(writing_delta_list)
    print("\n\nWriting losers: {}\n{}".format(len(writing_delta_list), writing_delta_list))
    print("Average loss: {}".format(avg_writing_loss))


