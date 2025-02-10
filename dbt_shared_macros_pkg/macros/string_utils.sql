{% macro suffix_worked(column_name) %}
    CONCAT({{ column_name }},'_worked')
{% endmacro %}