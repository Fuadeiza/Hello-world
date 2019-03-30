import math
import matplotlib.pyplot as plt

'''diam=input("Input your 5 values for diameter re-occuring thrice\n:")
diame=diam.split()
dia=[]
for i in diame:
  new_dia=int(i)
  dia.append(new_dia)
print(dia)


thic=input("Input your 15 values for diameter\n:")
thickn=thic.split()
thickness=[]
for th in :
  new_th=int(th)
  thickness.append(new_th)
print(thickness)'''

diff_k=[]
for t in range(1,len(dia)):
    D=dia[t]
    k=round(float(((1+(D/(2*t))) * math.log((D+t)/(D-t)))),3)
    diff_k.append(k)

print(diff_k)

kf=diff_k[4:15]
force=[20,25,30,35,40,45,50,55,60,65]
length=[6,7,8,9,10,11,12,13,14,15]
diameter=dia[4:14]
#thickness=[0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]
crsh_fact=[]


print(crsh_fact)

def cfd(): #cross sectional factor against Diameter
    plt.xlabel("diameter in m")
    plt.ylabel("K cross sectional factor")
    plt.plot(kf,diameter)
    return plt.show()


def cft():
    plt.xlabel("thickness in m")
    plt.ylabel("K cross sectional factor")
    plt.plot(kf,thickness)
    return plt.show()

# Now, we vary different parameter against crushing strength

def csf(L,t,k,D):# crushing strength against force
    for F in force:
        #L=input(int("input your value of L in m"))
        #t=input(int("input your value for thickness in m"))
        #k=input(int("int(your crushing factor")))
        crsh_fct=round(float(((F/(L*t)) * ((1/(math.pi*(1+k)))) * (1+ ((1/k) * (t/(D+t)))))),3)
        crsh_fact.append(crsh_fct)
    print("The elements of the crushing factor are:",crsh_fact)
    print("The elements of the forces are:",force)
    plt.xlabel("Force in N")
    plt.ylabel("Crushing Strength in N/m**2")
    plt.plot(crsh_fact,force)
    return plt.show()

def csl(F,t,k,D): #crushing strength against length
    for L in length:
        crsh_fct=round(float(((F/(L*t)) * ((1/(math.pi*(1+k)))) * (1+ ((1/k) * (t/(D+t)))))),3)
        crsh_fact.append(crsh_fct)
    print("The elements of the crushing factor are:",crsh_fact)
    print("The elements of the length are:", length)
    plt.xlabel("Length in m")
    plt.ylabel("Crushing Strength in N/m**2")
    plt.plot(crsh_fact,length)
    return plt.show()

def csd(F,t,L,K): # crushing strength against diameter
    for d in diameter:
        crsh_fct=round(float(((F/(L*t)) * ((1/(math.pi*(1+k)))) * (1+ ((1/k) * (t/(D+t)))))),3)
        crsh_fact.append(crsh_fct)
    print ("The elements in crushing factor are:",crsh_fact)
    print("The elements in diameter are:",diameter)
    plt.xlabel("Diameter in m")
    plt.ylabel("Crushing Strength in N/m**2")
    plt.plot(crsh_fact,diameter)
    return plt.show()

def cst(F,L,k,D): # crushing strength against thickness
    for t in thickness:
        crsh_fct=round(float(((F/(L*t)) * ((1/(math.pi*(1+k)))) * (1+ ((1/k) * (t/(D+t)))))),3)
        crsh_fact.append(crsh_fct)
    print("The elements in crushing factor are:",crsh_fact)
    print("The elements in thickness are:",thickness)
    plt.xlabel("Thickness in m")
    plt.ylabel("Crushing Strength in N/m**2")
    plt.plot(crsh_fact,thickness)
    return plt.show()

def csk(F,D,t,L): # crushing strength against cross section factor
    for k in kf:
        crsh_fct=round(float(((F/(L*t)) * ((1/(math.pi*(1+k)))) * (1+ ((1/k) * (t/(D+t)))))),3)
        crsh_fact.append(crsh_fct)
    print("the elements of crushing factor are:",crsh_fact)
    print("The element of cross section factor are:",kf)
    plt.xlabel("cross section factor")
    plt.ylabel("Crushing Strength in N/m**2")
    plt.plot(crsh_fact,kf)
    return plt.show()
  