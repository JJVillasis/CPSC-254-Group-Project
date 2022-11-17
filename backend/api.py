from ELSPAY import Elsa


def main():

    print('Welcome to Source Finder!')
    print('The purpose of this program is to help find reliable sources for a specific topic.')
    query = input('Please enter the topic or theme you would like to search.(ex: global warming): ')
    elsa = Elsa(query)
    results = elsa.search()
    for result in results:
        for r in result:
            print(result[r])

        print('---------------------------------------------------------------------')

    # return results
    
main()