import hashlib


def find_zero_collision_from_salt(salt, number_of_zeros):

    collision_output=[0]*10
    indices=[0]*10
    k=1
    i=1
    while k!=0:
        m = hashlib.md5()
        m.update(salt+str(i))

        if [m.hexdigest()[:number_of_zeros]]==['0'*number_of_zeros]:

            index=m.hexdigest()[number_of_zeros]

            if index.isdigit():
                if indices[int(index)]==0:
                    indices[int(index)]='1'
                    collision_output[int(index)]=m.hexdigest()[i%32]
        i=i+1

        if set(indices)==set(['1']*10):
            k=0
    print collision_output

    f1 = open('./collision_output.txt', 'w+')
    f1.write(str(collision_output))
    f1.close()

    return collision_output


find_zero_collision_from_salt("code-quality", 3)