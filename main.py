from crud import show_company, show_customer, show_employee, add_new_company, add_new_customer, add_new_employee, \
    update_company, update_customer, update_employee, remove_company, remove_customer, remove_employee, \
    map_single_company, map_single_customer, map_single_employee, map_all_companies, map_all_customers, \
    map_all_employees, assign_customers_to_companies, assign_employees_to_companies
from data import companies, customers, employees

if __name__ == '__main__':
    print('Logowanie')
    print('Login: Nazwisko twórcy')
    print('Haslo: grupa wydzialowa')
    print('')

    Login = "GOSCINSKI"
    Haslo = "WIG23GW1S0"
    login: str = input("Podaj login:")
    haslo: str = input("Podaj haslo:")
    if Login == login and Haslo == haslo:
        print("Sukces")
    else:
        print("Blędny login lub haslo")
        login: str = input("Podaj login:")
        haslo: str = input("Podaj haslo:")

while True:
    print('0. zakoncz program ')
    print('1. wyswietl centra badawcze ')
    print('2. dodaj centrum badawcze ')
    print('3. usun centrym badawcze ')
    print('4. centrum badawcze do aktualizacji')
    print('5. mapa pokazujaca jedna firme')
    print('6. mapa wszystkich firm')
    print('')
    print('11. wyswietl klientow')
    print('22. dodaj klienta')
    print('33. usun klienta')
    print('44. klient do aktualizacji')
    print('55. mapa pokazujaca jednego pracownika')
    print('66. mapa wszystkich pracownikow')
    print('77. lista klientow i firmy zakontraktowane')
    print('')
    print('111. wyswietl pracownikow')
    print('222. dodaj pracownika')
    print('333. usun pracownika')
    print('444. pracownik do aktualizacji')
    print('555. mapa pokazujaca jednego klienta')
    print('666. mapa wszystkich klientow')
    print('777. lista pracownikow i miejsca ich pracy')

    menu_option = input('wybierz opcje menu: ')
    if menu_option == '0': break
    if menu_option == '1': show_company(companies)
    if menu_option == '2': add_new_company(companies)
    if menu_option == '3': remove_company(companies)
    if menu_option == '4': update_company(companies)
    if menu_option == '5': map_single_company(companies)
    if menu_option == '6': map_all_companies(companies)
    if menu_option == '11': show_customer(customers)
    if menu_option == '22': add_new_customer(customers)
    if menu_option == '33': remove_customer(customers)
    if menu_option == '44': update_customer(customers)
    if menu_option == '55': map_single_customer(customers)
    if menu_option == '66': map_all_customers(customers)
    if menu_option == '77': assign_customers_to_companies(companies, customers)
    if menu_option == '111': show_employee(employees)
    if menu_option == '222': add_new_employee(employees)
    if menu_option == '333': remove_employee(employees)
    if menu_option == '444': update_employee(employees)
    if menu_option == '555': map_single_employee(employees)
    if menu_option == '666': map_all_employees(employees)
    if menu_option == '777': assign_employees_to_companies(companies, employees)
