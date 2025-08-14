# Fractional Knapsack Problem: refer https://takeuforward.org/data-structure/fractional-knapsack-problem-greedy-approach/

class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight
        self.Ratio = value /weight
class FractionalKnapsack:
    def __init__(self,capacity):
        self.capacity = capacity
    def getMaxValue(self, items):
        items.sort(key= lambda x: x.Ratio, reverse=True)
        total_value= 0
        for item in items:
            if self.capacity >= item.weight:
                self.capacity -= item.weight
                total_value += item.value
            else:
                total_value += item.Ratio * self.capacity
                break
        return total_value
arr = [Item(60,10), Item(100,20), Item(120,30)]
capacity = 50
knapsack = FractionalKnapsack(capacity)
max_value = knapsack.getMaxValue(arr)
print(f"Maximum value in Knapsack = {max_value}")