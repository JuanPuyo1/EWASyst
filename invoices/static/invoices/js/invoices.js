document.addEventListener('DOMContentLoaded', function() {
    var discountCheckbox = document.getElementById('invoice_discount');
    var discountFields = document.getElementById('discount_fields');
    var invoiceStatus = document.getElementById('invoice_status_id');
    discountCheckbox.addEventListener('change', function() {
        discountFields.style.display = this.checked ? 'block' : 'none';
    });
});