import TreeNode
import sortingAlgorithms as sr
import placedict as pd
def divideCategory(category):
    print(category)
    if 'museums' in category.lower() or 'art' in category.lower():
        return 'Museums'
    if 'historic' in category.lower() or 'religious' in category.lower() or 'landmarks' in category.lower():
        return 'Historic'
    if 'parks' in category.lower() or 'gardens' in category.lower() or 'zoo' in category.lower():
        return 'Parks'
    if 'malls' in category.lower() or 'markets' in category.lower():
        return 'Malls'
    else:
        return 'Others'
def build_Tree(places):
    root = TreeNode.Tree('Places')
    category_map = {}
    for place in places:
        
        name = place['Name']
        ratings = place['Ratings']
        category = place['Category']
        category = divideCategory(category)
        print(category,"is the category assigned")
        if category not in category_map:
            category_map[category] = TreeNode.Tree(category)
            root.add_child(category_map[category])
        placeNode = TreeNode.Tree(name,category=category,ratings=ratings)
        category_map[category].add_child(placeNode)
    print('Tree built successfully')    
    return root
def bfsRecommendation(root,target,topN):
    queue = [root]
    recommendations = []
    while queue:
        node = queue.pop(0)
        if node.name == target:
            recommendations.extend([child for child in node.children if child.ratings is not None])
        queue.extend(node.children)
    # sr.bubbleSort(recommendations)
    return recommendations[:topN]
places = pd.ReadCsv()
# tree2 = build_Tree(places)
# for node in tree2.children:
#     print(node.tostring())
tree = bfsRecommendation(build_Tree(places),'Malls',3)
for node in tree:
    print(node.tostring())


