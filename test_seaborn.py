
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")    # 붓꽃 데이터
titanic = sns.load_dataset("titanic")    # 타이타닉호 데이터
tips = sns.load_dataset("tips")    # 팁 데이터
flights = sns.load_dataset("flights")    # 여객운송 데이터

sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde")
plt.suptitle("Joint Plot and Kernel Density Plot", y=1.02)
plt.show()