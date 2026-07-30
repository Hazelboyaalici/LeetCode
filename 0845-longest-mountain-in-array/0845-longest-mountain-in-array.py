class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        down=0
        up=0
        best=0

        for i in range(1, len(arr)):

            #down

            if arr[i] < arr[i-1]:

                if up == 0: # ilk down, daha önce up yok
                    down =1
                else: 
                    down +=1
            
            # up
            elif arr[i] > arr[i-1]:
            
                if down >0:
                    down =0
                    up =1
                else:
                    up +=1
            
            else:
                up=0
                down = 0
            

            if down >0 and up >0:
                best = max (best, up + down + 1)
        return best


