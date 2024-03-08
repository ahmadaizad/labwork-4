# Custom flower sales data
flower_sales_data = [
    {"product": "Rose", "units_sold": 150, "customer_reviews": [4, 5, 3, 4, 5]},
    {"product": "Tulip", "units_sold": 120, "customer_reviews": [3, 4, 4, 3, 5]},
    {"product": "Lily", "units_sold": 100, "customer_reviews": [4, 3, 4, 3, 4]},
    {"product": "Sunflower", "units_sold": 80, "customer_reviews": [5, 4, 3, 5, 4]},
    {"product": "Daisy", "units_sold": 90, "customer_reviews": [3, 3, 3, 4, 4]},
    {"product": "Orchid", "units_sold": 110, "customer_reviews": [5, 5, 4, 4, 3]},
    {"product": "Carnation", "units_sold": 70, "customer_reviews": [4, 3, 3, 4, 4]},
    {"product": "Daffodil", "units_sold": 130, "customer_reviews": [3, 4, 4, 3, 5]},
    {"product": "Hyacinth", "units_sold": 85, "customer_reviews": [4, 3, 3, 4, 5]},
    {"product": "Peony", "units_sold": 95, "customer_reviews": [5, 4, 4, 5, 3]},
    {"product": "Crocus", "units_sold": 105, "customer_reviews": [4, 3, 5, 4, 3]},
    {"product": "Iris", "units_sold": 115, "customer_reviews": [3, 4, 5, 3, 4]},
    {"product": "Chrysanthemum", "units_sold": 125, "customer_reviews": [4, 5, 3, 4, 5]},
    {"product": "Freesia", "units_sold": 75, "customer_reviews": [5, 4, 3, 5, 4]},
    {"product": "Gladiolus", "units_sold": 140, "customer_reviews": [4, 3, 4, 3, 4]},
    {"product": "Anemone", "units_sold": 65, "customer_reviews": [3, 3, 3, 4, 4]},
    {"product": "Begonia", "units_sold": 145, "customer_reviews": [4, 5, 3, 5, 4]},
    {"product": "Amaryllis", "units_sold": 60, "customer_reviews": [5, 4, 3, 4, 3]},
    {"product": "Snapdragon", "units_sold": 155, "customer_reviews": [4, 3, 4, 3, 4]},
    {"product": "Zinnia", "units_sold": 110, "customer_reviews": [3, 4, 5, 3, 5]}
]

# 1. Total Units Sold Calculation
total_units_sold = sum(item["units_sold"] for item in flower_sales_data)
print("Total Units Sold:", total_units_sold)

# 2. Highest Sales Identification
highest_sales_flower = max(flower_sales_data, key=lambda x: x["units_sold"])
print("Flower with the Highest Sales:", highest_sales_flower["product"])

# 3. Above-Average Customer Reviews Identification
above_average_reviews = [item["product"] for item in flower_sales_data if sum(item["customer_reviews"]) / len(item["customer_reviews"]) > 3]
print("Flowers with Above-Average Customer Reviews:", above_average_reviews)

# 4. Average Customer Review Score Calculation
total_reviews = sum(sum(item["customer_reviews"]) for item in flower_sales_data)
total_reviews_count = sum(len(item["customer_reviews"]) for item in flower_sales_data)
average_review_score = total_reviews / total_reviews_count
print("Average Customer Review Score:", round(average_review_score, 2))

# 5. Below-Average Sales Identification
average_units_sold = total_units_sold / len(flower_sales_data)
below_average_sales = [(item["product"], item["units_sold"], sum(item["customer_reviews"]) / len(item["customer_reviews"])) for item in flower_sales_data if item["units_sold"] < average_units_sold]
print("Flowers with Below-Average Sales:")
for flower in below_average_sales:
    print(f"Product: {flower[0]}, Units Sold: {flower[1]}, Average Customer Review: {round(flower[2], 2)}")
