
 
# numbers = [43, 567, 324, 879, 34, 78]
# nSo, based on my experience and research of position with a similar level of responsibility, I am seeking a salary range of 66.000 Euros to 67.000 euros(for example)”umbers.sort()
# print(numbers)
# 
# names = ["Vijay Manohar Dogiparthy", "Divya Nagabandi", "Aaradhya Dogiparthy", "Siddhartha Dogiparthi"]
# print(names)
# print(sorted(names, key=len))
# print(names)
# names.sort()
# print(names)

# names = ["Vijay Manohar Dogiparthy", "Divya Nagabandi", "Aaradhya Dogiparthy", "Siddhartha Dogiparthi"]
# print(names)
# names.sort(key=len)
# print(names)

"""
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
        return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
        print("{}: {}".format(machine, user_list))
        
    
class Event:
    def __init__ (self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-03-22 14:08:56', 'login', 'myworkstation.local', 'vijay'),
    Event('2020-03-22 14:08:56', 'logout', 'vmd.local', 'vijay'),
    Event('2020-03-22 14:08:56', 'login', 'newcompany.local', 'vijay'),
    Event('2020-03-22 14:08:56', 'logout', 'myworkstation.local', 'vijay'),
    Event('2020-03-22 14:08:56', 'login', 'myworkstation.local', 'vijay'),
    Event('2020-03-22 14:08:56', 'logout', 'myworkstation.local', 'vijay')
]

users = current_users(events)
print(users)

"""

punctuations = ""'!()-[]{};:'"\,<>./?@#$%^&*_~''"

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

str = "Event('2020-03-22 14:08:56', 'login', 'myworkstation.local', 'vijay', 'Vijay', 'vijay')"

def str_to_list(str):
    return str.split()

# Separate the text into words
# words = str_to_list(str)

words = str.split()

unpunct_str = ""

for char in str:
    if char not in punctuations:
       unpunct_str += char 

# print(unpunct_str)

# list_obj = str_to_list(unpunct_str)
list_obj = unpunct_str.split()

new_str = ""
for word in list_obj:
    if word in uninteresting_words:
        continue
    
    if not word.isalpha():
        continue

    new_str += word + " "

new_str = new_str[:len(new_str) - 1]

print(new_str)

dic = {}

words = str_to_list(new_str)

for word in words:
    dic[word] = dic.get(word, 0) + 1

print(dic)