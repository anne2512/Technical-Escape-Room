import random

code = {
    "easy" : [ """<html>
<body>
</body>
</html>
""", # 1st code.. very easy code only for testing

"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Page</title>
</head>
<body>
    <header>
        <h1>Welcome to My Page</h1>
    </header>
    <main>
        <p>This is a simple HTML page.</p>
    </main>
    <footer>
        <p>Copyright &copy; 2024</p>
    </footer>
</body>
</html>""", # easy code no 1

"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Embedded Image</title>
</head>
<body>
    <h2>Cute Cat</h2>
    <img src="https://placekitten.com/200/300" alt="Cute Cat">
</body>
</html>""", # easy code no 2

"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Embedded Audio</title>
</head>
<body>
    <h2>My Favorite Song</h2>
    <audio controls>
        <source src="audio.mp3" type="audio/mpeg">
    </audio>
</body>
</html>""", # easy code no 2
"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embedding SVG</title>
</head>
<body>
    <svg width="100" height="100">
        <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
    </svg>
</body>
</html>""", # easy code no 4
"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Embedded Video</title>
</head>
<body>
    <h2>My Favorite Video</h2>
    <video controls width="400" height="300">
        <source src="video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>"""
] ,# easy code no 5

"difficult" : [
    """<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
    <header>
        <h1>Main Heading</h1>
        <nav>
            <ul>
                <li><a href="#">Link 1</a></li>
                <li><a href="#">Link 2</a></li>
                <li><a href="#">Link 3</a></li>
            </ul>
        </nav>
    </header>
    <article>
        <h2>Article Title</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer eget ligula et justo sodales vestibulum.</p>
    </article>
    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>
</body>
</html>""", # difficult code 1

"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complex HTML Structure</title>
</head>
<body>
    <h1>Main Heading</h1>
    <figure>
        <img src="image.jpg" alt="Description of the image">
        <figcaption>Caption for the image</figcaption>
    </figure>
    <section>
        <h2>Section Heading</h2>
        <p>This is a paragraph within a section.</p>
        <blockquote>
            <p>This is a quote within the section.</p>
        </blockquote>
    </section>
    <footer>
        <p>&copy; 2024</p>
    </footer>
</body>   
</html>""", # difficult code no 2
"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>Semantic Markup with Microdata</title>
</head>
<body>
    <article itemscope itemtype="http://schema.org/Article">
        <h1 itemprop="headline">Article Title</h1>
        <p itemprop="description">Article description goes here.</p>
        <footer>
            <span itemprop="author">Author Name</span>
        </footer>
    </article>
</body>
</html>""", #diffcult code 3



 ] #diffcult code 2

}  # end of code dict




def get_easy():
    
    ind = random.randint(0,len(code["easy"])-1)
    
    print("function call")

    cur_code = code["easy"][ind]
    o = cur_code.split('\n')
    orig = []
    for i in o : 
        if i != '' and i != None:
            orig.append(i)
    original =[x.strip() for x in orig]
    
    jumbled = original.copy()
    random.shuffle(jumbled)
    return original, jumbled
    


def get_difficult():
    
    ind = random.randint(0,len(code["difficult"])-1)
    
    print("function call difficult")

    cur_code = code["difficult"][ind]
    o = cur_code.split('\n')
    orig = []
    for i in o : 
        if i != '' and i != None:
            orig.append(i)
    original =[x.strip() for x in orig]
    
    jumbled = original.copy()
    random.shuffle(jumbled)
    return original, jumbled
    
