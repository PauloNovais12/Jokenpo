counts=["92,google.com.br","889,yahoo.com.br","600,facebook.com.br","7,youtube.com.br", "1600,ojogos.com.br", "1350,netflix.com.br"]
for i in counts:
    clicks, sites= [],[]
    for u in i:
        try: # verificador de numeros inteiros numa string
            if(int(u)!=False or int(u)==0):
                clicks.append(u)
        except:
                sites.append(u)
    clicks= "".join(clicks)
    sites= "".join(sites[1:])
    print("{}           {}".format(sites,clicks))



