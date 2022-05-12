import re

while True:
    try:
        s = input().rstrip()
        sc, mcv, op = s.split(";")
        if sc == 'S' and mcv == 'M':
            result = re.split('(?=[A-Z])', op[:-2])
            finalResult = ' '.join([i.lower() for i in result])
            print(finalResult)
        if sc == "C" and mcv == "V":
            res = []
            list = op.split(' ')
            for i in range(len(list)):
                if i == 0:
                    res.append(list[i].lower())
                else:
                    res.append(list[i].capitalize())
            ans = "".join(i for i in res)
            print(ans.rstrip())
        if sc == "C" and mcv == "C":
            res = []
            lst = [i.capitalize() for i in op.split(' ')]
            print(' '.join(lst))
        if sc == "S" and mcv == "C":
            res = re.split('(?=[A-Z])', op)[1:]
            print(' '.join([i.lower() for i in res]))
        if sc == "C" and mcv == "M":
            op = [i.capitalize() for i in op.split(' ')]
            op.append('()')
            res = []
            for i in range(len(op)):
                if i == 0:
                    res.append(op[i].lower())
                else:
                    res.append(op[i].capitalize())
            print(''.join(res))
        if sc == "S" and mcv == "V":
            op = re.split('(?=[A-Z])', op)
            print(' '.join([i.lower() for i in op]))

    except EOFError:
        break
