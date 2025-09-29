def create_string(pages):
    page_range = lambda rs, re: str(rs) if rs==re else str(rs)+'-'+str(re)
    sorted_list = sorted(list(set(pages)))
    prs = []
    rs = re = sorted_list.pop(0)

    for n in sorted_list:
        if re+1 < n:
            prs.append(page_range(rs, re))
            rs = n
        re = n
    prs.append(page_range(rs, re))

    return ','.join(prs)

