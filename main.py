
'''
Returneaza true daca n este prim si false daca nu.
'''

def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  d = 3
  while d*d <= n:
    if n % d == 0:
      return False
    d += 2
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p = 1
  for i in range(len(lst)):
    p = p * lst[i]
  return p

  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  if y == 0:
    return x
  return get_cmmdc_v1(y , x%y)
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while x != y:
    if x > y:
      x = x-y
    else:
      y = y-x
  return x
  
  
def main():
  while True:
    print('1.  Numar prim sau nu.')
    print('2.  Produsul a unor numere naturale')
    print('3.  CMMDC a doua numere folosind prima varianta de rezolvare. ')
    print('4.  CMMDC a doua numere folosind a  doua varianta de rezolvare. ')
    print('x   Close.')
    print('Alege optiunea:')
    opiune = input()
    if opiune == '1':
      a = int(input('Introduceti numarul:'))
      if is_prime(a) == True:
        print(f'Numarul {a} este prim.')
      else:
        print(f'Numarul {a} nu este prim.')
    elif opiune == '2':
      nr = int(input('Introduceti lungimea sirului:'))
      while nr <= 0:
          if nr == 0:
              print('Sirul este gol.Introduceti o valoare pozitiva pentru lungimea sirului!')
          elif nr < 0:
              'Va rog sa introduceti o valoare pozitiva pentru lungimea sirului!'
          nr=int(input('Introduceti lungimea sirului:'))
      else:
        lst=[int(i) for i in input().split(' ')]
        print(get_product(lst))
    elif opiune == '3':
      x=int(input('Introduceti primul numar:'))
      y=int(input('Intorduceti al doilea numar:'))
      print(f'CMMDC dintre {x} si {y} este {get_cmmdc_v1(x,y)}')
    elif opiune == '4':
      w=int(input('Introduceti primul numar:'))
      z=int(input('Intorduceti al doilea numar:'))
      print(f'CMMDC dintre {w} si {z} este ',get_cmmdc_v2(w,z))
    elif opiune == 'x': break

if __name__ == '__main__':
  main()
