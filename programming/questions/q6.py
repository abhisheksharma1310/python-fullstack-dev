# i = 10
# while i > 0:
#      if bool(i % 3):
#          print("I rock")
#      i-=1

#Given the following dictionary: how would you access the title of the second dictionary in the tags list i.e the one with 991 counts and access its title i.e fundamentals

article = {
'name':'programming principles',
'tags': [{
'title':'python',
'counts': 28
},
{
'title':'fundamentals',
'counts':991
}
]
}

print(article['tags'][1]['title'])

