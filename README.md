# Shree Rajlaxmi Handloom & Furnishing Website

A clean, responsive Flask + HTML/CSS/JavaScript website for the Morbi business.

## Business details used
- Owner: Nirav Jivani
- Business: Shree Rajlaxmi Handloom & Furnishing
- Products: Sofa, Curtain, Mattress
- Sofa price: ₹3,000 – ₹7,000 as per design
- Curtain price: ₹250 – ₹1,200 per meter
- Phone / WhatsApp: 9638635600
- Email: niravrajlaxmi@gmail.com
- Address: First Floor, Vaidehi Plaza, Opp. Hanuman Ji Temple, Ravapar Ghunda Road, Morbi, Gujarat 363641

## Run in VS Code

1. Install Python 3.10+.
2. Open this folder in VS Code.
3. Open Terminal.
4. Run:
   `python -m venv venv`
5. Activate it:
   - Windows: `venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`
6. Install Flask:
   `pip install flask`
7. Start:
   `python app.py`
8. Open the local address shown in the terminal, normally:
   `http://127.0.0.1:5000`

## npm development command

This project remains Flask-based, but includes npm scripts for a familiar workflow.
After installing Node.js, run:

`npm run dev`

For a temporary public Cloudflare URL, install `cloudflared`, start the app with
`npm run dev`, then open a second terminal and run:

`npm run cloudflare`

Cloudflare will print a temporary `trycloudflare.com` URL. Keep both terminals
running while the tunnel is in use.

## Images
The product images supplied in the uploaded DOCX were extracted into `static/images/`.
You can replace them with your own higher-resolution product photos while keeping the same filenames.
