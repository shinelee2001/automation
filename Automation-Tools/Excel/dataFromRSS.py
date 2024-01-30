import feedparser
import pandas

url = "https://www.dailysecu.com/rss/allArticle.xml"
# Parse RSS feed
feed = feedparser.parse(url)

# Extract the required data in list
titles = []
links = []
descriptions = []
authors = []
pubDates = []
for entry in feed.entries:
    titles.append(entry.title)
    links.append(entry.link)
    descriptions.append(entry.description)
    authors.append(entry.author)
    pubDates.append(entry.published)

# Save the extracted data in pandas DataFrame
data = {
    "Title": titles,
    "Link": links,
    "Description": descriptions,
    "Author": authors,
    "PubDate": pubDates,
}
df = pandas.DataFrame(data)

# Save the DataFrame as in excel format
df.to_excel("rss1.xlsx", index=False)

"""
Save 10 data on each sheet on excel using for loop:

with pandas.ExcelWriter('rss1.xlsx') as writer:
    sheet_count = 0
    for i in range(0, len(df), 10):
        sheet_count += 1
        sheet_name = f'Shhet{sheet_count}'
        df.iloc[i:i+10].to_excel(writer, sheet_name=sheet_name, index=False)
"""
