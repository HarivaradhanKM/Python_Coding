def create_list_of_freq_and_companies(companies):
    freq_dictionary = {}
    set_companies = list(set(companies))
    set_companies.sort()

    for each_company in set_companies:
        frequency = companies.count(each_company)
        if frequency in freq_dictionary.keys():
            freq_dictionary[frequency].append(each_company)
        else:
            freq_dictionary[frequency] = [each_company]
    
    list_of_freq_and_companies = list(freq_dictionary.items())
    list_of_freq_and_companies.sort(reverse = True)
    
    return list_of_freq_and_companies

def print_top_n_companies(list_of_freq_and_companies, n):
    companies_in_required_order = []
    
    for freq_and_companies in list_of_freq_and_companies:
        companies_in_required_order.extend(freq_and_companies[1])
    
    for counter in range(n):
        print(companies_in_required_order[counter])

def main():
    companies = input().split()
    n = int(input())
    
    list_of_freq_and_companies = create_list_of_freq_and_companies(companies)
    print_top_n_companies(list_of_freq_and_companies, n)
    
main()