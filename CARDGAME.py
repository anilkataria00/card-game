import random
a = ['ace(diamond)','2(diamond)','3(diamond)','4(diamond)','5(diamond)','6(diamond)','7(diamond)','8(diamond)','9(diamond)','10(diamond)','jack(diamond)','queen(diamond)','king(diamond)',
     'ace(heart)','2(heart)','3(heart)','4(heart)','5(heart)','6(heart)','7(heart)','8(heart)','9(heart)','10(heart)','jack(heart)','queen(heart)','king(heart)',
     'ace(spades)','2(spades)','3(spades)','4(spades)','5(spades)','6(spades)','7(spades)','8(spades)','9(spades)','10(spades)','jack(spades)','queen(spades)','king(spades)',
     'ace(club)','2(club)','3(club)','4(club)','5(club)','6(club)','7(club)','8(club)','9(club)','10(club)','jack(club)','queen(club)','king(club)']
random.shuffle(a)
print()
l = [a[i] for i in range(20,29)]
for cards in l:
    print(cards,end=', ')
print()
print()
print('Select one card from the above list')
print()
print('Type "YES" if you have selected a card')
w = input()
if w == "YES":
    l1 = [l[i] for i in range(0,3)]
    l2 = [l[i] for i in range(3,6)]
    l3 = [l[i] for i in range(6,9)]
    for cards in l1:
        print(cards,end=' ')
    print()
    print('[Type "YES" if your card in the list and "NO" if it is not:]')
    x1 = input()
    if x1 == "YES":
        b1 = [l3[2], l1[2], l2[2]]
        b2 = [l3[1], l1[1], l2[1]]
        b3 = [l3[0], l1[0], l2[0]]
        for cards in b1:
            print(cards,end=' ')
        print()
        print('Type "YES" if your card in the list and "NO" if it is not:')
        x2 = input()
        if x2 == "YES":
            c1 = [l2[0], l2[2], l2[1]]
            c2 = [l1[0], l1[2], l1[1]]
            c3 = [l3[0], l3[2], l3[1]]
            for cards in c1:
                print(cards, end=' ')
            print()
            print('Type "YES" if your card in the list and "NO" if it is not:')
            y2 = input()
            if y2 == "Yes":
                print(f'Your card is {l2[2]}')
            if y2 == "NO":
                for cards in c2:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y3 = input()
                if y3 == "YES":
                   print(f' Your card is {l1[2]}')
                if y3 == "NO":
                   for cards in c3:
                       print(cards,end= ' ')
                   print()
                   print('Type "YES" if your card in the list and "NO" if it is not:')
                   y4 = input()
                   if y4 == "YES":
                       print(f'Your card is {l3[2]}')
                   if y4 == "NO":
                       print('You were lying')
        if x2 == "NO":
            for cards in b2:
                print(cards, end=' ')
            print()
            print('Type "YES" if your card in the list and "NO" if it is not:')
            y5 = input()
            if y5 == "YES":
                c1 = [l2[2], l2[1], l2[0]]
                c2 = [l1[2], l1[1], l1[0]]
                c3 = [l3[2], l3[1], l3[0]]
                for cards in c1:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y6 = input()
                if y6 == "YES":
                    print(f'Your card if {l2[1]}')
                if y6 == "NO":
                    for cards in c2:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y7 = input()
                    if y7 == "YES":
                        print(f'Your card is{l1[1]}')
                    if y7 == "NO":
                        for cards in c3:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y8 = input()
                        if y8 == "YES":
                            print(f'Your card is {l3[1]}')
                        if y8 == "NO":
                            print('You were lying')
            if y5 == "NO":
                for cards in b3:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y9 = input()
                if y9 == "YES":
                    c1 = [l2[1], l2[0], l2[2]]
                    c2 = [l1[1], l1[0], l1[2]]
                    c3 = [l3[1], l3[0], l3[2]]
                    for cards in c1:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y10 = input()
                    if y10 == "YES":
                        print(f'Your card is {l2[0]}')
                    if y10 == "NO":
                        for cards in c2:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y11 = input()
                        if y11 == "YES":
                            print(f'Your card is {l1[0]}')
                        if y11 == "NO":
                            for cards in c3:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y12 = input()
                            if y12 == "YES":
                                print(f'Your card is {l3[0]}')
                            if y12 == "NO":
                                print('You were lying')
                if y9 == 'NO':
                    print('You were lying')

    if x1 == "NO":
        for cards in l2:
            print(cards, end=' ')
        print()
        print('Type "YES" if your card in the list and "NO" if it is not:')
        x2 = input()
        if x2 == "YES":
            b1 = [l1[2], l2[2], l3[2]]
            b2 = [l1[1], l2[1], l3[1]]
            b3 = [l1[0], l2[0], l3[0]]
            for cards in b1:
                print(cards, end=' ')
            print()
            print('Type "YES" if your card in the list and "NO" if it is not:')
            y1 = input()
            if y1 == "YES":
                c1 = [l3[0], l3[2], l3[1]]
                c2 = [l2[0], l2[2], l2[1]]
                c3 = [l1[0], l1[2], l1[1]]
                for cards in c1:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y2 = input()
                if y2 == "YES":
                    print(f'Your card is {l3[2]}')
                if y2 == 'NO':
                    for cards in c2:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y3 = input()
                    if y3 == 'YES':
                        print(f'Your card is {l2[2]}')
                    if y3 == 'NO':
                        for cards in c3:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y4 = input()
                        if y4 == 'YES':
                            print(f'Your card is {l1[2]}')
                        if y4 == 'NO':
                            print('You were lying')
            if y1 == 'NO':
                for cards in b2:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y5 = input()
                if y5 == "YES":
                    c1 = [l3[2], l3[1], l3[0]]
                    c2 = [l2[2], l2[1], l2[0]]
                    c3 = [l1[2], l1[1], l1[0]]
                    for cards in c1:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y6  = input()
                    if y6 == "YES":
                        print(f'Your card is {l3[1]}')
                    if y6 == "NO":
                        for cards in c2:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y7 = input()
                        if y7 == 'YES':
                            print(f'Your card is {l2[1]}')
                        if y7 == 'NO':
                            for cards in c3:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y8 = input()
                            if y8 == 'YES':
                                print(f'Your card is {l1[1]}')
                            if y8 == 'NO':
                                print('You were lying')
                if y5 == 'NO':
                    for cards in b3:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y9 = input()
                    if y9 == "YES":
                        c1 = [l3[1], l3[0], l3[2]]
                        c2 = [l2[1], l2[0], l2[2]]
                        c3 = [l1[1], l1[0], l1[2]]
                        for cards in c1:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y10 = input()
                        if y10 == 'YES':
                            print(f'Your card is {l3[0]}')
                        if y10 == 'NO':
                            for cards in c2:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y11 = input()
                            if y11 == 'YES':
                                print(f'Your card is {l2[0]}')
                            if y11 == 'NO':
                                for cards in c3:
                                    print(cards, end=' ')
                                print()
                                print('Type "YES" if your card in the list and "NO" if it is not:')
                                y12 = input()
                                if y12 == 'YES':
                                    print(f'Your card is {l1[0]}')
                                if y12 == 'NO':
                                    print('You were lying')
                    if y9 == 'NO':
                        print('You were lying')
        if x2 == 'NO':
            for cards in l3:
                print(cards, end=' ')
            print()
            print('Type "YES" if your card in the list and "NO" if it is not:')
            y1 = input()
            if y1 == 'YES':
                b1 = [l2[2], l3[2], l1[2]]
                b2 = [l2[1], l3[1], l1[1]]
                b3 = [l2[0], l3[0], l1[0]]
                for cards in b1:
                    print(cards, end=' ')
                print()
                print('Type "YES" if your card in the list and "NO" if it is not:')
                y2 = input()
                if y2 == "YES":
                    c1 = [l1[0], l1[2], l1[1]]
                    c2 = [l3[0], l3[2], l3[1]]
                    c3 = [l2[0], l2[2], l2[1]]
                    for cards in c1:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y3 = input()
                    if y3 == "YES":
                        print(f'Your card is {l1[2]}')
                    if y3 == "NO":
                        for cards in c2:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y4 = input()
                        if y4 == "YES":
                            print(f'Your card is {l3[2]}')
                        if y4 == "NO":
                            for cards in c3:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y5 = input()
                            if y5 == "YES":
                                print(f'Your card is {l2[2]}')
                            if y5 == "NO":
                                print('You were lying')
                if y2 == "NO":
                    for cards in b2:
                        print(cards, end=' ')
                    print()
                    print('Type "YES" if your card in the list and "NO" if it is not:')
                    y6 = input()
                    if y6 == "YES":
                        c1 = [l1[2], l1[1], l1[0]]
                        c2 = [l3[2], l3[1], l3[0]]
                        c3 = [l2[2], l2[1], l2[0]]
                        for cards in c1:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y7 = input()
                        if y7 == 'YES':
                            print(f'Your card is {l1[1]}')
                        if y7 == "NO":
                            for cards in c2:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y8 = input()
                            if y8 == "YES":
                                print(f'Your card is {l3[1]}')
                            if y8 == "NO":
                                for cards in c3:
                                    print(cards, end=' ')
                                print()
                                print('Type "YES" if your card in the list and "NO" if it is not:')
                                y9 = input()
                                if y9 == "YES":
                                    print(f'Your card is {l2[1]}')
                                if y9 == "NO":
                                    print('You were lying')
                    if y6 == 'NO':
                        for cards in b3:
                            print(cards, end=' ')
                        print()
                        print('Type "YES" if your card in the list and "NO" if it is not:')
                        y10 = input()
                        if y10 == 'YES':
                            c1 = [l1[1], l1[0], l1[2]]
                            c2 = [l3[1], l3[0], l3[2]]
                            c3 = [l2[1], l2[0], l2[2]]
                            for cards in c1:
                                print(cards, end=' ')
                            print()
                            print('Type "YES" if your card in the list and "NO" if it is not:')
                            y11 = input()
                            if y11 == "YES":
                                print(f'Your card is {l1[0]}')
                            if y11 == 'NO':
                                for cards in c2:
                                    print(cards, end=' ')
                                print()
                                print('Type "YES" if your card in the list and "NO" if it is not:')
                                y12 = input()
                                if y12 == "YES":
                                    print(f'Your card is {l3[0]}')
                                if y12 == "NO":
                                    for cards in c3:
                                        print(cards, end=' ')
                                    print()
                                    print('Type "YES" if your card in the list and "NO" if it is not:')
                                    y13 = input()
                                    if y13 == "YES":
                                        print(f'Yours card is {l2[0]}')
                                    if y13 == "NO":
                                        print('You were lying')
                        if y10 == 'NO':
                            print('You were lying')
            if y1 == 'NO':
                print('You were lying')
print()
print("THANK YOU")