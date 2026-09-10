class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        buckets=[[] for _ in range(len(nums)+1)]
        for num,freq in d.items():
            buckets[freq].append(num)
        res=[]
        for frq in range(len(nums),0,-1):
            for p in buckets[frq]:
                res.append(p)
                if len(res)==k:
                    return res


        