def graph_view(request):
    selected_date = request.GET.get(
        'date', date.today().isoformat())  # Format 'YYYY-MM-DD'
    selected_date = parse_date(selected_date)

    # Aggregate the count of each FoodMenu category from OrderItems on the selected date
    category_counts = (OrderItem.objects
                       .filter(orderID__date=selected_date)
                       .values('fooditem__foodmenu__categories')
                       .annotate(total=Count('fooditem__foodmenu__categories'))
                       .order_by())

    # Prepare data for the pie chart
    labels = [item['fooditem__foodmenu__categories']
              for item in category_counts]
    values = [item['total'] for item in category_counts]

    # Create the pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    chart = plot(fig, output_type='div')

    context = {
        'chart': chart,
    }

    return render(request, 'admin/daily_pie_chart.html', context)
