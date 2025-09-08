<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>Instagram</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body {
    font-family: Arial, sans-serif;
    background: linear-gradient(45deg,#405DE6,#5851DB,#833AB4,#C13584,#E1306C,#FD1D1D);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
    margin:0;
  }
  .login-box {
    background:#fff;
    padding:36px 30px;
    border:1px solid #dbdbdb;
    border-radius:8px;
    width:360px;
    text-align:center;
    box-shadow:0 1px 8px rgba(0,0,0,0.12);
  }
  .login-box img { width:120px; margin-bottom:18px; }
  input {
    width:92%;
    margin:6px 0;
    padding:10px;
    border:1px solid #dbdbdb;
    border-radius:4px;
    background:#fafafa;
    box-sizing:border-box;
  }
  .btn {
    width:96%;
    padding:11px;
    margin-top:10px;
    background:#3897f0;
    border:none;
    color:#fff;
    font-weight:600;
    border-radius:4px;
    cursor:pointer;
  }
  .secondary {
    margin-top:12px;
    font-size:12px;
    color:#999;
  }
  .message {
    margin-top:12px;
    color:green;
    font-weight:600;
  }
  small { color:#999; display:block; margin-top:8px; }
</style>
</head>
<body>
  <div class="login-box">
    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
    <!-- Affiche l'email du destinataire injecté par Gophish -->
    <input type="text" placeholder="Nom d'utilisateur" disabled value="{{.Email}}">
    <input id="pwd" type="password" placeholder="Mot de passe">
    <!-- Boutons simulés : aucune donnée n'est envoyée -->
    <button class="btn" onclick="simulate('connect')">Se connecter</button>
    <button class="btn" style="background:#34a853;" onclick="simulate('reset')">Réinitialiser</button>

    <div class="message" id="message" aria-live="polite"></div>
    <p class="secondary">Page simulée pour atelier de prévention — aucune donnée n'est collectée.</p>
    <small>Appuyez sur un bouton pour simuler l'action.</small>
  </div>

<script>
  // Simulation uniquement — PAS D'ENVOI / PAS DE STOCKAGE
  function simulate(action) {
    var msg = (action === 'connect') ? "Connexion simulée avec succès ! 🎉" : "Processus de réinitialisation simulé ! ✅";
    document.getElementById('message').innerText = msg;
    // (optionnel) tracker Gophish : si tu veux, Gophish peut suivre la page via {{.Tracker}} dans ton template d'email
  }
</script>
</body>
</html>

