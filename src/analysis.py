print("5.2 Refactored functions for data analysis")
def events_over_100_tickets(df):
    """Return events that sold more than 100 tickets."""

    result = df[df["tickets_sold"] > 100]

    return result

def highest_priced_event(df):
    """Return the event with the highest ticket price."""

    result = df.sort_values(
        "ticket_price",
        ascending=False
    ).head(1)

    return result
     
def average_attendance_by_venue(df):
    """Calculate average tickets sold by venue."""

    result = (
        df.groupby("venue")["tickets_sold"]
        .mean()
        .sort_values(ascending=False)
    )

    return result

def add_revenue(df):
    """Add estimated ticket revenue to the dataset."""

    df = df.copy()

    df["revenue"] = (
        df["tickets_sold"] *
        df["ticket_price"]
    )

    return df

def highest_revenue_event(df):
    """Return the event with the highest estimated ticket revenue."""

    df = add_revenue(df)

    result = df.sort_values(
        "revenue",
        ascending=False
    ).head(1)

    return result

def add_capacity_utilisation(df):
    """Add percentage of venue capacity sold."""

    df = df.copy()

    df["capacity_utilisation"] = (
        df["tickets_sold"] /
        df["capacity"]
    ) * 100

    return df   

def highest_capacity_utilisation(df):
    """Return the event with the highest capacity utilisation."""

    df = add_capacity_utilisation(df)

    result = df.sort_values(
        "capacity_utilisation",
        ascending=False
    ).head(1)

    return result

def sold_out_events(df):
    """Return events where ticket sales reached capacity."""

    result = df[
        df["tickets_sold"] >= df["capacity"]
    ]

    return result

def average_ticket_price(df):
    """Calculate the average ticket price."""

    return df["ticket_price"].mean()

def total_tickets_sold(df):
    """Calculate total tickets sold across all events."""

    return df["tickets_sold"].sum()

