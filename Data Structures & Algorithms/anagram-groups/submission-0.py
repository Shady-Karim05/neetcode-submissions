class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        res=[]
        for i in strs:
            d={}
            for j in i:
                if j in d:
                    d[j]=d[j]+1
                else:
                    d[j]=1
            keys=tuple(sorted((d.items())))
            if keys in di:
                di[keys].append(i)
            else:
                di[keys]=[i]
        return list(di.values())