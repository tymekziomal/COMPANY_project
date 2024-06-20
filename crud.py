import folium


def show_company(companies_list: list[dict]) -> None:
    for companies in companies_list:
        print(
            f"nazwa: {companies['name']},miejscowosc: {companies['location']}, szerokosc geograficzna: {companies['latitude']}, {companies['longitude']}")


def show_customer(customers_list: list[dict]) -> None:
    for customer in customers_list:
        print(
            f"Imie kilenta {customer['name']}, nazwisko klienta {customer['surname']},miejscowosc: {customer['location']}, szerokosc geograficzna: {customer['latitude']}, {customer['longitude']}")


def show_employee(employees_list: list[dict]) -> None:
    for employee in employees_list:
        print(
            f"Imie pracownika {employee['name']}, nazwisko pracownika {employee['surname']},miejscowosc: {employee['location']}, szerokosc geograficzna: {employee['latitude']}, {employee['longitude']}")


def add_new_company(companies: list[dict]) -> None:
    new_name = new_company = input("Nowa nazwa firmy: ")
    add_new_location = input("Podaj miejscowosc: ")
    coordinates = get_coordinates(add_new_location)

    if coordinates:
        new_latitude, new_longitude = coordinates

    new_company: dict = {"name": new_name, "location": add_new_location, "latitude": new_latitude,
                         "longitude": new_longitude, "company": companies}
    companies.append(new_company)


def add_new_customer(customers: list[dict]) -> None:
    new_name: str = input("Nowe imie klienta: ")
    new_surname: str = input("Nowe nazwisko klienta: ")
    add_new_location = input("Podaj miejscowosc: ")
    new_my_company = input("Wpisz firme do ktorej nalezysz")


    coordinates = get_coordinates(add_new_location)

    if coordinates:
        new_latitude, new_longitude = coordinates

    new_customer: dict = {"name": new_name, "location": add_new_location, "latitude": new_latitude,
                          "longitude": new_longitude, "surname": new_surname, "company": new_my_company}
    customers.append(new_customer)


def add_new_employee(employees_list) -> None:
    new_name: str = input("Nowe imie pracownika: ")
    new_surname: str = input("Nowe nazwisko pracownika: ")
    add_new_location: str = input("Podaj miejscowosc: ")
    new_workplace = input("Wpisz nazwe firmy w ktorej nalezysz ")
    coordinates = get_coordinates(add_new_location)

    if new_workplace := False:
        for new_workplace in employees_list:
            if new_workplace['name'] == new_workplace:
                new_workplace = True
                break

    new_workplace = any(company['name'] == new_workplace for company in employees_list)

    if not new_workplace:
        print("Nie można dodać pracownika. Firma nie istnieje.")

    if coordinates:
        new_latitude, new_longitude = coordinates

    new_employee = {"name": new_name, "location": add_new_location, "latitude": new_latitude,
                    "longitude": new_longitude, "surname": new_surname, "company": new_workplace}
    employees_list.append(new_employee)


def remove_company(companies) -> None:
    Jakiej_firmy_szukasz = input("Jakiej firmy szukasz: ")
    for company in companies:
        if company['name'] == Jakiej_firmy_szukasz:
            companies.remove(company)


def remove_customer(customers) -> None:
    Jakiego_klienta_szukasz = input("Jakiego klienta szukasz: ")
    for customer in customers:
        if customer['name'] == Jakiego_klienta_szukasz:
            customers.remove(customer)


def remove_employee(employees) -> None:
    Jakiego_pracownika_szukasz = input("Jakiego pracownika szukasz: ")
    for employee in employees:
        if employee['name'] == Jakiego_pracownika_szukasz:
            employees.remove(employee)


