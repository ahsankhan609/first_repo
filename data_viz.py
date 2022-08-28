#steps involved in data visualization

#import librarirs
import seaborn as sns
import matplotlib.pyplot as plt

#set a theme of the chart

sns.set_theme(style="ticks", color_codes=True)

#import dataset

kashti = sns.load_dataset("titanic")

#print(kashti)

# #plot basic graph with 1 variable

# p = sns.countplot(x="sex", data=kashti)

# #show plot
# p.set_title("Count for plot with 1 Variable.")
# plt.show()

#plot basic graph with 2 variable

p = sns.countplot(x="sex", data=kashti, hue="alive")

#show plot
p.set_title("Count for plot with 2 Variables.")
plt.show()