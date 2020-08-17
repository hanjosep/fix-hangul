import os


text = "1Áý ¼ÒÇâ"
text ="C:\\Users\\Josep Han\\Music\\¼ÒÇâ - 2. ¾Æºü¿ÍÀÇ ¿¹¹è.mp3"
# print(text.encode('windows-1252').decode('korean', 'replace')) 
# helps decode the given text into proper korean.
# print(os.path.basename("C:\\Users\\Josep Han\\Music\\¼ÒÇâ - 2. ¾Æºü¿ÍÀÇ ¿¹¹è.mp3"))
# returns badly encoded filename

# print(os.listdir("C:\\Users\\Josep Han\\Music\\"))
# prints list of broken filenames within folder

brokenlist=os.listdir("C:\\Users\\Josep Han\\Music\\")
print(brokenlist)
fixedlist = []

for item in brokenlist:
    fixedlist.append(item.encode('windows-1252', "ignore").decode('korean', 'replace'))


# print(fixedlist)
parent_path = "C:\\Users\\Josep Han\\Music\\"
# fix the broken file names into the properly encoded filenames.
# for broken in brokenlist:
#     for fixed in fixedlist:
#         os.rename(parent_path + broken, parent_path+fixed)
res = {brokenlist[i]: fixedlist[i] for i in range(len(fixedlist))} 
# print(res)
# print(len(fixedlist))
# print((brokenlist))

