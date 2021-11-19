import operator


def top_ten_check(bnf_codes):
    top_ten_practices={'paracetamol': [],'melatonin': [],'prednisolone':[]}

    for chemical, values in bnf_codes.items():
        temp_pracices_counter=dict()
        for value in values:
            if len(value)==1:
                top_ten_practices[chemical].append(value)
            else:
                if value[0] not in temp_pracices_counter:
                    temp_pracices_counter[value[0]]=value[1]
                else:
                    temp_pracices_counter[value[0]]+=value[1]
        temp_top=dict(sorted(temp_pracices_counter.items(), key=operator.itemgetter(1),reverse=True))
        temp_top_ten=list(temp_top.items())[:10]                
        top_ten_practices[chemical].append(temp_top_ten)
    # print(top_ten_practices)
    return top_ten_practices    
    
