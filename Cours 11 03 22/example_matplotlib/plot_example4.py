import sqlite3
import matplotlib.pyplot as plt

database_path = "/home/nsukami/GIT/sqlite_stuff/sakila/sqlite-sakila.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor()

results = []
for row in cursor.execute(
    """
    select * from sales_by_film_category;
    """
):
    results.append(row)


x_points = [x[0] for x in results]
y_points = [x[1] for x in results]

fig, ax = plt.subplots(figsize=(20, 5))
ax.set_title("Total sales for each category", fontsize = 14)
ax.set_ylabel("Total sold", fontsize = 12)
ax.set_ylabel("Categories", fontsize = 12)
ax.set_xticklabels(x_points, rotation='vertical')
# ax.grid("on")

plt.scatter(
    x_points,
    y_points,
)
plt.show()
