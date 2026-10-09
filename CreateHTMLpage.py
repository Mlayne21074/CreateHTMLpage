from pathlib import Path


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Learning Flexbox and Grid</title>

	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			font-family: Arial, sans-serif;
			background-color: #f4f6f9;
			color: #222;
			line-height: 1.6;
		}

		/* Navigation menu using Flexbox */
		nav {
			background-color: #172554;
			padding: 15px 8%;
			display: flex;
			justify-content: space-between;
			align-items: center;
			flex-wrap: wrap;
			gap: 15px;
		}

		.logo {
			color: white;
			font-size: 22px;
			font-weight: bold;
		}

		.menu {
			display: flex;
			gap: 20px;
			flex-wrap: wrap;
		}

		.menu a {
			color: white;
			text-decoration: none;
		}

		.menu a:hover {
			color: #93c5fd;
		}

		header {
			background-color: #dbeafe;
			text-align: center;
			padding: 45px 20px;
		}

		header h1 {
			color: #172554;
		}

		main {
			max-width: 1100px;
			margin: 30px auto;
			padding: 0 20px;
		}

		/* Main content using CSS Grid */
		.grid-container {
			display: grid;
			grid-template-columns: repeat(3, 1fr);
			gap: 20px;
		}

		.card {
			background-color: white;
			border-radius: 10px;
			padding: 20px;
			box-shadow: 0 3px 10px rgba(0, 0, 0, 0.08);
		}

		.card img {
			width: 100%;
			height: 150px;
			object-fit: cover;
			border-radius: 6px;
		}

		.card h2 {
			color: #1d4ed8;
		}

		.explanation {
			background-color: white;
			margin-top: 25px;
			padding: 25px;
			border-radius: 10px;
		}

		footer {
			background-color: #172554;
			color: white;
			text-align: center;
			padding: 20px;
			margin-top: 30px;
		}

		/* Responsive layout for tablets and phones */
		@media (max-width: 800px) {
			.grid-container {
				grid-template-columns: repeat(2, 1fr);
			}

			nav {
				justify-content: center;
			}
		}

		@media (max-width: 550px) {
			.grid-container {
				grid-template-columns: 1fr;
			}

			.menu {
				justify-content: center;
				gap: 12px;
			}
		}
	</style>
</head>

<body>

	<nav>
		<div class="logo">WebLearn</div>

		<div class="menu">
			<a href="#home">Home</a>
			<a href="#features">Features</a>
			<a href="#layout">Layout Guide</a>
			<a href="#about">About</a>
		</div>
	</nav>

	<header id="home">
		<h1>Learning CSS Layouts</h1>
		<p>Discover how Flexbox and CSS Grid help create modern websites.</p>
	</header>

	<main>
		<h2 id="features">CSS Layout Features</h2>

		<div class="grid-container">
			<section class="card">
				<img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600"
					 alt="Laptop and web development workspace">
				<h2>Flexbox</h2>
				<p>Flexbox arranges items in a row or column. It is useful for navigation menus and aligning elements.</p>
			</section>

			<section class="card">
				<img src="https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=600"
					 alt="Computer screen displaying code">
				<h2>CSS Grid</h2>
				<p>Grid arranges content into rows and columns. It is useful for card layouts and page structures.</p>
			</section>

			<section class="card">
				<img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600"
					 alt="Modern workspace">
				<h2>Responsive Design</h2>
				<p>Responsive design changes the layout to fit different screen sizes, including phones and tablets.</p>
			</section>
		</div>

		<section class="explanation" id="layout">
			<h2>How the Layout Works</h2>

			<h3>Flexbox settings</h3>
			<ul>
				<li><strong>display: flex;</strong> places menu items in a flexible layout.</li>
				<li><strong>justify-content: space-between;</strong> separates the logo and menu.</li>
				<li><strong>align-items: center;</strong> aligns items vertically.</li>
				<li><strong>gap:</strong> creates space between menu items.</li>
				<li><strong>flex-wrap: wrap;</strong> allows items to move onto another line.</li>
			</ul>

			<h3>CSS Grid settings</h3>
			<ul>
				<li><strong>display: grid;</strong> creates a grid layout.</li>
				<li><strong>grid-template-columns: repeat(3, 1fr);</strong> creates three equal columns.</li>
				<li><strong>gap: 20px;</strong> adds space between cards.</li>
				<li><strong>1fr</strong> represents one share of the available space.</li>
			</ul>

			<h3>Responsive design</h3>
			<p>
				Media queries change the grid to two columns when the screen
				is 800 pixels wide or smaller, and one column when it is
				550 pixels wide or smaller. This makes the page easier to
				read on smaller devices.
			</p>

			<h3>About this project</h3>
			<p id="about">
				This webpage demonstrates how Flexbox and CSS Grid can work
				together to create an organized, responsive website.
			</p>
		</section>
	</main>

	<footer>
		<p>WebLearn | HTML and CSS Layout Project</p>
	</footer>

</body>
</html>
"""


if __name__ == "__main__":
	output_path = Path(__file__).with_suffix(".html")
	output_path.write_text(HTML, encoding="utf-8")
	print(f"Created {output_path}")
