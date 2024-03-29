from tweet import TweetParser


def main():
    parser = TweetParser()
    data = {
        "id": 1,
        "tweet": "HelloWorld",
        "user_id": 2,
        "user_name": "bob"
    }

    print(parser.parse(data))

    data_list = [data, data]
    print(parser.parse_many(data_list))


if __name__ == "__main__":
    main()
