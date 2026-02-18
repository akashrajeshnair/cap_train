const API_BASE_URL = 'http://localhost:5000';

// Store JWT token (in production, use localStorage or sessionStorage securely)
let authToken = null;

// Utility functions
function showMessage(message, type = 'info') {
    alert(message);
}

function handleResponse(response) {
    if (!response.ok) {
        return response.json().then(err => {
            throw new Error(err.error || `HTTP error! status: ${response.status}`);
        }).catch(() => {
            throw new Error(`HTTP error! status: ${response.status}`);
        });
    }
    return response.json();
}

function getAuthHeaders() {
    const headers = { 'Content-Type': 'application/json' };
    if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
    }
    return headers;
}

// Customer functions
function loadCustomers() {
    fetch(`${API_BASE_URL}/customers/`, {
        headers: getAuthHeaders()
    })
        .then(handleResponse)
        .then(customers => {
            const customerDiv = document.getElementById('customers');
            const customerSelect = document.getElementById('customerId');
            
            if (customerDiv) {
                customerDiv.innerHTML = customers.map(customer => `
                    <div>
                        <strong>${customer.name}</strong> - ${customer.email}<br>
                        Phone: ${customer.phone_number}<br>
                        <button onclick="editCustomer(${customer.id})">Edit</button>
                        <button onclick="deleteCustomer(${customer.id})">Delete</button>
                        <hr>
                    </div>
                `).join('');
            }
            
            if (customerSelect) {
                customerSelect.innerHTML = '<option value="">Select Customer</option>' +
                    customers.map(customer => 
                        `<option value="${customer.id}">${customer.name}</option>`
                    ).join('');
            }
        })
        .catch(error => showMessage('Error loading customers: ' + error.message, 'error'));
}

function addCustomer(customerData) {
    // Remove 'address' field as it's not in the model
    const data = {
        name: customerData.name,
        email: customerData.email,
        phone_number: customerData.phone
    };
    
    fetch(`${API_BASE_URL}/customers/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(handleResponse)
    .then(data => {
        // Store the token for subsequent requests
        if (data.token) {
            authToken = data.token;
            localStorage.setItem('authToken', data.token);
        }
        showMessage(data.message || 'Customer added successfully!', 'success');
        loadCustomers();
        document.getElementById('addCustomerForm').reset();
    })
    .catch(error => showMessage('Error adding customer: ' + error.message, 'error'));
}

function editCustomer(customerId) {
    fetch(`${API_BASE_URL}/customers/${customerId}`, {
        headers: getAuthHeaders()
    })
        .then(handleResponse)
        .then(customer => {
            document.getElementById('updateCustomerId').value = customer.id;
            document.getElementById('updateCustomerName').value = customer.name;
            document.getElementById('updateCustomerEmail').value = customer.email;
            document.getElementById('updateCustomerPhone').value = customer.phone_number;
            // Remove address field handling
            document.getElementById('customer-update').style.display = 'block';
        })
        .catch(error => showMessage('Error loading customer: ' + error.message, 'error'));
}

function updateCustomer(customerId, customerData) {
    const data = {
        name: customerData.name,
        email: customerData.email,
        phone_number: customerData.phone
    };
    
    fetch(`${API_BASE_URL}/customers/${customerId}`, {
        method: 'PUT',
        headers: getAuthHeaders(),
        body: JSON.stringify(data)
    })
    .then(handleResponse)
    .then(data => {
        showMessage('Customer updated successfully!', 'success');
        loadCustomers();
        cancelUpdate();
    })
    .catch(error => showMessage('Error updating customer: ' + error.message, 'error'));
}

function deleteCustomer(customerId) {
    if (confirm('Are you sure you want to delete this customer?')) {
        fetch(`${API_BASE_URL}/customers/${customerId}`, {
            method: 'DELETE',
            headers: getAuthHeaders()
        })
            .then(handleResponse)
            .then(data => {
                showMessage(data.message || 'Customer deleted successfully!', 'success');
                loadCustomers();
            })
            .catch(error => showMessage('Error deleting customer: ' + error.message, 'error'));
    }
}

function cancelUpdate() {
    document.getElementById('customer-update').style.display = 'none';
    document.getElementById('updateCustomerForm').reset();
}

// Account functions
function loadAccounts() {
    console.log('loadAccounts called');
    fetch(`${API_BASE_URL}/accounts/`, {
        headers: getAuthHeaders()
    })
        .then(handleResponse)
        .then(accounts => {
            console.log('Accounts loaded:', accounts);
            console.log('Number of accounts:', accounts.length);
            
            const accountDiv = document.getElementById('accounts');
            const accountSelect = document.getElementById('accountId');
            const filterAccountSelect = document.getElementById('filterAccountId');
            
            console.log('accountDiv:', accountDiv);
            console.log('accountSelect:', accountSelect);
            console.log('filterAccountSelect:', filterAccountSelect);
            
            if (accountDiv) {
                if (accounts.length === 0) {
                    accountDiv.innerHTML = '<p>No accounts found. Please create an account first.</p>';
                } else {
                    accountDiv.innerHTML = accounts.map(account => `
                        <div>
                            <strong>Account #${account.account_no}</strong><br>
                            Customer ID: ${account.customer_id}<br>
                            Type: ${account.account_type}<br>
                            Balance: $${account.balance}<br>
                            <button onclick="editAccount(${account.account_no})">Edit</button>
                            <button onclick="deleteAccount(${account.account_no})">Delete</button>
                            <hr>
                        </div>
                    `).join('');
                }
            }
            
            const accountOptions = accounts.map(account => 
                `<option value="${account.account_no}">Account #${account.account_no} - $${account.balance}</option>`
            ).join('');
            
            console.log('Account options HTML:', accountOptions);
            
            if (accountSelect) {
                console.log('Populating accountId select...');
                accountSelect.innerHTML = '<option value="">Select Account</option>' + accountOptions;
                console.log('accountId select now has', accountSelect.options.length, 'options');
                console.log('accountId select innerHTML:', accountSelect.innerHTML);
            } else {
                console.log('accountId select NOT FOUND!');
            }
            
            if (filterAccountSelect) {
                console.log('Populating filterAccountId select...');
                filterAccountSelect.innerHTML = '<option value="">Filter by Account</option>' + accountOptions;
                console.log('filterAccountId select now has', filterAccountSelect.options.length, 'options');
            } else {
                console.log('filterAccountId select NOT FOUND!');
            }
        })
        .catch(error => {
            console.error('Error loading accounts:', error);
            showMessage('Error loading accounts: ' + error.message, 'error');
        });
}

