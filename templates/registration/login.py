{% load static %}
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>

<h2>Login</h2>

{% if error %}
  <p style="color:red">{{ error }}</p>
{% endif %}

<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>

<a href="{% url 'register' %}">Don't have an account? Register</a>

</body>
</html>
