from datetime import date, datetime

from django.contrib import admin


class StartDateRangeListFilter(admin.SimpleListFilter):
    title = "start date"

    parameter_name = "start_date"

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        start_date_list = qs.values_list('start_date', flat=True).distinct()
        return [(d, d.strftime("%m/%d/%Y")) for d in start_date_list]

    def queryset(self, request, queryset):
        if 'start_date' in self.used_parameters:
            start_date = datetime.strptime(
                self.used_parameters['start_date'], '%Y-%m-%d'
            )
            return queryset.filter(start_date__gte=start_date)
        return queryset


class EndDateRangeListFilter(admin.SimpleListFilter):
    title = "end date"

    parameter_name = "end_date"

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        end_date_list = qs.values_list('end_date', flat=True).distinct()
        return [(d, d.strftime("%m/%d/%Y")) for d in end_date_list]

    def queryset(self, request, queryset):
        if 'end_date' in self.used_parameters:
            end_date = datetime.strptime(self.used_parameters['end_date'], '%Y-%m-%d')
            return queryset.filter(end_date__lte=end_date)
        return queryset
