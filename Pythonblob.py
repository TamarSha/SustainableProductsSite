import textblob
from textblob import TextBlob
bloblist = []
users = []
Yaara ="Your website is great!"
Shlomo= "Your website is bad:("

users.append(Shlomo)
users.append(Yaara)

blob1 = TextBlob(Yaara).polarity
blob2 = TextBlob(Shlomo).polarity

bloblist.append(blob2)
bloblist.append(blob1)
x = range(len(bloblist))

print(blob1)
print(blob2)
print(bloblist)