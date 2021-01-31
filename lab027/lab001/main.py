import argparse

from notion.client import NotionClient

#
parser = argparse.ArgumentParser(description='notion')
parser.add_argument('--token', '-t', help='token')
args = parser.parse_args()
print("token={}".format(args.token))


def get_title():
    # Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so

    client = NotionClient(token_v2=args.token)

    # Replace this URL with the URL of the page you want to edit
    page = client.get_block(
        "https://www.notion.so/liguoqinjim/3f253e90fea2424aa1d7224b526b04a5?v=6cb47ebcd12a4982bd89c04762c04e05")

    print("The old title is:", page.title)


def access_database():
    client = NotionClient(token_v2=args.token)

    # Access a database using the URL of the database page or the inline block
    cv = client.get_collection_view(
        "https://www.notion.so/liguoqinjim/3f253e90fea2424aa1d7224b526b04a5?v=c26bee77d48e4a3fade236ff1ae49498")
    print(cv)

    # List all the records with "Bob" in them
    for row in cv.collection.get_rows():
        print("id={}".format(row.id))
        print("name={}".format(row.title))

        block = client.get_block(row.id)
        print(block)
        props = block.get_all_properties()
        print(props)
        print(type(props))

        break

    # Add a new record
    row = cv.collection.add_row()
    row.title = "Just some data2"
    print(row)
    block = client.get_block(row.id)
    props = block.get_all_properties()
    print("props:{}".format(props))
    # 设置row的值
    block.set_property("fen_lei", "历史")


if __name__ == '__main__':
    # get_title()
    access_database()
