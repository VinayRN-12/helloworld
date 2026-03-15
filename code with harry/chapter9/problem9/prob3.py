# generate a table from 2 to 20
def generate_tables(n):
    table=""
    for i in range(1,11):
        table += f"{n}X{i}={n*i}\n"
    with open(f"tables/table_{n}.txt","w")as f:
        f.write(table)

for i in range(2,21):
    generate_tables(i)