function addAccount(accountData) {
    fetch(`${API_BASE_URL}/accounts/`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: JSON.stringify(accountData)
    })
    .then(handleResponse)
    .then(data => {
        showMessage(data.message || 'Account created successfully!', 'success');
        loadAccounts();
        document.getElementById('addAccountForm').reset();
    })
    .catch(error => showMessage('Error creating account: ' + error.message, 'error'));
}

function editAccount(accountNo) {
    fetch(`${API_BASE_URL}/accounts/${accountNo}`, {
        headers: getAuthHeaders()
    })
        .then(handleResponse)
        .then(account => {
            document.getElementById('updateAccountId').value = account.account_no;
            document.getElementById('updateAccountType').value = account.account_type;
            document.getElementById('updateBalance').value = account.balance;
            document.getElementById('account-update').style.display = 'block';
        })
        .catch(error => showMessage('Error loading account: ' + error.message, 'error'));
}

function updateAccount(accountNo, accountData) {
    fetch(`${API_BASE_URL}/accounts/${accountNo}`, {
        method: 'PUT',
        headers: getAuthHeaders(),
        body: JSON.stringify(accountData)
    })
    .then(handleResponse)
    .then(data => {
        showMessage('Account updated successfully!', 'success');
        loadAccounts();
        cancelAccountUpdate();
    })
    .catch(error => showMessage('Error updating account: ' + error.message, 'error'));
}

function deleteAccount(accountNo) {
    if (confirm('Are you sure you want to delete this account?')) {
        fetch(`${API_BASE_URL}/accounts/${accountNo}`, {
            method: 'DELETE',
            headers: getAuthHeaders()
        })
            .then(handleResponse)
            .then(data => {
                showMessage(data.message || 'Account deleted successfully!', 'success');
                loadAccounts();
            })
            .catch(error => showMessage('Error deleting account: ' + error.message, 'error'));
    }
}

function cancelAccountUpdate() {
    document.getElementById('account-update').style.display = 'none';
    document.getElementById('updateAccountForm').reset();
}


