function addTask() {
    const taskInput = document.getElementById('new-task');
    const taskList = document.getElementById('task-list');

    if (taskInput.value.trim() === '') return;

    const li = document.createElement('li');
    li.innerHTML = `
        <span onclick="toggleComplete(this)">${taskInput.value}</span>
        <button class="delete-btn" onclick="deleteTask(this)">Delete</button>
    `;
    taskList.appendChild(li);
    taskInput.value = '';
}

function toggleComplete(task) {
    task.parentElement.classList.toggle('completed');
}

function deleteTask(button) {
    button.parentElement.remove();
}
