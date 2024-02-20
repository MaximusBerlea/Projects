print("Welcome to the triathalon awards calculator! \nEnter your results in minutes!")
print()
swimming_time = float(input("Please enter your swimming time: ")) 
cycling_time = float(input("Please enter your cycling time: ")) 
running_time = float(input("Please enter your running time: "))

total_time = swimming_time + cycling_time + running_time 

print(f"Your total time taken to complete the traithalon was: {total_time} minutes!")


if total_time <= 100:
    print("\nCongragulations! You have won the Provincial Colours Award!")
elif total_time > 100 and total_time <= 105:
    print("\nWell done! You have won the Provincial Half Colours Award!")
elif total_time > 105 and total_time <= 110:
    print("\nGreat Effort! You have won the Provincial Scroll Award!")
else:
    print("\nSorry...You have failed to achieve an Award. Better luck next time!")