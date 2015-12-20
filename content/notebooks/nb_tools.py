import os
from datetime import datetime

def connect_notebook_to_post(name='Untitled', title='New post', tags='ipython', author='UEA'):
    """
    Write a header to a markdown blog post and return an HTML string with links to the notebook.
    
    Idea taken from http://ocefpaf.github.com/python4oceanographers
    """

    hour = datetime.utcnow().strftime('%H:%M')

    date = '-'.join(name.split('-')[:3])

    metadata = dict(title=title,
                    date=date,
                    hour=hour,
                    tags=tags,
                    name=name,
                    author=author)

    markdown = "Title: {title}\nAuthor: {author}\ndate: {date} {hour}\ntags: {tags}\n\n{{% notebook {name}.ipynb cells[2:] %}}".format(**metadata)

    content = os.path.abspath(os.path.join(os.getcwd(),
                                           os.pardir,
                                           '{}.md'.format(name)))
    with open('{}'.format(content), 'w') as f:
        f.writelines(markdown)

    html = """
    <small>
    <p> This post was written as an IPython (Jupyter) notebook. You can view or download it using
    <a href="http://nbviewer.ipython.org/github/ueapy/ueapy.github.io/blob/src/content/notebooks/%s.ipynb">nbviewer</a>.</p>
    """ % (name)

    return html
