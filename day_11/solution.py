from monkey import test_data, input_state
from tqdm import tqdm

rounds = 10_000
data = input_state

def main():
    for round in tqdm(range(rounds), total=rounds, unit="rounds"):
        for n in range(len(data)):
            data[n].processTurn(data)
        # print(f"Round: {n}")
        # print(*[f"Monkey {index}: {mon.items}" for index, mon in enumerate(test_data)], sep='\n')
    
    top_two = sorted([mon.item_count for mon in data], reverse=True)[0:2]
    print(top_two[0] * top_two[1])
    

if __name__ == "__main__":
    main()