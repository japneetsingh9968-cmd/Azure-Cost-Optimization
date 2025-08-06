def main():
    pre_cost = get_cost("2023-Q1")
    post_cost = get_cost("2023-Q3")
    savings = pre_cost - post_cost
    
    print(f"Monthly savings: ${savings:,.2f}")
    
    if savings < EXPECTED_SAVINGS * 0.8:
        alert_admin(f"Savings below threshold: ${savings}")

if __name__ == "__main__":
    main()