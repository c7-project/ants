# ants
ant simulation: artificial intelligence experiment

[![YouTube: ants: an artificial intelligence experiment by c7](https://cloud.githubusercontent.com/assets/14852491/20645401/2b536c82-b455-11e6-8e10-ceeb5f913c5f.png)](https://youtu.be/m7c78RZ0-nY)

---

## Development Software Requirements

### Windows:

- **Python 2.7** *[download](https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi)*
- **Pygame** *[download](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi)*
- *Optional:* **Pycharm** *[download](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)*
- To use **GitHub** with Pycharm: **(git)** *[download](https://git-scm.com/download/win)*

### Linux (Ubuntu):

*To be run in sequence:*

    sudo -s
    apt-get update
    apt-get install -y git software-properties-common
    add-apt-repository -y ppa:fkrull/deadsnakes
    apt-get update
    apt-get install -y python2.7
    apt-get install -y python-setuptools python-dev build-essential
    easy_install pip
    pip install pygame
    pip install flake8
    
To install Pycharm, continue to run these commands:

    add-apt-repository -y ppa:mystic-mirage/pycharm
    apt-get update
    apt-get install -y pycharm-community
    pycharm-community

## Development Notes

- **We're using the [PEP8](https://www.python.org/dev/peps/pep-0008/) formatting standard** to make sure our code is all nice and tidy
- **Keep commit titles short**, but feel free to add longer descriptions (in PyCharm enter two new lines below title for description)
- When committing some work related to an issue, **reference the issue in the commit title as '#X'**, where X is the issue number
- **Look at the issues page** often. The issues are prioritised and will help keep track of development. Don't start impulsively developing a brand new feature before planning and discussing it with the team
- **Make sure you pull the latest changes** ('Update' in PyCharm) **regularly**, especially before committing - otherwise you'll have to merge before you push to master and it'll add merge commits bla bla bla
- If you're unsure of anything to do with development or the true meaning of life, **ask [James](https://github.com/jamesevickery)**

## Sources

_Please append to this list when using third-party resources_

- Background image: [fabooguy.deviantart.com](http://fabooguy.deviantart.com/art/Dirt-Ground-Texture-Tileable-2048x2048-441212191)
- Rock sprite images: [1](http://www.rocasa.es/), [2](http://ggyma.geo.ucm.es/docencia/MasterGeoBio/), [3](http://lascosasdejuampa1.blogspot.com/), [4](http://eldorado.webcubecms.net/products/stone/nationwide-profiles/top-rock/)
- Lekton monospace font: [fonts.google.com/specimen/Lekton](https://fonts.google.com/specimen/Lekton)
