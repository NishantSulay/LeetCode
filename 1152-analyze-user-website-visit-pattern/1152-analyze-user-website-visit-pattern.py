class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        #Let's find for every user separately the websites he visited.

        
#         hashmap = {}
#         for i in range(len(username)):
#             if username[i] in hashmap:
#                 hashmap[username[i]] += [website[i]]
#             else:
#                 hashmap[username[i]] = [website[i]] 

            
#         #find minimum pattern length
#         pattern_min = float('inf')                
                
#         for i in hashmap:
#             temp_min = len(hashmap[i])
#             if temp_min < pattern_min:
#                 pattern_min = temp_min
        
#         #Consider all possible 3-sequences, find the number of distinct users who visited each of them.
#         '''
#         The pattern ("home", "about", "career") has score 2 (joe and mary).
#         The pattern ("home", "cart", "maps") has score 1 (james).
#         The pattern ("home", "cart", "home") has score 1 (james).
#         The pattern ("home", "maps", "home") has score 1 (james).
#         The pattern ("cart", "maps", "home") has score 1 (james).
        
                
         
#         ['home', 'about', 'career']
#         ['home', 'cart', 'maps', 'home']
#         ['home', 'about', 'career']
        
#         '''

#         #create list of subarrays of length 3 given list of visited websites for each user
#         #from list of subarrays, count the number of subarrays that equal as store as the score 
        
        
        user_website = collections.defaultdict(list)
        counter = collections.defaultdict(int)
        
        tuw = tuple(zip(timestamp, username, website))
        tuw_sorted = sorted(tuw)
        
        for timestamp, username, website in tuw_sorted:
            user_website[username].append(website)
            counter[username] += 1
        
        
        three_seq_map = collections.defaultdict(int)
        
        for username, website in user_website.items():
            visited = set()

            for i in range(counter[username]):
                for j in range(i+1, counter[username]):
                    for k in range(j+1, counter[username]):
                        three_seq = (website[i], website[j], website[k])
                        
                        if three_seq in visited:
                            continue
                        visited.add(three_seq)
                        three_seq_map[three_seq] += 1
                        
        ans = sorted(three_seq_map.items(), reverse = True, key=lambda x : (-x[1],x[0]))
        
        return ans[-1][0]
            
          
        
        
