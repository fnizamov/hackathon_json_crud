from hackathon_json_crud import (
    create,
    delete,
    get_all_data,
    get_data_by_id,
    clear,
    update
)



if __name__ == '__main__':
    print("""                     
                            Добро пожаловать в Makers Store
                    Выберите операцию, которую хотите совершить (1-7):""")

    while True:
        operation = input("""
            1. create   - создать новый продукт
            2. delete   - удалить продукт по id
            3. list     - получить список всех продуктов
            4. retrieve - получить продукт по id
            5. clear    - очистить базу данных
            6. update   - изменить данные
            7. exit     - выйти из программы 
            
            Выберите цифру в зависимости от необходимой операции и нажмите Enter: """)
        if operation == '1':
            create()
        elif operation == '2':
            print(delete())
        elif operation == '3':
            print(get_all_data())
        elif operation == '4':
            print(retrieve_prod())
        elif operation == '5':
            print(clear())
        elif operation == '6':
            print(update())
        elif operation == '7':
            print("""
                       ---> До свидания! С уважением Makers Store. <---""")
            break
        else:
            print('Вы выбрали неверное действие! Попробуйте еще раз или выберите exit (7) для выхода')
    # print(get_all_data())
    # print(create())
    # print(get_data_by_id())
    # print(delete())
    # print(update())