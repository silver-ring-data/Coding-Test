def solution(arr):
    
    result = [value 
              for index, value in enumerate(arr) 
              if index == 0 or value != arr[index-1]
              ]
       
    return result