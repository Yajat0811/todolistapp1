<!-- tasks/templates/tasks/delete_task.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Delete Task</title>
</head>
<body>
    <h1>Delete Task</h1>
    <p>Are you sure you want to delete the task "{{ task.title }}"?</p>
    <form method="post" action="{% url 'delete_task' task.id %}">
        {% csrf_token %}
        <button type="submit">Delete</button>
    </form>
</body>
</html>
