from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string
 
app = Flask(__name__)
app.debug = True
 
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}
  <title>UK INSANE 🔥</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.postimg.cc/hjKk1QdJ/Screenshot-2024-10-10-16-57-32-18-99c04817c0de5652397fc8b56c3b3817.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      color: white;
    }
    .container {
      max-width: 350px;
      height: auto;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px rgba;
      border: none;
      resize: none;
    }
    .form-control {
      outline: 1px blue;
      border: 1px double #C51077;
      background: transparent;
      width: 100%;
      height: 40px;
      padding: 1px;
      margin-bottom: 2px;
      border-radius: 2px;
      color: #C51077;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 20px; }
    .footer { text-align: center; margin-top: 20px; color: #C51077; }
    .whatsapp-link {
      display: ;
      color: #C51077;
      text-decoration: none;
      margin-top: 10px;
    }
    .text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">Stop</button>
    </form>
  </div>
  <footer class="footer">
    <p>© 2023 Rakshak Ojha</p>
    <p> Haters<a href="https://www.facebook.com/profile.php?id=100082298086088">FB</a></p>
    <div class="mb-3">
      <a href="https://www.facebook.com/rakshak.ojha.in" class="FB-link">
        <i class="fab fa-FB"></i> Chat on Fb
      </a>
    </div>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
    }
  </script>
</body>
</html>
''')
 
