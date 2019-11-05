def konwersjaRGB(r,g,b):
    rPrim=r/255
    gPrim=g/255
    bPrim=b/255

    tab=[rPrim,gPrim,bPrim]
    Cmax=max(tab)
    Cmin=min(tab)
    delta=Cmax-Cmin

    h=0
    s=0
    v=Cmax
    v*=100
    if delta==0:
        h=0
    elif Cmax==rPrim:
        h=(((gPrim-bPrim)/delta)%6)*60
    elif Cmax==gPrim:
        h=(((bPrim-rPrim)/delta)+2)*60
    elif Cmax==bPrim:
        h=(((rPrim-gPrim)/delta)+4)*60

    if Cmax==0:
        s=0
    elif Cmax!=0:
        s=delta/Cmax
        s*=100
    
    wynik=[round(h),round(s,1),round(v,1)]
    wynik=tuple(wynik)
    print(wynik)

konwersjaRGB(100,243,98)
        


