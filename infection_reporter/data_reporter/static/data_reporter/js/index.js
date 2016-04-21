/**
 * Created by Vango on 20-Apr-16.
 */

$(document).ready(function () {
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
        $.fn.dataTable.tables({visible: true, api: true}).columns.adjust();
    });

    var diseaseId = $('li.active').attr('data-disease-id');

    var humanCasesTable = $('#human-cases-table').DataTable({
        ajax: {
            "url": "http://localhost:8000/data-reporter/human/cases/" + diseaseId,
            "dataType": "json"
        },
        columns: [
            {
                "data": "case_count",
                "class": "text-center",
                "render": function (data, type, full, meta) {
                    if (full.disease.urgent || full.case_count > 3) {
                        return "<span class='urgent'>" + data + "</span>"
                    } else if (full.recovery_rate == 100) {
                        return "<span class='ok'>" + data + "</span>"
                    }
                    return "<span>" + data + "</span>";
                }
            },
            {
                "data": "disease",
                "render": function (data, type, full, meta) {
                    return '<span>' + data.name + '</span>';
                }
            },
            {"data": "district"},
            {"data": "village"},
            {"data": "report_avg"},
            {"data": "hospitalization_avg"},
            {"data": "sampling_avg"},
            {"data": "laboratory_avg"},
            {"data": "treatment_avg"},
            {"data": "min_age"},
            {"data": "max_age"},
            {"data": "age_avg"},
            {
                "data": "vaccination_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "death_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "recovery_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "sequela_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "attack_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            }
        ]
    });
    var animalCasesTable = $('#animal-cases-table').DataTable({
        ajax: {
            "url": "http://localhost:8000/data-reporter/animal/cases/" + diseaseId,
            "dataType": "json"
        },
        columns: [
            {"data": "case_count"},
            {
                "data": "disease",
                "render": function (data, type, full, meta) {
                    return '<span>' + data.name + '</span>';
                }
            },
            {"data": "district"},
            {"data": "village"},
            {
                "data": "morbidity_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "mortality_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            },
            {
                "data": "fatality_rate",
                "render": function (data, type, full, meta) {
                    return '<span>' + data + '%</span>';
                }
            }
        ]
    });

    // setInterval(function () {
    //     humanCasesTable.ajax.reload();
    //     animalCasesTable.ajax.reload();
    // }, 60000);

    $('#add-human-case').on('click', function (event) {

    });
    $('#add-animal-case').on('click', function (event) {
        
    });
});