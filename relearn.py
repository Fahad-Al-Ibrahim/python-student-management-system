import json

with open("relearn.json", "r") as file:
    data = json.load(file)
info_dic = data



def save_data():
    """saves student data to JSON file."""
    with open("relearn.json", "w") as file:
        json.dump(info_dic, file, indent=4)

def add_student():
        """adds new student."""
        b=input("add student id number:")
        if b in info_dic:
            print(f"The id{b} alrady exsist.")
        else:
            a=input("add student name:")
        
            c=input("add student age:")
            d=input("add department:")
            info_name ={} 
            info_name['name'] = a.title()
            info_name['age'] = c
            info_name['department'] = d.upper()
            info_dic[b]=info_name
            save_data()

def view_all():
    """shows all students."""
    print(info_dic)

def search_student():
        """gets students info by id or name."""
        try:
            ab = int(input("1.By name\n2.By id.\n"))
        except ValueError:
             print("Sorry! This section can only accept numbers.")
        else:
             
            found=False
        
            if ab==1:
                nm= input("Name:")
                for key,val in info_dic.items():
                    i = val['name']
                    if i.lower() ==nm.lower():
                        print(key)
                        print(f"\t{val}")
                        found =True
                if found == False:
                    print(f"The student({nm}) does not exist.")
            
            elif ab==2:
                id_nm = (input("Enter id:"))
                if id_nm in info_dic:
                    print(id_nm)
                    print(f"\t{info_dic[id_nm]}")
                
                else:
                    print(f"The student({id_nm}) does not exist.")
            else:
                 print("Invalid option.")

def add_marks():
        """add marks to student account."""
        qu=input('student id:')      
        marks_info={}
        

        if qu in info_dic:
            marks = input("enter maths marks:")
            marks_py=input("inter physics marks:")
            marks_info['math']=marks
            marks_info['physics']=marks_py
            info_dic[qu]['marks']=marks_info
            save_data()
            
        else:
            print(f"There is not student with this id({qu}).")

def get_result():
        """gets student result"""
        qu=input("student id:")
        

        if qu in info_dic:
            
            if 'marks' in info_dic[qu]:

                marks_math= int(info_dic[qu]['marks']['math'])
                marks_physics=int(info_dic[qu]['marks']['physics'])
                
                total = marks_math+marks_physics
                avarage = total/2
                print(f"Math:{marks_math}")
                print(f"Physics:{marks_physics}")
                print(f"Total mark is :{total}")
                print(f"Avarage mark:{avarage}")
                
            else:
                print(f"This student{qu} doesn't have any marks yet.")
        else:
            print(f"There is no student with this id({qu}).")

def update_student():
        """updates studen info."""
        qu = input('Enter id:')
        
        if qu in info_dic:
            print(qu)
            print(f"\t{info_dic[qu]}")
            try:               
                ask = int(input("What would you like to update?\n1.Name\n2.Id\n3.Age\n4.Department.\n"))
            except ValueError:
                 print("Sorry! This section can only accept numbers.")
            else:
                     
                if ask==1:
                    ij=input('Enter new Name:')
                    info_dic[qu]['name']=ij.title()
                    save_data()
                
                elif ask ==2:
                    ij=input('Enter new Id:')
                    if ij in info_dic:
                        print(f"The id({ij}) already exists.")
                    else:
                        info_dic[ij]=info_dic[qu]
                        del info_dic[qu]
                
                        save_data()
                   
                elif ask == 3:
                    ij=input('Enter new Age:')
                    info_dic[qu]['age']=ij
                    save_data()

                elif ask==4:
                    ij=input('Enter new Department:')
                    info_dic[qu]['department']=ij.upper()
                    save_data()
                else:
                     print("Invalid option.")
        else:
            print(f"There is not student with this id({qu}).")

def delete_student():
        """deletes student whole info."""
        ask = input('Enter id:')
        
        if ask in info_dic:
            del info_dic[ask]
            save_data()
            
        else:
            print(f"There is no student with this Id({ask}).")



while True:
    try:
        question = int(input("welcome\n1.Add student\n2.View all students\n3.Search student\n4.Add marks\n5.Get result\n6.Update student\n7.Delete student\n8.Exit.\n"))
    except ValueError:
         print("Sorry! This section can only accept numbers.")
    else:

        if question == 1:
            add_student()

        elif question==2:
            view_all()

        elif question==3:
            search_student()

        elif question==4:
            add_marks()

        elif question==5:
            get_result()

        elif question==6:
            update_student()

        elif question==7:
            delete_student()

        elif question==8:
            break
        else:
             print("Invalid option.")







