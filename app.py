from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template for the landing page
LANDING_PAGE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Limpeza Express - Serviços de Limpeza Residencial</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f4f4;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 10px;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .services {
            background-color: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .services h2 {
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        .service-list {
            list-style: none;
        }
        
        .service-list li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #eee;
        }
        
        .service-list li:last-child {
            border-bottom: none;
        }
        
        .contact {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        .contact h2 {
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        
        .contact-info {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        
        .cta-button {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1.1rem;
            transition: background-color 0.3s;
        }
        
        .cta-button:hover {
            background-color: #2980b9;
        }
        
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Limpeza Express</h1>
            <p class="subtitle">Seu lar limpo e organizado com profissionais qualificados</p>
        </header>
        
        <div class="services">
            <h2>Nossos Serviços</h2>
            <ul class="service-list">
                <li>✨ Limpeza residencial completa</li>
                <li>🧹 Limpeza pós-obra</li>
                <li>🏠 Limpeza de casas e apartamentos</li>
                <li>🪟 Lavagem de janelas</li>
                <li>🛏️ Higienização de estofados</li>
                <li>🧽 Limpeza de cozinhas e banheiros</li>
            </ul>
        </div>
        
        <div class="contact">
            <h2>Entre em Contato</h2>
            <p class="contact-info">
                📱 WhatsApp: (11) 98765-4321<br>
                📧 Email: contato@limpezaexpress.com.br<br>
                ⏰ Atendimento: Seg-Sex 8h às 18h | Sáb 8h às 14h
            </p>
            <a href="https://wa.me/5511987654321" class="cta-button">
                Solicitar Orçamento pelo WhatsApp
            </a>
        </div>
        
        <footer class="footer">
            <p>&copy; 2024 Limpeza Express. Todos os direitos reservados.</p>
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(LANDING_PAGE)

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)