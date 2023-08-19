import re

seconds = int(input("Enter number of seconds to convert: "))

years = 0
days = 0
hours = 0
minutes = 0
    
if seconds == 0 or seconds == '':
    print("now")
    
if (seconds - 31536000) >= 0:
    while(seconds >= 31536000):
        seconds = seconds - 31536000
        years = years + 1
    
if (seconds - 86400) >= 0:
    while(seconds >= 86400):
        seconds = seconds - 86400
        days = days + 1
            
if (seconds - 3600) >= 0:
    while(seconds >= 3600):
        seconds = seconds - 3600
        hours = hours + 1
    
if (seconds - 60) >= 0:
    while(seconds >= 60):
        seconds = seconds - 60
        minutes = minutes + 1
    
# The readable format creation is currently quite convoluted
total_fstring_list = []
    
years_fstring = f"{years} year{'s'[:years^1]}"
if years != 0:
    total_fstring_list.append(years_fstring)
        
days_fstring = f"{days} day{'s'[:days^1]}"
if days != 0:
    total_fstring_list.append(days_fstring)
        
hours_fstring = f"{hours} hour{'s'[:hours^1]}"
if hours != 0:
    total_fstring_list.append(hours_fstring)
    
minutes_fstring = f"{minutes} minute{'s'[:minutes^1]}"
if minutes != 0:
    total_fstring_list.append(minutes_fstring)  
    
seconds_fstring = f"{seconds} second{'s'[:seconds^1]}"
if seconds != 0:
    total_fstring_list.append(seconds_fstring)
        
total_fstring_string = ','.join(total_fstring_list)
    
total_fstring_list_reformat = total_fstring_string.split(",")
    
len_tflr = len(total_fstring_list_reformat)
if len_tflr > 1:
    and_string = "and " + total_fstring_list_reformat[len_tflr - 1]
    total_fstring_list_reformat.append(and_string)
    total_fstring_list_reformat.pop(-2)

#The Oxford comma was a significant pain point for a while    
oxfordcomma_fstring_string = ', '.join(total_fstring_list_reformat)
    
final_fstring_string_1 = oxfordcomma_fstring_string.rsplit(',', 1)[0]
final_fstring_string_2 = ','.join(oxfordcomma_fstring_string.split(',')[-1:])
    
if final_fstring_string_1 != final_fstring_string_2:
    final_fstring_string = final_fstring_string_1 + final_fstring_string_2
    
else:
    final_fstring_string = final_fstring_string_1
    
print(final_fstring_string)
