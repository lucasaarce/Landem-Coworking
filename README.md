# Landem Coworking Website

A professional website developed for Landem, a company offering coworking spaces in Barcelona's Gràcia district. The site allows users to explore available plans and reserve their workspace through an integrated form.

## 🌐 Live Site
Access the live website here: https://coworkinglandem.es

## 🏢 About Landem
Landem is a company that manages construction projects comprehensively, without rigid structures or complex organizational charts, and above all, without compromising on quality standards. They respect the uniqueness of each client and project, providing personalized, creative, and non-prefabricated solutions. Their communication with the client is agile, direct, and close, and their technicians are dedicated with enthusiasm and commitment to the projects, regardless of their size and volume.

## 📌 Location
Carrer de Camprodon, 26, local 1, 08012 Barcelona, Spain

## 🛠️ Project Overview
This project encompasses both frontend and backend components:  
- **Frontend**: Built with HTML, CSS, and JavaScript to provide a responsive and user-friendly interface.
- **Backend**: Developed using Python and Flask to handle form submissions and send reservation details via email to Landem.

## 📁 Repository Structure
Landem-Coworking/  
├── static  
│   ├── css/  
│   ├── js/  
│   └── images/  
├── templates/  
│   └── *.html  
├── app.py  
├── requirements.txt  
├── robots.txt  
├── sitemap.xml  
└── favicon.ico  

- **static/**: Contains all static assets like CSS, JavaScript, and images.  
- **templates/**: Holds HTML templates rendered by Flask.  
- **app.py**: The main Flask application handling routing and form processing.  
- **requirements.txt**: Lists all Python dependencies.  
- **robots.txt** & **sitemap.xml**: Files to enhance SEO.  

## ✉️ Reservation Form Functionality
Users can reserve a workspace by filling out a form on the website. Upon submission:

1. The form data is sent to the Flask backend [app.py](./app.py).
2. The backend processes the data and sends an email to Landem with the client's information.
3. Landem can then contact the client to confirm the reservation.

## 🔍 SEO Optimization
To improve search engine visibility:  
- **robots.txt**: Specifies the site's crawling policies.
- **sitemap.xml**: Provides a structured map of the website's pages for search engines.

## 🚀 Getting Started
### Prerequisites  
- Python 3.x  
- pip  
### Installation

#### 1. Clone the repository:  
```bash  
git clone https://github.com/lucasaarce/Landem-Coworking.git
cd Landem-Coworking
```
#### 2. Create a virtual environment (optional but recommended): 
```bash   
python3 -m venv venv  
source venv/bin/activate  
```
#### 3. Install dependencies:  
```bash  
pip install -r requirements.txt 
``` 
#### 4. Run the application:
```bash   
python app.py 
```  
#### 5. Access the website:  
Open your browser and navigate to http://localhost:5000  

## 📧 Configuration
To enable email functionality for form submissions:  
1. Set up environment variables (recommended) or configure directly in app.py:  
```python
 EMAIL_ADDRESS = 'your_email@example.com'  
 EMAIL_PASSWORD = 'your_email_password'
```
2. Ensure less secure app access is enabled for your email provider or use an app-specific password.  

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📞 Contact
For inquiries or support:  
- Email: landemcoworking@gmail.com
- Phone: +34 640 86 80 80