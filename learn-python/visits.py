import os

os.chdir('/home/alexeit/git/learn-python/')

visits = []

if os.path.isfile('visits.txt'):
	with open('visits.txt' ,'r') as file_visits:
		for visit in file_visits:
			visits_format = visit.strip()
			visits_format = visits_format.split(',')
			visits.append(visits_format)

def get_visits():
	for visit in visits:
		print('You were in ES in next date : {0} - {1}'.format(visit[0], visit[1]))

def add_visit(date_arrive, date_leave):
	visits.append([date_arrive, date_leave])

def del_visit(date_remove):
	for visit in visits:
		if date_remove in visit:
			index_remove_visit = visits.index(visit)
			del visits[index_remove_visit]

date_arrive = 0

while True:
	print(
	"""
	p - Show your visits

	a - Add yout visits

	r - Remove visits

	w - Write in file

	e - Exit

	""")
	choice = input('Enter your choice: ')

	if choice == 'p':
		if visits == []:
			print('You are not visit ES yet')
			input('Push any bottom !')
		else:
			get_visits()
			input('Push any bottom !')
	elif choice == 'a':
		date_arrive = input('Enter date arrive: ')
		date_leave = input('Enter date leave: ')
		if date_arrive > date_leave:
			print('You can not leave ES early then arrive!!')
			continue
		if visits != []:
		    if visits[-1][1] >= date_arrive:
			    print('You entered wrong date arrive, try again')
			    input('Push any bottom !')
		if int(date_arrive) - int(visits[0][0]) > 90:
			print('You stay in ES too long, you will not go in ES')
			print('You stayed in ES {0}'.format(int(date_arrive) - int(visits[0][0])))
		else:
			add_visit(date_arrive, date_leave)
			print('Your visits {0} - {1} was add'.format(date_arrive,date_leave))
	elif choice == 'r':
		date_remove = input('Enter date for delete: ')
		del_visit(date_remove)
	elif choice == 'w':
		with open('visits.txt', 'w') as file_visits:
			pass
		for visit in visits:
			with open('visits.txt', 'a') as file_visits:
				file_visits.write('{0}, {1} \n'.format(visit[0], visit[1]))
		print('File was write')
	elif choice == 'e':
		print('You wanted to exit in programm, GOOD BY')
		break
	else:
		print('You entered wrong choice')
		input('Push any bottom !')


