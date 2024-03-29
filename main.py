# Built-in imports
import math

GRADE = {}

for score in range(0,101):
  if score < 40:
    GRADE[score] = 'U'
  elif (score >= 40) and (score < 45):
    GRADE[score] = 'S'
  elif (score >= 45) and (score < 50):
    GRADE[score] = 'E'
  elif (score >= 50) and (score < 55):
    GRADE[score] = 'D'
  elif (score >= 55) and (score < 60):
    GRADE[score] = 'C'
  elif (score >= 60) and (score < 70):
    GRADE[score] = 'B'
  elif score >= 70 :
    GRADE[score] = 'A'


def read_testscores(filename):
  """
  Takes a string filename and reads the data, and returns a list of dicts, each representing row data for a single student.

  Parameters 
  ----------
  filename: str
      the file that is to be opened

  Returns
  -------
  list of dicts
    each dict represents the 
    'class'
    'name'
    'overall'
    'grade' for each student
  """
  list = []
  with open('testscores.csv','r') as f:
    header = f.readline()
    for line in f:
      record = line.strip().split(',')
      p1 = int(record[2])
      p2 = int(record[3])
      p3 = int(record[4])
      p4 = int(record[5])
      score_tup = (p1/30 * 15), (p2/40 * 30), (p3/80 * 35), (p4/30 * 20)
      overall = score_tup[0] + score_tup[1] + score_tup[2] + score_tup[3]
      overall = math.ceil(overall)
      grade = GRADE[overall]
      info = {'class':line[0], 'name':line[1], 'overall':overall, 'grade':grade}
      list.append(info)
  return(list)


def analyze_grades(studentdata):
    """
    Takes in student data and returns a dict representing the count of each grade for each class.

    Parameters 
    ----------
    studentdata

    Returns
    -------
    dict
      representing the count of each grade for each class
    """
    A_count = 0
    B_count = 0
    C_count = 0
    D_count = 0
    E_count = 0
    S_count = 0
    U_count = 0
    grade_count = {}
    for line in studentdata:
      room = line['class']
      grade = line['grade']
      if grade == 'A':
        A_count += 1
      elif grade == 'B':
        B_count += 1
      elif grade == 'C':
        C_count += 1
      elif grade == 'D':
        D_count += 1
      elif grade == 'E':
        E_count += 1
      elif grade == 'S':
        S_count += 1
      elif grade == 'U':
        U_count += 1

      grade_count = {room:{'A':A_count, 'B':B_count, 'C':C_count, 'D':D_count, 'E':E_count, 'S':S_count, 'U':U_count}}

    return(grade_count)