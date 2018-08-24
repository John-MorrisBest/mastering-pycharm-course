# To JMMB's Repo
# Some code added!!!!
# And some more...
import service


def main():
    show_header()
    service.download_info()
    display_results()


def show_header():
    print("Welcome to the talk python info downloader")
    print()


def display_results():
    for show_id in range(100, 141):
        info = service.get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


if __name__ == '__main__':
    main()
