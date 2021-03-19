import json


def category_fee(i):
    category_fees = []
    # calculate prices module,Logic to calculate the fee
    # Category_fee =Session fee + Minimum billing+ Maximum session fee

    # print(i['session Fee'], i['max_session fee'], i['min billing amount'])
    if i['max_session fee'] == 'False' and i['min billing amount'] == 'False' and i['session Fee'] != 'False':
        category_fee_a = float(i['session Fee'].replace(",", ""))
        category_fees.append(category_fee_a)
    elif i['max_session fee'] == 'False' and i['min billing amount'] != 'False' and i['session Fee'] == 'False':
        category_fee_b = float(i['min billing amount'].replace(",", ""))
        category_fees.append(category_fee_b)
    elif i['max_session fee'] != 'False' and i['min billing amount'] != 'False' and i['session Fee'] == 'False':
        category_fee_c = float(i['min billing amount'].replace(",", "")) + float(
            i['max_session fee'].replace(",", ""))
        category_fees.append(category_fee_c)
    elif i['max_session fee'] != 'False' and i['min billing amount'] != 'False' and i['session Fee'] != 'False':
        category_fee_d = float(i['session Fee'].replace(",", "")) + float(
            i['min billing amount'].replace(",", "")) + float(i['max_session fee'].replace(",", ""))
        category_fees.append(category_fee_d)
    elif i['max_session fee'] == 'False' and i['min billing amount'] == 'False' and i['session Fee'] == 'False':
        category_fee_e = 0
        category_fees.append(category_fee_e)

    return category_fees


def Category_time(i):
    Category_times = []
    # calculate ,Logic to calculate the category time
    # Category_time =Duration * Minute price

    # simple calculation of time

    if i['has complex minute price'] == 0:
        c = i['simple minute price'].replace(",", "")
        category_time_a = float(i['min_duration']) * float(c)
        Category_times.append(category_time_a)
    else:
        pass

    return Category_times


def Category_kWh(i):
    Category_kWhs = []
    # calculate category kWh ,Logic to calculate the category KWh
    # Category_kWh =Consumed kWh * kWh price

    # simple calculation of time
    if i['has complex minute price'] == 0:
        category_kWh_a = float(i['min_duration']) * float(i['kwh Price'])
        Category_kWhs.append(category_kWh_a)

    # when complex
    else:
        category_kWh_b = float(i['min_duration']) * float(i['time_price']['kwh price'])
        Category_kWhs.append(category_kWh_b)

    return Category_kWhs


def transaction_data(i):
    session_ids = []
    supplier_price_ids = []

    for i1 in Transactions_data:
        if i1['EVSEID'] == i['EVSE ID']:
            session_ids.append(i1['Session ID'])
            supplier_price_ids.append(i1['Proveider ID'])
            break

    return session_ids, supplier_price_ids


def final_result(category_fee, category_time, category_kWh, session_id, supplier_price_id):
    # calculate the total fee charged

    Total_fee = category_fee + category_time + category_kWh

    # to fetch the session id and the provider id from the transactions data

    final_result_sample = {

        "fee_price": category_fee,
        "time_price": Category_time,
        "kwh_price": Category_kWh,
        "total_price": Total_fee,
        "session_id": session_id,
        "supplier_price_id": supplier_price_id
    }

    return final_result_sample


# main driver
if __name__ == '__main__':
    # Opening JSON file
    f = open('data.json', )

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # two cleaned list for supplier and transactions, parsed data

    Supplier_prices_data = data["supplier_prices"]

    Transactions_data = data["transactions"]
    while True:
        test = 0

        for i in Supplier_prices_data:
            # print(i)
            category_fee_final = category_fee(i)
            category_time_final = Category_time(i)
            category_kWh_final = Category_kWh(i)
            session_id_final, supplier_price_id_final = transaction_data(i)
            final_result_json = final_result(category_fee_final, category_time_final, category_kWh_final, session_id_final,
                                             supplier_price_id_final)

            print(final_result_json)

        if test == 4:
            break
