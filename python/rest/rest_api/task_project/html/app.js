const API_BASE_URL = 'http://localhost:3000';
let authToken = localStorage.getItem('authToken') || '';

// Display token on page load
document.getElementById('token-display').textContent = authToken || 'Not logged in';

// Helper function to display response
function displayResponse(data) {
    document.getElementById('response-output').textContent = JSON.stringify(data, null, 2);
}

// Helper function to make API calls
async function apiCall(endpoint, method = 'GET', body = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    if (authToken) {
        options.headers['Authorization'] = `Bearer ${authToken}`;
    }

    if (body) {
        options.body = JSON.stringify(body);
    }

    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        const data = await response.json();
        displayResponse(data);
        return data;
    } catch (error) {
        displayResponse({ error: error.message });
    }
}

// Authentication handlers
document.getElementById('register-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        username: document.getElementById('reg-username').value,
        email: document.getElementById('reg-email').value,
        password: document.getElementById('reg-password').value,
        role: document.getElementById('reg-role').value,
        department: document.getElementById('reg-department').value
    };
    await apiCall('/auth/register', 'POST', data);
});

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        username: document.getElementById('login-username').value,
        password: document.getElementById('login-password').value
    };
    const response = await apiCall('/auth/login', 'POST', data);
    if (response && response.token) {
        authToken = response.token;
        localStorage.setItem('authToken', authToken);
        document.getElementById('token-display').textContent = authToken;
    }
});

document.getElementById('logout-btn').addEventListener('click', () => {
    authToken = '';
    localStorage.removeItem('authToken');
    document.getElementById('token-display').textContent = 'Not logged in';
    displayResponse({ message: 'Logged out successfully' });
});

// Project handlers
document.getElementById('create-project-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        name: document.getElementById('project-name').value,
        description: document.getElementById('project-description').value
    };
    await apiCall('/project/create', 'POST', data);
});

document.getElementById('list-projects-btn').addEventListener('click', async () => {
    const data = await apiCall('/project/list', 'GET');
    if (data && data.projects) {
        const projectsHtml = data.projects.map(p => 
            `<p><strong>ID:</strong> ${p.id} | <strong>Name:</strong> ${p.name} | <strong>Description:</strong> ${p.description}</p>`
        ).join('');
        document.getElementById('projects-list').innerHTML = projectsHtml;
    }
});

document.getElementById('get-project-tasks-btn').addEventListener('click', async () => {
    const projectId = document.getElementById('project-id-tasks').value;
    const data = await apiCall(`/project/${projectId}/tasks`, 'GET');
    if (data && data.tasks) {
        const tasksHtml = data.tasks.map(t => 
            `<p><strong>ID:</strong> ${t.id} | <strong>Title:</strong> ${t.title} | <strong>Status:</strong> ${t.status} | <strong>Due:</strong> ${t.due_date}</p>`
        ).join('');
        document.getElementById('project-tasks-list').innerHTML = tasksHtml;
    }
});

document.getElementById('update-project-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const projectId = document.getElementById('update-project-id').value;
    const data = {};
    const name = document.getElementById('update-project-name').value;
    const description = document.getElementById('update-project-description').value;
    if (name) data.name = name;
    if (description) data.description = description;
    await apiCall(`/project/${projectId}`, 'PUT', data);
});

document.getElementById('delete-project-btn').addEventListener('click', async () => {
    const projectId = document.getElementById('delete-project-id').value;
    await apiCall(`/project/${projectId}/delete`, 'DELETE');
});

// Task handlers
document.getElementById('create-task-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const assignedEmployees = document.getElementById('task-assigned-employees').value;
    const data = {
        title: document.getElementById('task-title').value,
        description: document.getElementById('task-description').value,
        priority: document.getElementById('task-priority').value,
        due_date: document.getElementById('task-due-date').value,
        status: document.getElementById('task-status').value,
        assigned_employees: assignedEmployees ? assignedEmployees.split(',').map(id => parseInt(id.trim())) : [],
        project_id: parseInt(document.getElementById('task-project-id').value) || null,
        comments: document.getElementById('task-comments').value
    };
    await apiCall('/task/create-task', 'POST', data);
});

document.getElementById('list-tasks-btn').addEventListener('click', async () => {
    const data = await apiCall('/task/list-tasks', 'GET');
    if (data && Array.isArray(data)) {
        const tasksHtml = data.map(t => 
            `<p><strong>ID:</strong> ${t.id} | <strong>Title:</strong> ${t.title} | <strong>Status:</strong> ${t.status} | <strong>Priority:</strong> ${t.priority}</p>`
        ).join('');
        document.getElementById('tasks-list').innerHTML = tasksHtml;
    }
});

document.getElementById('view-task-btn').addEventListener('click', async () => {
    const taskId = document.getElementById('view-task-id').value;
    const data = await apiCall(`/task/view-task/${taskId}`, 'GET');
    if (data) {
        const detailsHtml = `
            <p><strong>ID:</strong> ${data.id}</p>
            <p><strong>Title:</strong> ${data.title}</p>
            <p><strong>Description:</strong> ${data.description}</p>
            <p><strong>Status:</strong> ${data.status}</p>
            <p><strong>Priority:</strong> ${data.priority}</p>
            <p><strong>Due Date:</strong> ${data.due_date}</p>
            <p><strong>Comments:</strong> ${data.comments}</p>
        `;
        document.getElementById('task-details').innerHTML = detailsHtml;
    }
});

document.getElementById('filter-tasks-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {};
    const status = document.getElementById('filter-status').value;
    const priority = document.getElementById('filter-priority').value;
    const dueDate = document.getElementById('filter-due-date').value;
    const assignedEmployee = document.getElementById('filter-assigned-employee').value;
    
    if (status) data.status = status;
    if (priority) data.priority = priority;
    if (dueDate) data.due_date = dueDate;
    if (assignedEmployee) data.assigned_employee = parseInt(assignedEmployee);
    
    const result = await apiCall('/task/filter-tasks', 'POST', data);
    if (result && Array.isArray(result)) {
        const tasksHtml = result.map(t => 
            `<p><strong>ID:</strong> ${t.id} | <strong>Title:</strong> ${t.title} | <strong>Status:</strong> ${t.status} | <strong>Priority:</strong> ${t.priority}</p>`
        ).join('');
        document.getElementById('filtered-tasks-list').innerHTML = tasksHtml;
    }
});

document.getElementById('update-task-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const taskId = document.getElementById('update-task-id').value;
    const data = {};
    
    const title = document.getElementById('update-task-title').value;
    const description = document.getElementById('update-task-description').value;
    const priority = document.getElementById('update-task-priority').value;
    const dueDate = document.getElementById('update-task-due-date').value;
    const status = document.getElementById('update-task-status').value;
    const assignedEmployees = document.getElementById('update-task-assigned-employees').value;
    const comments = document.getElementById('update-task-comments').value;
    
    if (title) data.title = title;
    if (description) data.description = description;
    if (priority) data.priority = priority;
    if (dueDate) data.due_date = dueDate;
    if (status) data.status = status;
    if (assignedEmployees) data.assigned_employees = assignedEmployees.split(',').map(id => parseInt(id.trim()));
    if (comments) data.comments = comments;
    
    await apiCall(`/task/update-task/${taskId}`, 'PUT', data);
});

document.getElementById('delete-task-btn').addEventListener('click', async () => {
    const taskId = document.getElementById('delete-task-id').value;
    await apiCall(`/task/delete-task/${taskId}`, 'DELETE');
});
