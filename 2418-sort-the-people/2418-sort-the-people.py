class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        result= list(zip(heights, names))

        result =sorted(result, reverse =True)

        just_names = [n for h, n in result ]
        return just_names

        

