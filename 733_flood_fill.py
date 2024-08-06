class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        start_color=image[sr][sc]
        
        def floodfill(x,y):
            if x < 0 or x >= len(image):
                return
            if y < 0 or y >= len(image[0]):
                return
            if image[x][y]!=start_color:
                return 
            if image[x][y]==color:
                return

            image[x][y]=color

            floodfill(x-1,y)
            floodfill(x+1,y)
            floodfill(x,y-1)
            floodfill(x,y+1)


        floodfill(sr,sc)
        return image

s=Solution()
print(s.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))






