from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1
        Output: 500

        Using BFS: O(n * k)
            Start at 0

                          1     2    3
             0           200   inf   inf        stop = 0
             1           200   300   500        stop = 1          
                    
        Create an array prices and assign the float * n
        Assing prices[src] = 0
        stop =

        Ininiate an adj = {[i:[] for i in range(n)}
        Iterate thru s, d, p in flight
            add to the adj[s] with (d,p)
        
        while q and stop <= k:
                for i in range(len(q)):
                    pop city and cost (where we are, and how much)

                    #Go to the hashmap and find it nei
                    Iterate thru the nei, p in the adj[city]
                        newCost = cost + p
                    
                    if newCost < price[nei]
                        price[nei] < nextCost
                        q.append((nei, newCost))
            stop += 1
        return prices[dst] if prices[dst] != float else -1
        """
        prices = [float("inf")] * n
        prices[src] = 0

        adj = {i: [] for i in range(n)}

        for s, d, p in flights:
            adj[s].append((d, p))

        q = deque([(src, 0)])

        stop = 0

        while q and stop <= k:
            for _ in range(len(q)):
                city, cost = q.popleft()

                for nei, price in adj[city]:
                    newCost = cost + price

                    if newCost < prices[nei]:
                        prices[nei] = newCost
                        q.append((nei, newCost))

            stop += 1

        return prices[dst] if prices[dst] != float("inf") else -1
