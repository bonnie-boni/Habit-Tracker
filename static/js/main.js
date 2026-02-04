// Theme Toggle
document.getElementById('themeToggle')?.addEventListener('click', function() {
    const body = document.body;
    const theme = body.classList.contains('light-mode') ? 'dark' : 'light';
    
    body.classList.toggle('light-mode');
    localStorage.setItem('theme', theme);
});

// Load saved theme
window.addEventListener('DOMContentLoaded', function() {
    const savedTheme = localStorage.getItem('theme') || 'dark';
    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
    }
});

// Profile Dropdown
document.getElementById('profileButton')?.addEventListener('click', function() {
    const menu = document.getElementById('dropdownMenu');
    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
});

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const dropdown = document.querySelector('.profile-dropdown');
    if (dropdown && !dropdown.contains(event.target)) {
        const menu = document.getElementById('dropdownMenu');
        if (menu) menu.style.display = 'none';
    }
});

// Sidebar Toggle for Mobile
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar?.classList.toggle('open');
}