def update_company(companies_list) -> None:
    Jakiej_firmy_szukasz = input('Nazwa firmy do aktualizacji: ')
    for company in companies_list:
        if company['name'] == Jakiej_firmy_szukasz:
            new_name = new_company = input('Wprowadz nowa nazwe firmy: ')
            update_new_location = input("Podaj miejscowosc: ")
            coordinates = get_coordinates(update_new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates

            company['name'] = new_name
            company['location'] = update_new_location
            company['latitude'] = new_latitude
            company['longitude'] = new_longitude
            company['company'] = new_company

            print(f"Firma  {Jakiej_firmy_szukasz} zostało zaktualizowane.")
            return
    print(f"Firma {Jakiej_firmy_szukasz} nie zostało znalezione.")


def update_customer(customers_list) -> None:
    Jakiego_klienta_szukasz = input('Imie klienta do aktualizacji: ')
    for customer in customers_list:
        if customer['name'] == Jakiego_klienta_szukasz:
            new_name = input('Wprowadz nowe imie klienta: ')
            new_surname = input('Wprowadz nowe nazwisko klienta: ')
            update_new_location = input("Podaj miejscowosc: ")
            new_my_company = input('Wpisz nazwe firmy do ktorej nalezysz')
            coordinates = get_coordinates(update_new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates

            customer['name'] = new_name
            customer['surname'] = new_surname
            customer['location'] = update_new_location
            customer['latitude'] = new_latitude
            customer['longitude'] = new_longitude
            customer['company'] = new_my_company

            print(f"Klient  {Jakiego_klienta_szukasz} zostało zaktualizowane.")
            return
    print(f"Klient {Jakiego_klienta_szukasz} nie zostało znalezione.")


def update_employee(employees_list) -> None:
    Jakiego_pracownika_szukasz = input('Imie pracownika do aktualizacji: ')
    for employee in employees_list:
        if employee['name'] == Jakiego_pracownika_szukasz:
            new_name = input('Wprowadz nowe imie pracownika: ')
            new_surname = input('Wprowadz nowe nazwisko pracownika: ')
            update_new_location = input('Podaj miejscowosc: ')
            new_workplace = input('Wpisz nazwe firmy do ktorej nalezysz ')
            coordinates = get_coordinates(update_new_location)
            if coordinates:
                new_latitude, new_longitude = coordinates

            employee['name'] = new_name
            employee['surname'] = new_surname
            employee['location'] = update_new_location
            employee['latitude'] = new_latitude
            employee['longitude'] = new_longitude
            employee['company'] = new_workplace

            print(f"Pracownik  {Jakiego_pracownika_szukasz} zostało zaktualizowane.")
            return
        print(f"Pracownik {Jakiego_pracownika_szukasz} nie zostało znalezione.")


import requests
from bs4 import BeautifulSoup


def get_coordinates(location):

    url: str = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, "html.parser")
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    return [latitude, longitude]


def map_all_companies(companies_list):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for company in companies_list:
        url = (f"https://pl.wikipedia.org/wiki/{company['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{company['name']},\n{company['location']}",
                      icon=folium.Icon(color='green')).add_to(map)

    map.save(f'map_companies.html')


def map_all_customers(customers_list):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for customer in customers_list:
        url = (f"https://pl.wikipedia.org/wiki/{customer['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{customer['name']},\n{customer['location']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map_customers.html')


def map_all_employees(employees_list):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for employee in employees_list:
        url = (f"https://pl.wikipedia.org/wiki/{employee['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{employee['name']},\n{employee['location']}",
                      icon=folium.Icon(color='red')).add_to(map)

    map.save(f'map_employees.html')


def map_single_company(companies_list):
    company_name = input("wprowadz nazwe firmy do wyświetlenia na mapie: ").strip()

    selected_company = None
    for company in companies_list:
        if company['name'].lower() == company_name.lower():
            selected_company = company
            break

    if selected_company is None:
        print(f"Firma '{company_name}' nie zostało znalezione.")
        return

    location = selected_company['location']
    latitude = selected_company['latitude']
    longitude = selected_company['longitude']

    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{company_name}', icon=folium.Icon(color='green')).add_to(
        map)
    map_filename = f'map_{company_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")


def map_single_customer(customers_list):
    customer_name = input("wprowadz imie pracownika do wyświetlenia na mapie: ").strip()

    selected_customer = None
    for company in customers_list:
        if company['name'].lower() == customer_name.lower():
            selected_customer = company
            break

    if selected_customer is None:
        print(f"pracownik '{customer_name}' nie został znaleziony.")
        return

    location = selected_customer['location']
    latitude = selected_customer['latitude']
    longitude = selected_customer['longitude']

    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{customer_name}', icon=folium.Icon(color='blue')).add_to(
        map)
    map_filename = f'map_{customer_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")


def map_single_employee(employees_list):
    employee_name = input("wprowadz imie klienta do wyświetlenia na mapie: ").strip()

    selected_employee = None
    for employee in employees_list:
        if employee['name'].lower() == employee_name.lower():
            selected_employee = employee
            break

    if selected_employee is None:
        print(f"klient '{employee_name}' nie został znaleziony.")
        return

    location = selected_employee['location']
    latitude = selected_employee['latitude']
    longitude = selected_employee['longitude']

    print(f"Szerokość: {longitude}, Długość: {latitude}")

    map = folium.Map(location=[longitude, latitude], zoom_start=11)
    folium.Marker(location=[longitude, latitude], popup=f'{employee_name}', icon=folium.Icon(color='red')).add_to(
        map)
    map_filename = f'map_{employee_name}.html'
    map.save(map_filename)
    print(f"Mapa została zapisana jako {map_filename}")


def assign_customers_to_companies(companies_list, customers_list):
    companies_customer = {company['name']: [] for company in companies_list}

    for customer in customers_list:
        my_company = customer.get('my_company')
        if my_company and my_company in companies_customer:
            companies_customer[my_company].append(customer)

    for company in companies_list:
        company_name = company['name']
        print(f"Klienci firmy '{company_name}':")
        customers = companies_customer.get(company_name, [])
        if customers:
            for customer in customers:
                print(f" imie: {customer['name']} ,nazwisko: {customer['surname']} ,Korzysta z uslug w ({customer['my_company']})")
        else:
            print("Brak klientów w firmie.")
        print()


def assign_employees_to_companies(companies_list, employees_list):
    companies_employee = {company['name']: [] for company in companies_list}

    for employee in employees_list:
        workplace = employee.get("workplace")
        if workplace and workplace in companies_employee:
            companies_employee[workplace].append(employee)

    for company in companies_list:
        company_name = company['name']
        print(f"Pracownicy firmy '{company_name}':")
        employees = companies_employee.get(company_name, [])
        if employees:
            for employee in employees:
                print(f" imie: {employee['name']} ,nazwisko: {employee['surname']} ,Pracuje w ({employee['workplace']})")
        else:
            print("Brak pracownikow w firmie.")
        print()
