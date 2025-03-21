from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        found = []
        
        notFound = {}

        for i in range(len(recipes)):
            ingredientFound = set()
            for item in ingredients[i]:
                if item in supplies:
                    ingredientFound.add(item)
                else:
                    if i in notFound:
                        notFound[i].append(item)
                    else:
                        notFound[i] = [item]
                    
                    
            if len(ingredientFound) == len(ingredients[i]):
                found.append(recipes[i]) 
        for item, value in notFound.items():
            add = True
            for stuff in value:
                if stuff not in found:
                    add = False
                    break
            if add:
                found.append(recipes[i])
        
        return found
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]          
solution = Solution()
print(solution.findAllRecipes(recipes, ingredients, supplies))