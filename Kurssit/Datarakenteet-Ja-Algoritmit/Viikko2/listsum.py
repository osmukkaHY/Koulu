find_sums=lambda ns,s:[(ss:=sum(ns[:s]))]+[(ss:=ss+ns[i]-ns[i-s])for i in range(s,len(ns))]

