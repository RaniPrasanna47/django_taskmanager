function editTask(taskId) {
    let taskTextElement = document.querySelector(`#task-${taskId} .task-text`);
    let newText = prompt("Edit task:", taskTextElement.textContent);   
    if (newText && newText.trim() !== "") {
        fetch(`/edit-task/${taskId}/`, {
            method: "POST",
            headers: { "X-CSRFToken": getCSRFToken(), "Content-Type": "application/json" },
            body: JSON.stringify({ title: newText })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                taskTextElement.textContent = newText;
            } else {
                alert("Error updating task!");
            }
        });
    }
}
function completeTask(taskId) {
    fetch(`/complete-task/${taskId}/`, {
        method: "POST",
        headers: { "X-CSRFToken": getCSRFToken() }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            let taskItem = document.querySelector(`#task-${taskId}`);
            taskItem.classList.add("completed");
            taskItem.querySelector(".complete").style.background = "green";
        } else {
            alert("Error marking task as completed!");
        }
    });
}
function deleteTask(taskId) {
    fetch(`/delete-task/${taskId}/`, {
        method: "POST",
        headers: { "X-CSRFToken": getCSRFToken() }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.querySelector(`#task-${taskId}`).remove();
        } else {
            alert("Error deleting task!");
        }
    });
}
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
