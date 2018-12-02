# Semester 1, 2018
# CITS1401 Project 1
# Author: Xinkai Chen, Student number: 22404059

import os

def open_file(filename):

    # if the file exists, return the file handle
    if os.path.isfile(filename):
        csvfile = open(filename)
        return csvfile

    # if the file does not exist, return None
    else:
        print(filename, "does not exist!")
        return None

def get_units(unitfile):

    # store all the units in a list
    units_list = []

    # get the file handle
    handle = open_file(unitfile)
    if handle is None:
        exit()

    # convert each unit and its full mark to corresponding formats, and then add to the list
    for line in handle:
        ln = line.strip('\n').split(',')
        if len(ln) == 2:
            unit = str(ln[0])
            mark = float(ln[1])
            units_list.append((unit, mark))

    return units_list

def get_student_records(students_file, unit_count):

    # store all the student marks into a list
    students_list = []

    # get the file handle
    handle = open_file(students_file)
    if handle is None:
        exit()

    for line in handle:
        ln = line.strip('\n').split(',')
        if len(ln) == unit_count + 1:
            for i in range(1, len(ln)):
                if len(ln[i]) == 0:
                    ln[i] = None
                else:
                    ln[i] = float(ln[i])

        else:
            raise ValueError("Student records do not match the units information! Please try again.")

        students_list.append(list(ln))

    return students_list

def normalise(students_list, units_list):

    # store normalised results in a list
    normalised_list = []

    # record the full mark of each unit in a list
    full_marks = [unit[1] for unit in units_list]

    for info in students_list:
        # create the normalised list for each student
        pclist = []
        pclist.append(info[0])
        # divide the student mark by corresponding full mark. In each info, marks start from position 1
        for i in range(1, len(info)):
            if info[i] != None:
                pclist.append(info[i] / full_marks[i - 1])

        normalised_list.append(pclist)

    return normalised_list

def compute_mean_pc(students_pclist):

    mean_pclist = []

    # compute the average marks and add the tuples containing mean marks and names to the list
    for info in students_pclist:
        sum, count = 0, 0
        for i in range(1, len(info)):
            if info[i] != None:
                sum += info[i]
                count += 1
        mean = sum / count
        mean_pclist.append((mean, info[0]))

    return mean_pclist

def print_final_list(mean_pclist):

    # sort the marks in descending order
    final_list = sorted(mean_pclist, reverse=True)

    # print out the final list (round the marks to 3 decimal places)
    print()
    print("Students and their final marks are as follows:\n")
    for mark, name in final_list:
        print(name, ' ', round(mark, 3))

def main():
    units_file = input("Enter the file name of the units list: ")
    students_file = input("Enter the file name of the students list: ")
    units_list = get_units(units_file)
    students_list = get_student_records(students_file, len(units_list))
    students_pclist = normalise(students_list, units_list)
    mean_pclist = compute_mean_pc(students_pclist)
    print_final_list(mean_pclist)

    # close two files
    open_file(units_file).close()
    open_file(students_file).close()

if __name__ == '__main__':
    main()