function loadAccountTransactions() {
    const accountNo = document.getElementById('filterAccountId').value;
    if (!accountNo) {
        showMessage('Please select an account to view transactions', 'error');
        return;
    }
    
    fetch(`${API_BASE_URL}/accounts/${accountNo}/transactions`, {
        headers: getAuthHeaders()
    })
        .then(handleResponse)
        .then(transactions => {
            displayTransactions(transactions);
        })
        .catch(error => showMessage('Error loading account transactions: ' + error.message, 'error'));
}

function displayTransactions(transactions) {
    const transactionDiv = document.getElementById('transactions');
    if (transactionDiv) {
        if (transactions.length === 0) {
            transactionDiv.innerHTML = '<p>No transactions found.</p>';
        } else {
            transactionDiv.innerHTML = transactions.map(transaction => `
                <div>
                    <strong>${transaction.transaction_type.toUpperCase()}</strong><br>
                    Amount: $${transaction.amount}<br>
                    Account: ${transaction.account_no}<br>
                    Date: ${new Date(transaction.date).toLocaleString()}<br>
                    <hr>
                </div>
            `).join('');
        }
    }
}

function addTransaction(transactionData) {
    const accountNo = transactionData.account_id;
    const type = transactionData.transaction_type;
    
    if (!accountNo) {
        showMessage('Please select an account', 'error');
        return;
    }
    
    let endpoint = '';
    if (type === 'withdrawal') {
        endpoint = `/accounts/${accountNo}/withdraw`;
    } else if (type === 'deposit') {
        endpoint = `/accounts/${accountNo}/deposit`;
    } else {
        showMessage('Only withdrawal and deposit are supported', 'error');
        return;
    }
    
    fetch(`${API_BASE_URL}${endpoint}`, {
        method: 'POST',
        headers: getAuthHeaders(),
        body: JSON.stringify({ amount: transactionData.amount })
    })
    .then(handleResponse)
    .then(data => {
        showMessage(data.message || 'Transaction created successfully!', 'success');
        loadAccountTransactions();
        loadAccounts(); // Refresh account balances
        document.getElementById('addTransactionForm').reset();
    })
    .catch(error => showMessage('Error creating transaction: ' + error.message, 'error'));
}

// Form setup functions
function setupCustomerForms() {
    const addForm = document.getElementById('addCustomerForm');
    if (addForm) {
        addForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const customerData = {
                name: document.getElementById('customerName').value,
                email: document.getElementById('customerEmail').value,
                phone: document.getElementById('customerPhone').value
            };
            addCustomer(customerData);
        });
    }

    const updateForm = document.getElementById('updateCustomerForm');
    if (updateForm) {
        updateForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const customerId = document.getElementById('updateCustomerId').value;
            const customerData = {
                name: document.getElementById('updateCustomerName').value,
                email: document.getElementById('updateCustomerEmail').value,
                phone: document.getElementById('updateCustomerPhone').value
            };
            updateCustomer(customerId, customerData);
        });
    }
}

function setupAccountForms() {
    const addForm = document.getElementById('addAccountForm');
    if (addForm) {
        addForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const accountData = {
                customer_id: parseInt(document.getElementById('customerId').value),
                account_type: document.getElementById('accountType').value,
                balance: parseFloat(document.getElementById('initialBalance').value)
            };
            addAccount(accountData);
        });
    }

    const updateForm = document.getElementById('updateAccountForm');
    if (updateForm) {
        updateForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const accountNo = document.getElementById('updateAccountId').value;
            const accountData = {
                account_type: document.getElementById('updateAccountType').value,
                balance: parseFloat(document.getElementById('updateBalance').value)
            };
            updateAccount(accountNo, accountData);
        });
    }
}

function setupTransactionForms() {
    const addForm = document.getElementById('addTransactionForm');
    if (addForm) {
        addForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const transactionData = {
                account_id: parseInt(document.getElementById('accountId').value),
                transaction_type: document.getElementById('transactionType').value,
                amount: parseFloat(document.getElementById('amount').value)
            };
            addTransaction(transactionData);
        });
    }
}

// Initialize auth token from localStorage on page load
document.addEventListener('DOMContentLoaded', function() {
    authToken = localStorage.getItem('authToken');
});