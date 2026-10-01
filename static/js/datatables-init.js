$(document).ready(function () {
  $('table.table-datatable').each(function () {
    $(this).DataTable({
      paging: false,
      info: false,
      lengthChange: false,
      order: [],
      language: { url: 'https://cdn.datatables.net/plug-ins/2.1.8/i18n/pt-BR.json' }
    });
  });
});
