class BreadthFirstSearch:
    def __init__(self):
        self.graph = {}

    def add_page(self, page):
        if page not in self.graph:
            self.graph[page] = []

    def add_link(self, src, dest):
        if src in self.graph and dest in self.graph:
            self.graph[src].append(dest)
        else:
            print("Both pages must exist before adding a link.")

    def bfs_traversal(self, start, goal):
        queue = [(start, [start])]
        visited = set()
        front = 0

        while front < len(queue):
            current, path = queue[front]
            front += 1

            if current == goal:
                print("Path to goal:", " -> ".join(path))
                return path

            if current not in visited:
                visited.add(current)
                for neighbor in self.graph[current]:
                    queue.append((neighbor, path + [neighbor]))

        print("Goal is not found...")
        return None

    def display_web_structure(self):
        print("Web Page Structure :")
        for page in self.graph:
            print(f"{page}: {self.graph[page]}")


# Example Usage:
crawler = BreadthFirstSearch()
crawler.add_page("Home")
crawler.add_page("Products")
crawler.add_page("Blogs")
crawler.add_page("About Us")
crawler.add_page("Contact Us")
crawler.add_page("Product 1")
crawler.add_page("Product 2")
crawler.add_page("Product 3")
crawler.add_page("Blog Post 1")
crawler.add_page("Blog Post 2")

crawler.add_link("Home", "Products")
crawler.add_link("Home", "Blogs")
crawler.add_link("Home", "About Us")
crawler.add_link("Home", "Contact Us")
crawler.add_link("Products", "Product 1")
crawler.add_link("Products", "Product 2")
crawler.add_link("Products", "Product 3")
crawler.add_link("Blogs", "Blog Post 1")
crawler.add_link("Blogs", "Blog Post 2")

crawler.display_web_structure()
crawler.bfs_traversal("Home", "Product 2")
