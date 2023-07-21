def convert_input_to_integers(input_list):
    for index in range(len(input_list)):
        input_list[index] = int(input_list[index])
    return input_list

def count_doctors_during_inspections(inspection_times, doctor_schedules):
    doctors_available = []
    doctor_schedules.sort()
    for inspection_time in inspection_times:
        doctors_count = 0
        for doctor_schedule in doctor_schedules:
            shift_start_time = doctor_schedule[0]
            shift_end_time = doctor_schedule[1]
            if shift_start_time <= inspection_time and inspection_time <= shift_end_time:
                doctors_count += 1 
        
        doctors_available.append(str(doctors_count))
        
    return doctors_available
    
def main():
    inspection_times = input().split()
    number_of_doctors = int(input())

    doctor_schedules = []
    for i in range(number_of_doctors):
        shift_start_time, shift_end_time = input().split()
        shift_start_time = int(shift_start_time)
        shift_end_time = int(shift_end_time)
        doctor_schedules.append([shift_start_time, shift_end_time])
    
    inspection_times = convert_input_to_integers(inspection_times)

    doctors_during_inspections = count_doctors_during_inspections(inspection_times, doctor_schedules)
    
    doctors_during_inspections = " ".join(doctors_during_inspections)
    
    print(doctors_during_inspections)
    
main()