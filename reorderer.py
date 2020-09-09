import pandas as pd


if __name__ == '__main__':
    number_of_pages = 114


    pages_list = []
    keyword_list = []
    pg = -1

    for pg in range(0, 115):
        file = "wardrobe.txt"
        f = open('./outputs/{}'.format(file))
        for line in f:

            page_search_orig_lst = line.split(',')
            p_search = page_search_orig_lst[0].split('Pattern Found on Page: ')
            page_find = p_search[1]
            page_find2 = int(page_find)

            keyword_temp = page_search_orig_lst[1].split('\n')
            keyword = keyword_temp[0]

            print(pg)

            if page_find2 == pg:
                print("{} does equal {}".format(pg, page_find2))
                pages_list.append(page_find2)
                keyword_list.append(keyword)
        f.close()



    dataframe = pd.DataFrame(pages_list, keyword_list)

    print(dataframe)

    export = pd.DataFrame.to_csv(dataframe,'outputs/ordered_wardrobe.csv')
