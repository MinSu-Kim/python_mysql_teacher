from dml.coffee_procedure import call_sale_stat_sp, call_order_price_by_issale

if __name__ == "__main__":
    # create_procedure()
    call_sale_stat_sp('proc_sale_stat')
    print()
    call_order_price_by_issale('proc_saledetail_orderby', False)
    print()
    call_order_price_by_issale('proc_saledetail_orderby', True)

    # transaction_fail1()
    # transaction_fail2()
    # transaction_success()

    # select_sql = "select code, name from product where code like 'C___'"
    # res = query_with_fetchall2(select_sql)
    # columns_list = ['code', 'name']
    # df = pd.DataFrame(res, columns=columns_list)
    # print(df)
    #
    # delete_sql = "delete from product where code = %s"
    # delete_product(delete_sql, 'C004')
    #
    # for code, name in (query_with_fetchall2(select_sql)):
    #     print(code, " ", name)

    # select_sql = "select * from product"
    # query_with_fetchone(select_sql)
    # query_with_fetchall(select_sql)
    # res = query_with_fetchall2(select_sql)
    # print(type(res), 'size = ',  len(res))
    # for pno, pname in res:
    #     print(pno, pname)
    # query_with_fetchmany(select_sql)

    # insert_sql = "Insert into product values(%s, %s)"

    # query_with_fetchall(select_sql)
    # insert_product(insert_sql, 'C001', '라떼')
    # query_with_fetchall(select_sql)

    # products = [('C002', '라떼2'), ('C003', '라떼3'), ('C004', '라떼4')]
    # insert_products(insert_sql, products)
    # query_with_fetchall(select_sql)

    # select_sql_by_code = "select code, name from product where code = '{code}'".format(code='C001')
    # query_with_fetchone(select_sql_by_code)
    #
    # update_sql = "update product set name = %s where code = %s"
    # update_product(update_sql, '라떼수정', 'C001')
    #
    # query_with_fetchone(select_sql_by_code)


