from flask import Blueprint, render_template, request
import pandas
from datetime import date
import glob
import csv
import os



views = Blueprint('views', __name__)


def calling_fnc(calling_t):

    path = 'C:/Users/Thanalak/PycharmProjects/True/'
    df = pandas.concat(map(pandas.read_csv, glob.glob(path + "*.csv")))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if calling_t == row[1]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def called_fnc(called_t):

    path = 'C:/Users/Thanalak/PycharmProjects/True/'
    df = pandas.concat(map(pandas.read_csv, glob.glob(path + "*.csv")))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def calling_with_date(calling_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if calling_t == row[1]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def called_with_date(called_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def fully_input(calling_t, called_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2] and calling_t == row[1]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        calling = request.form.get('calling_number')
        called = request.form.get('called_number')
        startDate = request.form.get('startdate')
        endDate = request.form.get('enddate')


        if calling != '' and called == '' and startDate == '' and endDate == '':
            res = calling_fnc(calling)
            os.remove("combined_csv.csv")
            return render_template("home.html", tables=[res.to_html()], titles=[''])

        elif calling == '' and called != '' and startDate == '' and endDate == '':
            res = called_fnc(called)
            os.remove("combined_csv.csv")
            return render_template("home.html", tables=[res.to_html()], titles=[''])

        elif calling != '' and called == '' and startDate != '' and endDate != '':
            res = calling_with_date(calling, startDate, endDate)
            os.remove("combined_csv.csv")
            return render_template("home.html", tables=[res.to_html()], titles=[''])

        elif calling == '' and called != '' and startDate != '' and endDate != '':
            res = called_with_date(called, startDate, endDate)
            os.remove("combined_csv.csv")
            return render_template("home.html", tables=[res.to_html()], titles=[''])

        elif calling != '' and called != '' and startDate != '' and endDate != '':
            res = fully_input(calling, called, startDate, endDate)
            os.remove("combined_csv.csv")
            return render_template("home.html", tables=[res.to_html()], titles=[''])

    return render_template("home.html")