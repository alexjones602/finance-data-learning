print("Jigsaw Events Sales data practice as of 23/7/26")
print("1.1 Variables:")

venue = "Bonobo Bar and Canteen"
print(venue)
earlybird_tickets_sold = 11
print(earlybird_tickets_sold)
general_release_tickets_sold = 0
print(general_release_tickets_sold)
final_release_tickets_sold = 0
print(final_release_tickets_sold)
capacity = 100
print(capacity)
earlybird_ticket_price = 7.00
print(earlybird_ticket_price)
general_release_ticket_price = 8.00
print(general_release_ticket_price) 
final_release_ticket_price = 9.00
print(final_release_ticket_price)

print("1.2 Strings:")
moto = "House Music, Piece by Piece"
print(moto)
first = "House Music,"
second = "Piece by Piece"
print(first + " " + second)
dj = "Alex Jones"
venue = "Bonobo Bar and Canteen"
city = "Chester"
print(dj + " will be performing at " + venue + " in " + city)

print("1.3 Numbers:")
total_tickets_sold = earlybird_tickets_sold + general_release_tickets_sold + final_release_tickets_sold
print(total_tickets_sold)
total_tickets_remaining = capacity - total_tickets_sold
print(total_tickets_remaining)
total_sales = (earlybird_tickets_sold * earlybird_ticket_price) + (general_release_tickets_sold * general_release_ticket_price) + (final_release_tickets_sold * final_release_ticket_price)
print(total_sales)

print("1.4 Basic Maths")
earlybird_ticket_revenue = earlybird_tickets_sold * earlybird_ticket_price
print(earlybird_ticket_revenue)
general_release_ticket_revenue = general_release_tickets_sold * general_release_ticket_price
print(general_release_ticket_revenue)
final_release_ticket_revenue = final_release_tickets_sold * final_release_ticket_price
print(final_release_ticket_revenue)

