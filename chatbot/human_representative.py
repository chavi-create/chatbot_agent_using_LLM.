import csv

def request_human_representative(full_name, email, phone):
    with open('data/contact_requests.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([full_name, email, phone])
    return "Your request has been submitted. Our representative will contact you shortly."
