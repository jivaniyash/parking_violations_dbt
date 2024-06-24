-- source: https://docs.getdbt.com/guides/best-practices/writing-custom-generic-tests#generic-tests-with-default-config-values
{% test my_not_null(model, column_name) %}

    select *
    from {{ model }}
    where {{ column_name }} = 0

{% endtest %}