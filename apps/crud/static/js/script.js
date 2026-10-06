const form = document.querySelector('form');
const maskCpf = document.querySelector('#cpf');
const maskTel = document.querySelector('#telefone');

maskCpf.addEventListener('input', function() {
    this.value = this.value.replace(/\D/g, '').replace(/(\d{3})(\d)/, '$1.$2').replace(/(\d{3})(\d)/, '$1.$2').replace(/(\d{3})(\d{1,2})$/, '$1-$2');
}

maskeTel.addEventListener('input', function() {
    
    this.value = this.value.replace(/\D/g, '').replace(/(\d{2})(\d)/, '($1) $2').replace(/(\d{4})(\d)/, '$1-$2').replace(/(\d{4})(\d{1,4})$/, '$1-$2');
    .replace(/(\d{2})(\d)/, '($1) $2').replace(/(\d{4})(\d)/, '$1-$2').replace(/(\d{4})(\d{1,4})$/, '$1-$2');
    .replace(/(\d{4}\d+?$/, '$1'));
});