import random
import pandas as pd

#Generate a list of workers with random attributes
workers = []
def generate_workers(num_workers = 400):

     first_names = ["John", "Jane", "Michael", "Emily","Abdul" "David", "Sarah", 
                  "Robert", "Fatu", "William", "Lisa", "Joe-Henry", "Aminata"]
     
     last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", 
                "Koroma", "Davis", "Kamara", "Vandy", "Sesay", "Sunders"]

     genders = ["Male", "Female"]

     for i in range(num_workers):
        worker = {
            "id": i + 1,
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "gender": random.choice(genders),
            "salary": random.randint(5000, 35000)
        }
        workers.append(worker)
    
     return workers


def generate_payment_slips(workers):
    """Generate payment slips with employee levels based on conditions"""
    payment_slips = []
    
    for worker in workers:
        try:
            # Copy worker data
            slip = worker.copy()
            
            # Initialize employee level
            slip["employee_level"] = "Standard"
            
            # Apply conditional logic
            if 10000 < worker["salary"] < 20000:
                slip["employee_level"] = "A1"
            elif 7500 < worker["salary"] < 30000 and worker["gender"] == "Female":
                slip["employee_level"] = "A5-F"
                
            payment_slips.append(slip)  # Intentional error for exception handling
            
        except Exception as e:
            print(f"Error processing worker {worker.get('id', 'unknown')}: {str(e)}")
            continue
    
    return payment_slips

def main():
    try:
        # Generate 400 workers
        workers = generate_workers(400)
        
        # Generate payment slips
        payment_slips = generate_payment_slips(workers)
        
        # Convert to DataFrame and save to CSV
        df = pd.DataFrame(payment_slips)
        df.to_csv("payment_slips.csv", index=False)
        print("Payment slips generated successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()