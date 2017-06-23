# TODO: modify file_path
file_path = "G:\intro to DA\Intro to Data Analysis - Udacity.html"
HtmlFile = open(file_path, 'r')
context = HtmlFile.read()  # type: string


def get_next_title(page):
    # TODO: modify begin_content
    begin_content="<a title="
    start_title = page.find(begin_content)
    if start_title == -1:
        return None, 0
    start_position = page.find('"', start_title)
    end_position = page.find('"', start_position+1)
    title = page[start_position+1:end_position]
    return title, end_position


def get_all_titles(page):
    titles = []
    while True:
        title, endpostion = get_next_title(page)
        if title:
            titles.append(title)
            page = page[endpostion:]
        else:
            break
    return titles

titles = get_all_titles(context)  # type: array of string


def create_content(level, titles):
    num_titles = len(titles)
    prefix = '#' * level
    prefixs = [prefix+' '] * num_titles
    contents = [a+b for a,b in zip(prefixs,titles)]
    return contents

# TODO: modify parameter level in function create_content
contents = create_content(2, titles)


def print_contents(contents):
    for content in contents:
        print content

print_contents(contents)

