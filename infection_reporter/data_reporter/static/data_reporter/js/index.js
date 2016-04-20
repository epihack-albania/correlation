/**
 * Created by Vango on 20-Apr-16.
 */

$(document).ready(function () {
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        $.fn.dataTable.tables({visible: true, api: true}).columns.adjust();
    });

    $('#human-cases-table').DataTable({
        ajax: {
            "url": "http://192.168.176.86:8000/data-reporter/human/cases/",
            "dataType": "json"

        },
        columns: [{"data": "case_count"},
            {"data": "residency_region"},
            {"data": "residency_district"},
            {"data": "residency_commune"},
            {"data": "residency_village"},
            {"data": "period"},
            {"data": "disease"},
            {"data": "confirm_count"},
            {"data": "probable_count"},
            {"data": "suspected_count"},
            {"data": "severity_level"}],
        fnRowCallback: function (nRow, aData, iDisplayIndex) {
            nRow.className = "alert-danger"
        },
        scrollY: 700,
        scrollCollapse: true,
        paging: false
    });
    $('#myTable2').DataTable({
        ajax: {
            "url": "http://192.168.176.86:8000/data-reporter/animal/cases/",
            "dataType": "json"

        },
        columns: [{"data": "case_count"},
            {"data": "residency_region"},
            {"data": "residency_district"},
            {"data": "residency_commune"},
            {"data": "residency_village"},
            {"data": "period"},
            {"data": "disease"},
            {"data": "confirm_count"},
            {"data": "probable_count"},
            {"data": "suspected_count"},
            {"data": "severity_level"}],
        scrollY: 700,
        scrollCollapse: true,
        paging: false
    });
    // Apply a search to the second table for the demo
    $('#myTable2').DataTable().draw();
});