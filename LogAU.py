
import psycopg2

DBNAME = "news"

req_1 = "What are the most popular articles of all time?"

qu_1 = (''' SELECT title, views FROM log_arts INNER JOIN articles ON
    articles.slug = log_arts.slug ORDER BY views desc LIMIT 3; ''')

req_2 = "Who are the most popular article authors of all time?"

qu_2 = ('''
    SELECT author_name.name AS author,
    sum(log_arts.views) AS views FROM log_arts INNER JOIN author_name
    ON author_name.slug=log_arts.slug
    GROUP BY author_name.name ORDER BY views desc limit 4;
    ''')

req_3 = "On which days more than 1% of the requests led to error?"

qu_3 = ('''
    SELECT error_fail.date ,(error_fail.count*100.00 / anals_total.count) AS
    percentage FROM error_fail INNER JOIN anals_total
    ON error_fail.date = anals_total.date
    AND (error_fail.count*100.00 / anals_total.count) >1
    ORDER BY (error_fail.count*100.00 /anals_total.count) desc;
    ''')

# Connect to the database and feed query to extract results


def get_queryResults(sql_query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(sql_query)
    results = c.fetchall()
    db.close()
    return results

re1 = get_queryResults(qu_1)
re2 = get_queryResults(qu_2)
re3 = get_queryResults(qu_3)


# Create a function to print query results


def print_re(q_list):
    for i in range(len(q_list)):
        title = q_list[i][0]
        res = q_list[i][1]
        print("\t" + "%s - %d" % (title, res) + " views")
    print("\n")

print(req_1)
print_results(re1)
print(req_2)
print_results(re2)
print(req_3)
print("\t" + re3[0][1] + " - " + str(re3[0][0]) + "%")
