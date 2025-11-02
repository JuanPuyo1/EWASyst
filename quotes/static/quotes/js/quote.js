document.addEventListener('DOMContentLoaded', function() {
    var discountCheckbox = document.getElementById('quote_discount');
    var discountFields = document.getElementById('discount_fields');
    discountCheckbox.addEventListener('change', function() {
        discountFields.style.display = this.checked ? 'block' : 'none';
    });
});