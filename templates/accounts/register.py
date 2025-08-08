{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>Register</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
  <div class="container">
    <h2>Register</h2>
    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Register</button>
    </form>
    <p><a href="{% url 'login' %}">Already have an account? Login</a></p>
  </div>
</body>
</html>
