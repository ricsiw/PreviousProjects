# Company Showcase Project

This project is a static website designed to showcase various types of content related to the company's work. It includes sections for pictures, PDF files, YouTube videos, and PowerPoint presentations, all styled using Tailwind CSS for a modern and responsive design.

## Project Structure

The project is organized as follows:

```
company-showcase
├── src
│   ├── index.html          # Main entry point of the website
│   ├── css
│   │   └── input.css      # Tailwind CSS and custom styles
│   ├── js
│   │   └── main.js        # JavaScript for interactive features
│   ├── pages
│   │   ├── pictures.html   # Gallery of images
│   │   ├── pdfs.html       # List of PDF files
│   │   ├── videos.html      # Embedded YouTube videos
│   │   └── presentations.html # Embedded or linked PowerPoint presentations
│   └── assets
│       ├── images          # Folder for image assets
│       └── pdfs            # Folder for PDF assets
├── tailwind.config.js      # Tailwind CSS configuration
├── package.json            # npm configuration
└── README.md               # Project documentation
```

## Features

- **Responsive Design**: The website is fully responsive and looks great on all devices.
- **Tailwind CSS**: Utilizes Tailwind CSS for styling, allowing for easy customization and a modern look.
- **Interactive Elements**: JavaScript is used to add interactivity, such as animations for buttons.
- **Content Categories**: Separate pages for pictures, PDFs, videos, and presentations, making it easy to navigate and find content.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the necessary dependencies using npm:
   ```
   npm install
   ```
4. Build the CSS using Tailwind:
   ```
   npm run build
   ```
5. Open `src/index.html` in your web browser to view the project.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.