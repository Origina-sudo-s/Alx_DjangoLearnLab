<!-- bookshelf/template/bookshelf/form_example.html -->
<form method="post" action="{% url 'form_view_name' %}">
     {% csrf_token %}
     <!-- form fields here -->
     <input type="submit" value="Submit">
     </form>