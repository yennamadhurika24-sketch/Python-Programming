def clean_email(email_list):
    return set(email.lower() for email in email_list)
def final_report(day1_raw,day2_raw,day3_raw):
    day1=clean_email(day1_raw)
    day2=clean_email(day2_raw)
    day3=clean_email(day3_raw)
    
#All unique
    unique=day1| day2| day3
    attended_all_three=day1 & day2 & day3
    #Attendees who exactly attended one day
    only_day1=day1-(day2|day3)
    only_day2=day2-(day1|day3)
    only_day3=day3-(day1|day2)
    
    # Pair wise overlap counts
    d1_d2_overlap=day1 & day2
    d2_d3_overlap= day2 & day3
    d3_d1_overlap= day3 & day1
    print("Count of unique elements=",len(unique))
    print("unique data(sorted):",sorted(unique))
    print("count of people who attended all the three days=",len(attended_all_three))
    print("Attendees who exactly attended one day(Sorted)",sorted(attended_all_three))
    print("count of only day1=",len(only_day1))
    print("count of only day2=",len(only_day2))
    print("count of only day3=",len(only_day3))
    print("Attendees who exactly attended one day(Sorted)Day1=",sorted(only_day1))
    print("Attendees who exactly attended one day(Sorted)Day2=",sorted(only_day2))
    print("Attendees who exactly attended one day(Sorted)Day3=",sorted(only_day3))
    print("Count of pair wise overlaps of day1 and day2=",len(d1_d2_overlap))
    print("Count of pair wise overlaps of day2 and day3=",len(d2_d3_overlap))
    print("Count of pair wise overlaps of day3 and day1=",len(d3_d1_overlap))
    print("overlap of day1 amd day2(Sorted)=",sorted(d1_d2_overlap))
    print("overlap of day2 amd day3(Sorted)=",sorted(d2_d3_overlap))
    print("overlap of day3 amd day1(Sorted)=",sorted(d3_d1_overlap))
day1 = [
    "Alice@example.com", "BOB@example.com", "charlie@example.com",
    "alice@example.com", "bob@example.com"
]

day2 = [
    "bob@example.com", "david@example.com", "EVE@example.com",
    "frank@example.com", "DAVID@example.com"
]

day3 = [
    "George@example.com", "alice@example.com", "Eve@example.com",
    "harry@example.com", "CHARLIE@example.com"
]

# Run the report
final_report(day1, day2, day3)